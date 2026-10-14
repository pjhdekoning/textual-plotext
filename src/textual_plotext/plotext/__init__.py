"""Wrapper module for the main Plotext module.

Re-exports the public plotext symbols needed by the Plot class.
"""

from plotext import (
    add_theme,
    colorize,
    platform,
    sin,
    square,
    uncolorize,
)

__all__ = [
    "add_theme",
    "colorize",
    "platform",
    "sin",
    "square",
    "uncolorize",
]
