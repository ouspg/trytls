def indent(text, by=4, first_line=True):
    r"""
    >>> indent("a\nb\nc", by=1) == ' a\n b\n c'
    True
    """

    spaces = " " * by
    lines = text.splitlines(True)
    prefix = lines.pop(0) if (lines and not first_line) else ""
    return prefix + "".join(spaces + line for line in lines)
