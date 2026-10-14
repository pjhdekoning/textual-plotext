"""Type stubs for the plotext wrapper module.

Re-exports the public plotext symbols needed by the Plot class.
"""

from typing import Any


def sin(
    periods: int = ...,
    length: int = ...,
    amplitude: int = ...,
    phase: float = ...,
    decay: int = ...,
) -> list[float]: ...

def square(
    periods: int = ...,
    length: int = ...,
    amplitude: float = ...,
) -> list[int]: ...

def colorize(
    string: str = ...,
    fullground: str | int | tuple[int, int, int] | None = ...,
    style: str | None = ...,
    background: str | int | tuple[int, int, int] | None = ...,
    show: bool = ...,
) -> str: ...

def uncolorize(string: str) -> str: ...

platform: str = ...

def add_theme(
    name: str,
    canvas: Any = None,
    text: Any = None,
    sequence: Any = None,
    grid: Any = None,
) -> None: ...
