"""Type stubs for plotext._settings.themes."""

from typing import Any

themes: dict[str, dict[str, Any]] = ...

def add_theme(
    name: str,
    canvas: Any = None,
    text: Any = None,
    sequence: Any = None,
    grid: Any = None,
) -> None: ...
