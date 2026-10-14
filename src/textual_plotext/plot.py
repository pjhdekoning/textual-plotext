"""Provides a class that acts as a thin wrapper around Plotext.

Because plotext 6+ uses a singleton figure pattern, this class creates
independent terminal + plot_class instances so each widget has its own
plot state with no global side-effects.
"""

from __future__ import annotations

from typing import Any, Literal, TypeAlias, get_args

from plotext._kernel.terminal import terminal as _terminal_class
from plotext._plotter.plot import plot_class as _plot_class
from plotext._settings.themes import themes as _themes

from . import plotext

PlotextThemeName = Literal[
    # The standard Plotext themes.
    "clear",
    "dark",
    "default",
    "dreamland",
    "elegant",
    "girly",
    "grandpa",
    "matrix",
    "mature",
    "pro",
    "retro",
    "sahara",
    "salad",
    "scream",
    "serious",
    "windows",
    # Full colour versions of the Plotext themes.
    "textual-clear",
    "textual-dark",
    "textual-default",
    "textual-dreamland",
    "textual-elegant",
    "textual-girly",
    "textual-grandpa",
    "textual-matrix",
    "textual-mature",
    "textual-pro",
    "textual-retro",
    "textual-sahara",
    "textual-salad",
    "textual-scream",
    "textual-serious",
    "textual-windows",
]
"""Literal type that is the list of theme names defined in Plotext.

Note:
    This is a copy of the theme names and will need to be updated if Plotext
    ever adds more. The main reasons for taking this approach are:

    1. There is no public interface to access this information.
    2. Turning runtime information into type-checking data isn't simple.
"""

Color: TypeAlias = str | int | tuple[int, int, int]
"""Type of a Plotext colour."""


class Plot:
    """A class that provides a Textual-friendly interface to Plotext.

    This class wraps an independent plotext plot_class instance so each
    widget has its own plot state with no global side-effects.

    The aim of the class is to make this:

    ```python
    import plotext as plt

    plt.title("Scatter Plot")
    plt.scatter(plt.sin())
    ```

    and this:

    ```python
    plt = Plot()
    plt.title("Scatter Plot")
    plt.scatter(plt.sin())
    ```

    functionally equivalent, but with the advantage that the latter has no
    global state and is free of external side-effects.
    """

    def __init__(self) -> None:
        """Initialise an independent Plotext plot instance."""
        self._terminal = _terminal_class()
        self._plot = _plot_class(parent=self._terminal)

    @property
    def plt(self) -> Any:
        """The underlying plot_class instance."""
        return self._plot

    # ---- Data helpers delegated to the plotext module ----

    @staticmethod
    def sin(
        periods: int = 2,
        length: int = 200,
        amplitude: int = 1,
        phase: float = 0,
        decay: int = 0,
    ) -> list[float]:
        """A wrapper around `Plotext.sin`."""
        return plotext.sin(
            periods=periods,
            length=length,
            amplitude=amplitude,
            phase=phase,
            decay=decay,
        )

    @staticmethod
    def square(periods: int = 2, length: int = 200, amplitude: float = 1) -> list[int]:
        """A wrapper around `Plotext.square`."""
        return plotext.square(periods=periods, length=length, amplitude=amplitude)

    @staticmethod
    def colorize(
        string: str,
        fullground: Color | None = None,
        style: str | None = None,
        background: Color | None = None,
        show: bool = False,
    ) -> str:
        """A wrapper around `Plotext.colorize`."""
        return plotext.colorize(
            string,
            fullground=fullground,
            style=style,
            background=background,
            show=show,
        )

    @staticmethod
    def uncolorize(string: str) -> str:
        """A wrapper around `Plotext.uncolorize`."""
        return plotext.uncolorize(string)

    platform = plotext.platform
    """The platform, as recognised by Plotext.

    One of either `unix` or `windows`.
    """

    # ---- Plot configuration methods ----

    def title(self, label: str | None = None) -> None:
        """Set the plot title."""
        self.plt.title(label)

    def label(
        self,
        label: str | None = None,
        axis: int | None = None,
        side: str | int | None = None,
    ) -> None:
        """Set the label of the selected axis and side."""
        self.plt.label(label, axis=axis, side=side)

    def xlabel(self, label: str | None = None) -> None:
        """Set the x-axis label."""
        self.plt.label(label, axis=0)

    def ylabel(self, label: str | None = None) -> None:
        """Set the y-axis label."""
        self.plt.label(label, axis=1)

    def theme(self, name: str) -> None:
        """Apply a named theme."""
        self.plt.theme(name)

    def canvas(self, background: Any = None) -> None:
        """Set the canvas background color."""
        self.plt.canvas(background)

    def legend(self, active: bool = True, **kwargs: Any) -> None:
        """Configure the legend."""
        self.plt.legend(active=active, **kwargs)

    def axes(self, active: bool = True, **kwargs: Any) -> None:
        """Configure the axes."""
        self.plt.axes(active=active, **kwargs)

    # ---- Ruler methods (replace xscale, yscale, grid, ylim, xlim) ----

    def ruler(self, axis: int | None = None, side: str | int | None = None) -> Any:
        """Return the ruler selection for fine-grained control."""
        return self.plt.ruler(axis=axis, side=side)

    def xscale(self, scale: str) -> None:
        """Set the x-axis scale (e.g. 'log', 'linear')."""
        self.plt.ruler(axis=0).scale(scale)

    def yscale(self, scale: str) -> None:
        """Set the y-axis scale (e.g. 'log', 'linear')."""
        self.plt.ruler(axis=1).scale(scale)

    def xlim(self, lower: float | None = None, upper: float | None = None) -> None:
        """Set the x-axis limits."""
        self.plt.ruler(axis=0).lim(lower=lower, upper=upper)

    def ylim(self, lower: float | None = None, upper: float | None = None) -> None:
        """Set the y-axis limits."""
        self.plt.ruler(axis=1).lim(lower=lower, upper=upper)

    def grid(self, x: bool = True, y: bool = True) -> None:
        """Set grid visibility."""
        self.plt.ruler(axis=0).grid(active=x)
        self.plt.ruler(axis=1).grid(active=y)

    # ---- Date methods ----

    def date(self, axis: int | None = None, side: str | int | None = None) -> Any:
        """Return the date converter for the selected ruler."""
        return self.plt.date(axis=axis, side=side)

    def date_form(self, form: str) -> None:
        """Set the date format (legacy alias)."""
        self.plt.date().activate()

    # ---- Drawing methods ----

    def plot(self, *args: Any, **kwargs: Any) -> None:
        """Plot a line signal. Alias for line()."""
        self.line(*args, **kwargs)

    def line(self, *args: Any, **kwargs: Any) -> None:
        """Draw a line plot."""
        signal_kwargs = {}
        draw_kwargs = {}
        for k, v in kwargs.items():
            if k in ("marker", "xside", "yside"):
                signal_kwargs[k] = v
            else:
                draw_kwargs[k] = v
        signal = self.plt.signal(*args, **signal_kwargs)
        # Apply fill/line settings on the signal object
        if draw_kwargs.get("fillx"):
            signal.fillx(draw_kwargs["fillx"])
        if draw_kwargs.get("filly"):
            signal.filly(draw_kwargs["filly"])
        if draw_kwargs.get("label") is not None:
            signal.label(draw_kwargs["label"])
        if draw_kwargs.get("style") is not None:
            signal.line(style=draw_kwargs["style"])
        if draw_kwargs.get("color") is not None:
            signal.line(pixel=draw_kwargs["color"])
        self.plt.draw(signal)

    def scatter(self, *args: Any, **kwargs: Any) -> None:
        """Draw a scatter plot (line with dot marker)."""
        signal_kwargs = {}
        draw_kwargs = {}
        for k, v in kwargs.items():
            if k in ("marker", "xside", "yside"):
                signal_kwargs[k] = v
            else:
                draw_kwargs[k] = v
        signal = self.plt.signal(*args, **signal_kwargs)
        if draw_kwargs.get("label") is not None:
            signal.label(draw_kwargs["label"])
        if draw_kwargs.get("color") is not None:
            signal.line(pixel=draw_kwargs["color"])
        self.plt.draw(signal)

    def bar(self, *args: Any, **kwargs: Any) -> None:
        """Draw a bar plot."""
        self.plt.bar(*args, **kwargs)

    def multiple_bar(self, *args: Any, **kwargs: Any) -> None:
        """Draw a multiple bar plot."""
        self.plt.bar(*args, stacked=False, **kwargs)

    def stacked_bar(self, *args: Any, **kwargs: Any) -> None:
        """Draw a stacked bar plot."""
        self.plt.bar(*args, stacked=True, **kwargs)

    def hist(self, *args: Any, **kwargs: Any) -> None:
        """Draw a histogram."""
        kwargs.pop("label", None)
        self.plt.hist(*args, **kwargs)

    def error(self, *args: Any, **kwargs: Any) -> None:
        """Draw an error plot.

        Note: In plotext 6+, error bars are passed as part of the data args,
        not as xerr/yerr kwargs. This wrapper strips unsupported kwargs.
        """
        kwargs.pop("label", None)
        kwargs.pop("xerr", None)
        kwargs.pop("yerr", None)
        self.plt.error(*args, **kwargs)

    def cmatrix(self, *args: Any, **kwargs: Any) -> None:
        """Draw a confusion matrix."""
        self.plt.cmatrix(*args, **kwargs)

    def heatmap(self, *args: Any, **kwargs: Any) -> None:
        """Draw a heatmap."""
        self.plt.heatmap(*args, **kwargs)

    def box(self, *args: Any, **kwargs: Any) -> None:
        """Draw a box plot."""
        self.plt.box(*args, **kwargs)

    def candlestick(self, *args: Any, **kwargs: Any) -> None:
        """Draw a candlestick plot."""
        self.plt.candlestick(*args, **kwargs)

    # ---- Decorator methods ----

    def text(self, *args: Any, **kwargs: Any) -> None:
        """Add text to the plot."""
        self.plt.text(*args, **kwargs)

    def polygon(self, *args: Any, **kwargs: Any) -> None:
        """Draw a polygon."""
        self.plt.polygon(*args, **kwargs)

    def rectangle(self, *args: Any, **kwargs: Any) -> None:
        """Draw a rectangle."""
        self.plt.rectangle(*args, **kwargs)

    def vline(self, *args: Any, **kwargs: Any) -> None:
        """Draw a vertical line."""
        self.plt.segment(*args, **kwargs)

    def hline(self, *args: Any, **kwargs: Any) -> None:
        """Draw a horizontal line."""
        self.plt.segment(*args, **kwargs)

    # ---- Size and build ----

    def plotsize(self, width: int, height: int) -> None:
        """Set the plot size (legacy alias for _set_size)."""
        self.plt._set_size(width, height)

    def _set_size(self, width: int, height: int) -> None:
        """Set the plot size."""
        self.plt._set_size(width, height)

    def build(self) -> str:
        """Build the plot and return the ANSI string."""
        return self.plt.build().string()

    def show(self) -> None:
        """Stub function. This should never be called within Textual."""

    def save_fig(
        self, path: str | None = None, append: bool = False, keep_colors: bool = False
    ) -> None:
        """Stub function. This should not be called within Textual."""
        del path, append, keep_colors

    # ---- Data clearing ----

    def clear_data(self) -> None:
        """Clear all data from the plot."""
        self.plt.clear()

    # ---- Matrix plot (heatmap) ----

    def matrix_plot(self, data: list[list[Any]], **kwargs: Any) -> None:
        """Draw a matrix plot (heatmap)."""
        self.plt.heatmap(data, **kwargs)

    # ---- Event plot ----

    def event_plot(self, times: list[str], **kwargs: Any) -> None:
        """Draw an event plot from time strings."""
        signal = self.plt.signal(times, **kwargs)
        self.plt.draw(signal)

    # ---- Datetime helper ----

    @staticmethod
    def datetimes_to_string(datetimes: list[Any]) -> list[str]:
        """Convert datetime objects to strings."""
        return [dt.strftime("%Y-%m-%d %H:%M:%S") for dt in datetimes]


# Hoist the docstrings for the wrapper functions we've added above.
Plot.sin.__doc__ = plotext.sin.__doc__
Plot.square.__doc__ = plotext.square.__doc__
Plot.colorize.__doc__ = plotext.colorize.__doc__
Plot.uncolorize.__doc__ = plotext.uncolorize.__doc__


def themes() -> tuple[str, ...]:
    """Get the list of available theme names.

    Returns:
        A tuple of the names of the themes defined in Plotext.
    """
    return get_args(PlotextThemeName)


##############################################################################
# Here we patch in some textual-friendly themes using plotext.add_theme.

_sequence = [
    (0, 130, 200),
    (60, 180, 75),
    (230, 25, 75),
    (255, 225, 25),
    (245, 130, 48),
    (145, 30, 180),
    (70, 240, 240),
    (240, 50, 230),
    (180, 225, 40),
    (250, 190, 212),
    (0, 128, 128),
    (220, 190, 255),
    (170, 110, 40),
    (235, 230, 180),
    (128, 0, 0),
    (170, 255, 195),
    (128, 128, 0),
    (255, 215, 180),
    (0, 0, 245),
    (128, 128, 128),
]
"""A sequence of colours for multiple plots.

Designed to work with either light or dark mode.
"""

# Register full-colour versions of the Plotext themes
plotext.add_theme(
    "textual-default",
    canvas="default",
    text="default",
    sequence=_sequence,
)
plotext.add_theme(
    "textual-clear",
    canvas="default",
    text="default",
    sequence=["default"],
)

# For themes that need RGB conversion, we register them based on the
# existing plotext themes
for _theme_name in [
    "dark", "dreamland", "elegant", "girly", "grandpa",
    "matrix", "mature", "retro", "sahara", "salad",
    "scream", "serious", "windows",
]:
    if _theme_name in _themes:
        plotext.add_theme(
            f"textual-{_theme_name}",
            sequence=_sequence,
        )

# Pro is an alias for default
plotext.add_theme("textual-pro", canvas="default", text="default", sequence=_sequence)
