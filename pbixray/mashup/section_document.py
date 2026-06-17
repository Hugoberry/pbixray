"""Lexical splitter for a Power Query ``Section1.m`` document ([MS-QDEFF] 2.3.2).

This is deliberately *not* a full M parser. It scans the section document into
its top-level ``shared`` members, respecting M lexical structure — double-quoted
strings (with ``""`` escaping), quoted identifiers ``#"..."``, ``//`` line
comments, ``/* */`` block comments, and ``()[]{}`` bracket nesting — and reads
each member's optional postfix ``meta`` record to classify parameters.

A member is a *parameter* when its metadata record contains
``IsParameterQuery=true``; otherwise it is a *query*.
"""
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class MQuery:
    """A single section member parsed from ``Section1.m``."""
    name: str
    expression: str
    is_parameter: bool = False
    param_type: Optional[str] = None
    default_value: Optional[str] = None
    allowed_values: List[str] = field(default_factory=list)
    is_required: Optional[bool] = None

    @property
    def kind(self):
        return "parameter" if self.is_parameter else "query"


_IDENT_CHARS = set(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
)
_OPEN = "([{"
_CLOSE = ")]}"


def _mask(text):
    """Blank out string/comment contents (preserving length) so structural
    scanning for brackets, ``;``, ``=`` and keywords is safe."""
    out = list(text)
    i, n = 0, len(text)
    state = None  # None | 'str' | 'line' | 'block'
    while i < n:
        c = text[i]
        if state is None:
            if c == '"':
                state = 'str'
                out[i] = ' '
            elif c == '/' and i + 1 < n and text[i + 1] == '/':
                state = 'line'
                out[i] = out[i + 1] = ' '
                i += 2
                continue
            elif c == '/' and i + 1 < n and text[i + 1] == '*':
                state = 'block'
                out[i] = out[i + 1] = ' '
                i += 2
                continue
        elif state == 'str':
            if c == '"':
                if i + 1 < n and text[i + 1] == '"':  # escaped quote
                    out[i] = out[i + 1] = ' '
                    i += 2
                    continue
                state = None
            out[i] = ' '
        elif state == 'line':
            if c == '\n':
                state = None
            else:
                out[i] = ' '
        elif state == 'block':
            if c == '*' and i + 1 < n and text[i + 1] == '/':
                out[i] = out[i + 1] = ' '
                state = None
                i += 2
                continue
            out[i] = ' '
        i += 1
    return ''.join(out)


def _strip_comments(text):
    """Remove ``//`` and ``/* */`` comments (preserving string literals)."""
    out, i, n, state = [], 0, len(text), None
    while i < n:
        c = text[i]
        if state is None:
            if c == '"':
                state = 'str'
                out.append(c)
            elif c == '/' and i + 1 < n and text[i + 1] == '/':
                state = 'line'
                i += 2
                continue
            elif c == '/' and i + 1 < n and text[i + 1] == '*':
                state = 'block'
                i += 2
                continue
            else:
                out.append(c)
        elif state == 'str':
            out.append(c)
            if c == '"':
                if i + 1 < n and text[i + 1] == '"':
                    out.append(text[i + 1])
                    i += 2
                    continue
                state = None
        elif state == 'line':
            if c == '\n':
                state = None
                out.append(c)
        elif state == 'block':
            if c == '*' and i + 1 < n and text[i + 1] == '/':
                state = None
                i += 2
                continue
        i += 1
    return ''.join(out)


def _is_word(mask, start, end):
    """True if mask[start:end] is bounded by non-identifier characters."""
    before = mask[start - 1] if start > 0 else ''
    after = mask[end] if end < len(mask) else ''
    return before not in _IDENT_CHARS and after not in _IDENT_CHARS


def _split_top_level(text, mask, separator):
    """Split ``text`` on ``separator`` characters that sit at bracket depth 0."""
    parts, depth, start = [], 0, 0
    for i, c in enumerate(mask):
        if c in _OPEN:
            depth += 1
        elif c in _CLOSE:
            depth -= 1
        elif c == separator and depth == 0:
            parts.append(text[start:i])
            start = i + 1
    parts.append(text[start:])
    return parts


def _find_assignment(mask):
    """Index of the member-assignment ``=`` (depth 0, not part of => >= <= <>)."""
    depth = 0
    for i, c in enumerate(mask):
        if c in _OPEN:
            depth += 1
        elif c in _CLOSE:
            depth -= 1
        elif c == '=' and depth == 0:
            prev = mask[i - 1] if i > 0 else ''
            nxt = mask[i + 1] if i + 1 < len(mask) else ''
            if nxt == '>' or prev in '<>=':
                continue
            return i
    return -1


def _strip_quotes(literal):
    """Turn an M string literal into its text value (handles ``""`` escapes)."""
    s = literal.strip()
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        return s[1:-1].replace('""', '"')
    return s


def _parse_name(left):
    """Extract the member name from the left side of the assignment."""
    s = _strip_comments(left).strip()
    if s.startswith('['):  # leading literal-attribute record
        m = _mask(s)
        depth = 0
        for i, c in enumerate(m):
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
                if depth == 0:
                    s = s[i + 1:].strip()
                    break
    if s.startswith('shared') and (len(s) == 6 or s[6] not in _IDENT_CHARS):
        s = s[6:].strip()
    s = s.strip()
    if s.startswith('#"') and s.endswith('"') and len(s) > 3:
        return s[2:-1]
    return s


def _split_meta(right):
    """Split off a member-level postfix ``meta [record]`` from the right side.

    The ``meta`` operator can also appear *inside* an expression, so only a
    depth-0 ``meta`` whose record literal closes at the very end of the
    statement is treated as the member's metadata; anything else is left as part
    of the expression.
    """
    m = _mask(right)
    positions = []
    depth = 0
    for i, c in enumerate(m):
        if c in _OPEN:
            depth += 1
        elif c in _CLOSE:
            depth -= 1
        elif depth == 0 and m[i:i + 4] == 'meta' and _is_word(m, i, i + 4):
            positions.append(i)
    for pos in reversed(positions):
        j = pos + 4
        while j < len(m) and m[j] in ' \t\r\n':
            j += 1
        if j >= len(m) or m[j] != '[':  # member metadata is always a record literal
            continue
        depth, end = 0, -1
        for k in range(j, len(m)):
            if m[k] == '[':
                depth += 1
            elif m[k] == ']':
                depth -= 1
                if depth == 0:
                    end = k
                    break
        if end >= 0 and m[end + 1:].strip() == '':
            return right[:pos].strip(), right[j:end + 1]
    return right.strip(), None


def _parse_record(record_text):
    """Parse a top-level ``[ key = value, ... ]`` record into a dict of raw values."""
    s = record_text.strip()
    if not s.startswith('['):
        return {}
    m = _mask(s)
    depth, end = 0, -1
    for i, c in enumerate(m):
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
            if depth == 0:
                end = i
                break
    if end < 0:
        return {}
    inner = s[1:end]
    out = {}
    for field_text in _split_top_level(inner, _mask(inner), ','):
        fmask = _mask(field_text)
        eq = _find_assignment(fmask)
        if eq < 0:
            continue
        key = field_text[:eq].strip()
        if key.startswith('#"') and key.endswith('"'):
            key = key[2:-1]
        out[key] = field_text[eq + 1:].strip()
    return out


def _as_bool(raw):
    if raw is None:
        return None
    return raw.strip().lower() == 'true'


def _as_list(raw):
    if raw is None:
        return []
    s = raw.strip()
    if not (s.startswith('{') and s.endswith('}')):
        return []
    inner = s[1:-1]
    return [_strip_quotes(item) for item in _split_top_level(inner, _mask(inner), ',') if item.strip()]


def _parse_member(statement):
    mask = _mask(statement)
    eq = _find_assignment(mask)
    if eq < 0:
        return None  # not a member (e.g. the `section Section1` header)
    name = _parse_name(statement[:eq])
    if not name:
        return None
    expression, meta_text = _split_meta(statement[eq + 1:])
    meta = _parse_record(meta_text) if meta_text else {}
    is_param = _as_bool(meta.get('IsParameterQuery')) or False
    return MQuery(
        name=name,
        expression=expression.strip(),
        is_parameter=is_param,
        param_type=_strip_quotes(meta['Type']) if 'Type' in meta else None,
        default_value=_strip_quotes(meta['DefaultValue']) if 'DefaultValue' in meta else None,
        allowed_values=_as_list(meta.get('List')),
        is_required=_as_bool(meta.get('IsParameterQueryRequired')),
    )


def parse_section_document(text):
    """Parse a ``Section1.m`` document into a list of :class:`MQuery`."""
    if not text:
        return []
    mask = _mask(text)
    queries = []
    for statement in _split_top_level(text, mask, ';'):
        if not statement.strip():
            continue
        member = _parse_member(statement)
        if member is not None:
            queries.append(member)
    return queries
