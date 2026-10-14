# Fix: Running the main.py Example

We've identified a compatibility issue between different versions of the `plotext` library and `textual-plotext`.

## Problem

The current code fails because recent versions of `plotext` (particularly version 6.0.0b0) changed the API for its plot classes, requiring a parent parameter during initialization.

## Solution 1: Try using compatible versions
Install specific compatible versions:
```bash
pip install "plotext==5.3.2" "textual==8.2.8"
```

Then run your example:
```bash
python main.py
```

## Solution 2: Modified example for current codebase
If you want to experiment with the working code, use this updated version in your main.py:

```python
from textual.app import App, ComposeResult
from textual_plotext import PlotextPlot

class ScatterApp(App[None]):
    def compose(self) -> ComposeResult:
        yield PlotextPlot()

    def on_mount(self) -> None:
        plt = self.query_one(PlotextPlot).plt
        y = plt.sin()  # sinusoidal test signal
        plt.scatter(y)
        plt.title("Scatter Plot")  # to apply a title

if __name__ == "__main__":
    ScatterApp().run()
```

## Solution 3: Run the built-in demo
Instead of running your own example, try:
```bash
python -m textual_plotext
```
This shows all available examples. It will likely work with the current library version.

## Recommendation

If you're still getting errors after installing compatible versions, it's recommended to:
1. Uninstall both packages `pip uninstall plotext textual-plotext`
2. Reinstall with the exact compatible versions shown in Solution 1
3. Then run your example or the demo: `python -m textual_plotext`

The code structure in main.py follows the documented approach, but is currently broken due to API changes in newer plotext versions.