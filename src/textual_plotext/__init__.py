"""A Textual widget library for wrapping the Plotext terminal plotting library."""

from .plot import Plot, PlotextThemeName, themes
from .plotext_plot import PlotextPlot

__all__ = ["Plot", "PlotextPlot", "PlotextThemeName", "themes"]
