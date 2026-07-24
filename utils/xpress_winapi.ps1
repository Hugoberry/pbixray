# Decompress a VertiPaq xpress8 (chunked MS-XCA Xpress/LZ77) slice via the
# native Windows decompressor in ntdll (RtlDecompressBuffer). PowerShell
# counterpart to utils/xpress_winapi.py -- an experimental winapi alternative
# to the Cython xpress8 port's decompress_chunked().
#
# xpress8 slice layout (see xpress8.Xpress8.decompress_chunked):
#   repeated: [u16 uncompressed_size][u16 compressed_size][compressed body]
#   when the two sizes are equal the body is stored verbatim (not compressed).
#
# Note: cabinet.dll's Compress/Decompress will NOT decode these slices -- it
# wraps data in its own container. ntdll's RtlDecompressBuffer takes a raw
# MS-XCA buffer, which is what each chunk body is.
#
# Usage:
#   .\xpress_winapi.ps1 -InPath slice.bin -OutPath out.bin

param(
    [Parameter(Mandatory)] [string] $InPath,
    [Parameter(Mandatory)] [string] $OutPath
)

Add-Type -TypeDefinition @'
using System;
using System.Runtime.InteropServices;
namespace Xpress {
  public static class Ntdll {
    // COMPRESSION_FORMAT_XPRESS = 0x0003 (plain LZ77, no Huffman).
    [DllImport("ntdll.dll")]
    public static extern int RtlDecompressBuffer(
        ushort format, byte[] dst, int dstLen, byte[] src, int srcLen, out int finalSize);
  }
}
'@

$XPRESS = 0x0003
$data = [System.IO.File]::ReadAllBytes((Resolve-Path $InPath))
$out = New-Object System.IO.MemoryStream

$pos = 0
while ($pos -lt $data.Length) {
    $u = [BitConverter]::ToUInt16($data, $pos)
    $c = [BitConverter]::ToUInt16($data, $pos + 2)
    $pos += 4
    if ($u -eq $c) {
        # Stored verbatim.
        $out.Write($data, $pos, $c)
    } else {
        $body = New-Object byte[] $c
        [Array]::Copy($data, $pos, $body, 0, $c)
        $dst = New-Object byte[] $u
        $final = 0
        $st = [Xpress.Ntdll]::RtlDecompressBuffer($XPRESS, $dst, $u, $body, $c, [ref]$final)
        if ($st -ne 0) {
            throw ("RtlDecompressBuffer failed at offset {0}: NTSTATUS 0x{1:x8}" -f ($pos - 4), $st)
        }
        $out.Write($dst, 0, $final)
    }
    $pos += $c
}

$bytes = $out.ToArray()
[System.IO.File]::WriteAllBytes($OutPath, $bytes)
Write-Host "Decompressed $($data.Length) -> $($bytes.Length) bytes into $OutPath"
