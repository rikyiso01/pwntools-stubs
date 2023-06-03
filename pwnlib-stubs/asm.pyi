def asm(
    code: str,
    vma: int = ...,
    extract: bool = ...,
    shared: bool = ...,
    **kwargs: dict[str, str]
) -> bytes: ...
def disasm(
    data: bytes,
    vma: int = ...,
    byte: bool = ...,
    offset: bool = ...,
    **kwargs: dict[str, str]
) -> str: ...
