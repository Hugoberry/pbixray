<#
.SYNOPSIS
  Light-touch peek into the Power Pivot / Analysis Services data model embedded
  in an .xlsx (or .pbix). Surfaces the ABF metadata XML logs (which are stored
  uncompressed) and previews one embedded file, decompressing it with the native
  Windows xpress8 path (ntdll RtlDecompressBuffer) that we validated separately.

  This is deliberately a *glimpse* only: header + virtual directory + backup-log
  manifest, plus a single decompressed sample. All the heavy VertiPaq column /
  RLE / dictionary decoding is left to pbixray.

.PARAMETER Path
  Path to a .xlsx or old .pbix file.

.PARAMETER ListFiles
  List every embedded backup file (friendly path, compressed size, offset).

.PARAMETER Dump
  Friendly-name substring of an embedded file to decompress and preview.

.EXAMPLE
  .\powerpivot_peek.ps1 -Path "Book.xlsx"
  .\powerpivot_peek.ps1 -Path "Book.xlsx" -ListFiles
  .\powerpivot_peek.ps1 -Path "Book.xlsx" -Dump ".xml"
#>
param(
    [Parameter(Mandatory)] [string] $Path,
    [switch] $ListFiles,
    [string] $Dump,
    [switch] $Full,          # print the whole decoded file instead of a preview
    [string] $OutFile        # save the full decompressed bytes to this path
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.IO.Compression.FileSystem

Add-Type -TypeDefinition @'
using System;
using System.Runtime.InteropServices;
namespace PP {
  public static class Nt {
    // COMPRESSION_FORMAT_XPRESS = 3 (raw MS-XCA LZ77 -- what VertiPaq xpress8 chunks are)
    [DllImport("ntdll.dll")]
    public static extern int RtlDecompressBuffer(
        ushort fmt, byte[] dst, int dstLen, byte[] src, int srcLen, out int finalSize);
  }
}
'@

# ---------- helpers ----------
function Slice([byte[]]$src, [int]$off, [int]$len) {
    $d = New-Object byte[] $len
    [Array]::Copy($src, $off, $d, 0, $len)
    ,$d
}

function Xml-FromBytes([byte[]]$bytes) {
    # Honors the <?xml encoding=...?> declaration (utf-8 or utf-16).
    $doc = New-Object System.Xml.XmlDocument
    $doc.Load((New-Object System.IO.MemoryStream (,$bytes)))
    $doc
}

function Text([System.Xml.XmlNode]$node, [string]$name) {
    $n = $node.SelectSingleNode("*[local-name()='$name']")
    if ($n) { $n.InnerText } else { $null }
}

# Decompress a VertiPaq slice: xpress8-chunked when ApplyCompression, else raw.
function Decode-Slice([byte[]]$data, [bool]$compressed) {
    if (-not $compressed) { return ,$data }
    $out = New-Object System.IO.MemoryStream
    $pos = 0
    while ($pos -lt $data.Length) {
        $u = [BitConverter]::ToUInt16($data, $pos)
        $c = [BitConverter]::ToUInt16($data, $pos + 2)
        $pos += 4
        if ($u -eq $c) {
            $out.Write($data, $pos, $c)                      # stored verbatim
        } else {
            $body = Slice $data $pos $c
            $dst = New-Object byte[] $u
            $final = 0
            $st = [PP.Nt]::RtlDecompressBuffer(3, $dst, $u, $body, $c, [ref]$final)
            if ($st -ne 0) { throw ("RtlDecompressBuffer NTSTATUS 0x{0:x8}" -f $st) }
            $out.Write($dst, 0, $final)
        }
        $pos += $c
    }
    ,$out.ToArray()
}

function Preview([byte[]]$b, [int]$max = 1400) {
    if ($b.Length -ge 2 -and $b[0] -eq 0xff -and $b[1] -eq 0xfe) {
        $s = [System.Text.Encoding]::Unicode.GetString($b)
    } elseif (($b[0..([Math]::Min(200,$b.Length-1))] | Where-Object { $_ -lt 9 }).Count -eq 0) {
        $s = [System.Text.Encoding]::UTF8.GetString($b)
    } else {
        $hex = ($b[0..([Math]::Min(63,$b.Length-1))] | ForEach-Object { $_.ToString('x2') }) -join ' '
        return "[binary] " + $hex
    }
    if ($s.Length -gt $max) { $s.Substring(0, $max) + "`n... (truncated)" } else { $s }
}

# ---------- read the model member ----------
$zip = [System.IO.Compression.ZipFile]::OpenRead((Resolve-Path $Path))
try {
    $entry = $zip.Entries | Where-Object { $_.FullName -in @('xl/model/item.data','DataModel') } | Select-Object -First 1
    if (-not $entry) { throw "No embedded model found (need xl/model/item.data or DataModel)." }
    $ms = New-Object System.IO.MemoryStream
    $es = $entry.Open(); $es.CopyTo($ms); $es.Close()
    $buf = $ms.ToArray()
} finally { $zip.Dispose() }

Write-Host "File   : $Path"
Write-Host "Member : $($entry.FullName)  ($($buf.Length) bytes)"

# ---------- detect format ----------
$head = [System.Text.Encoding]::Unicode.GetString((Slice $buf 0 ([Math]::Min(204,$buf.Length))))
if ($head -like '*STREAM_STORAGE_SIGNATURE*') {
    Write-Host "Format : uncompressed ABF  (winapi xpress8 path applies)`n"
} elseif ($head -like '*XPress9*' -or $head -like '*XPrs9*') {
    Write-Host "Format : XPress9-compressed`n"
    Write-Warning "This model is XPress9-compressed. The Windows compression APIs cannot decode XPress9 -- use pbixray (Cython xpress9) for this file."
    return
} else {
    Write-Warning "Unrecognized model stream signature."; return
}

# ---------- backup-log header (bytes 72..4096, utf-16, null-padded) ----------
$hdrStr = [System.Text.Encoding]::Unicode.GetString((Slice $buf 72 (4096 - 72))).TrimEnd([char]0)
[xml]$hdr = $hdrStr
$applyCompression = (Text $hdr.DocumentElement 'ApplyCompression') -eq 'true'
$errorCode        = (Text $hdr.DocumentElement 'ErrorCode') -eq 'true'
$filesCount       = [int](Text $hdr.DocumentElement 'Files')
$dataSize         = [int](Text $hdr.DocumentElement 'DataSize')
$vdOffset         = [int](Text $hdr.DocumentElement 'm_cbOffsetHeader')

# ---------- virtual directory (file registry) ----------
$vd = Xml-FromBytes (Slice $buf $vdOffset $dataSize)
$vdFiles = @{}
$vdList = @()
foreach ($f in $vd.SelectNodes("//*[local-name()='BackupFile']")) {
    $rec = [pscustomobject]@{
        StoragePath = Text $f 'Path'
        Size        = [int](Text $f 'Size')
        Offset      = [int](Text $f 'm_cbOffsetHeader')
    }
    $vdFiles[$rec.StoragePath] = $rec
    $vdList += $rec
}

# ---------- backup-log manifest (last registry entry, uncompressed) ----------
$logEntry = $vdList[-1]
$logLen = if ($errorCode) { $logEntry.Size - 4 } else { $logEntry.Size }
$log = Xml-FromBytes (Slice $buf $logEntry.Offset $logLen)
$groups = $log.SelectNodes("//*[local-name()='FileGroup']")
$persistRoot = ''
if ($groups.Count -gt 1) { $persistRoot = (Text $groups.Item(1) 'PersistLocationPath') + '\' }

# Join friendly paths (backup log) to offsets/sizes (virtual directory).
$files = @()
foreach ($g in $groups) {
    foreach ($bf in $g.SelectNodes("*[local-name()='FileList']/*[local-name()='BackupFile']")) {
        $sp = Text $bf 'StoragePath'
        if ($vdFiles.ContainsKey($sp)) {
            $p = Text $bf 'Path'
            if ($persistRoot -and $p.StartsWith($persistRoot)) { $p = $p.Substring($persistRoot.Length) }
            $files += [pscustomobject]@{
                Name   = ($p -split '\\')[-1]
                Path   = $p
                Size   = $vdFiles[$sp].Size
                Offset = $vdFiles[$sp].Offset
            }
        }
    }
}

# ---------- summary glimpse ----------
Write-Host "== Backup log =="
Write-Host ("  Object            : {0}" -f (Text $log.DocumentElement 'ObjectName'))
Write-Host ("  SyncVersion       : {0}" -f (Text $log.DocumentElement 'BackupRestoreSyncVersion'))
Write-Host ("  ApplyCompression  : {0}" -f $applyCompression)
Write-Host ("  ErrorCode trailer : {0}" -f $errorCode)
Write-Host ("  Languages         : {0}" -f (($log.SelectNodes("//*[local-name()='Language']") | ForEach-Object { $_.InnerText }) -join ', '))
Write-Host ("  File groups       : {0}" -f $groups.Count)
Write-Host ("  Embedded files    : {0} (header says {1})" -f $files.Count, $filesCount)
Write-Host ""

if ($ListFiles) {
    Write-Host "== Embedded files (by size) =="
    $files | Sort-Object Size -Descending |
        Format-Table @{N='Size';E={'{0:N0}' -f $_.Size};A='right'}, Offset, Name -AutoSize
}

# ---------- winapi preview of one embedded file ----------
$target = $null
if ($Dump) {
    $target = $files | Where-Object { $_.Path -like "*$Dump*" } | Sort-Object Size | Select-Object -First 1
    if (-not $target) { Write-Warning "No embedded file matching '*$Dump*'."; }
} else {
    # default: smallest .xml metadata file, else smallest overall
    $target = $files | Where-Object { $_.Name -like '*.xml' } | Sort-Object Size | Select-Object -First 1
    if (-not $target) { $target = $files | Sort-Object Size | Select-Object -First 1 }
}

if ($target) {
    Write-Host "== winapi preview: $($target.Path) =="
    $sliceLen = if ($errorCode) { $target.Size - 4 } else { $target.Size }
    $raw = Slice $buf $target.Offset $sliceLen
    try {
        $dec = Decode-Slice $raw $applyCompression
        Write-Host ("  decompressed {0} -> {1} bytes via ntdll xpress8`n" -f $target.Size, $dec.Length)
        if ($OutFile) {
            [System.IO.File]::WriteAllBytes($OutFile, $dec)
            Write-Host "  saved full file -> $OutFile`n"
        }
        Write-Host (Preview $dec ($(if ($Full) { [int]::MaxValue } else { 1400 })))
    } catch {
        Write-Warning "decode failed: $_"
    }
}
