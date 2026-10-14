"""Wrapper module for the Plotext plot_class.

In plotext 6+ the figure class is plotext._plotter.plot.plot_class.
This module re-exports it for backward compatibility.
"""

from plotext._plotter.plot import plot_class as _figure_class

__all__ = ["_figure_class"]
