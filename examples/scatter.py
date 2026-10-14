"""A small self-contained example of a Plotext plot in a Textual app."""

from __future__ import annotations

from textual.app import App, ComposeResult

from textual_plotext import PlotextPlot


class ScatterPlot(PlotextPlot):
    """A simple scatter plot widget."""

    def on_mount(self) -> None:
        """Set up the plot."""
        self.plt.scatter(self.plt.sin())
        self.plt.title("Scatter Plot")


class ScatterApp(App[None]):
    """Example Textual application showing a Plotext plot."""

    BINDINGS = [  # type: ignore[assignment] # noqa: RUF012
        ("[", "previous_theme", "Previous theme"),
        ("]", "next_theme", "Next theme"),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.theme_names = [
            theme for theme in self.available_themes if theme != "textual-ansi"
        ]

    def compose(self) -> ComposeResult:
        """Compose the plotting widget."""
        yield ScatterPlot()

    def replot(self) -> None:
        """Re-plot the scatter data."""
        plot = self.query_one(ScatterPlot)
        plot.plt.clear_data()
        plot.plt.scatter(plot.plt.sin())
        plot.refresh()

    def action_next_theme(self) -> None:
        themes = self.theme_names
        index = themes.index(self.current_theme.name)
        self.theme = themes[(index + 1) % len(themes)]
        self.notify_new_theme(self.current_theme.name)

    def action_previous_theme(self) -> None:
        themes = self.theme_names
        index = themes.index(self.current_theme.name)
        self.theme = themes[(index - 1) % len(themes)]
        self.notify_new_theme(self.current_theme.name)

    def notify_new_theme(self, theme_name: str) -> None:
        self.clear_notifications()
        self.notify(
            title="Theme updated",
            message=f"Theme is {theme_name}.",
        )


if __name__ == "__main__":
    ScatterApp().run()
