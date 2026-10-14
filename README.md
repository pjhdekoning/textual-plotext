# textual-plotext

![PlotextPlot in action](https://raw.githubusercontent.com/Textualize/textual-plotext/main/textual-plotext-example.png)

A Textual widget wrapper for the [Plotext plotting
library](https://github.com/piccolomo/plotext).

## Introduction

The library makes one widget available: `PlotextPlot`. This widget provides
a `plt` property, which should be used where you would normally use `plt` as
seen in the Plotext documentation.

Let's take [the first
example](https://github.com/piccolomo/plotext/blob/master/readme/basic.md#scatter-plot)
from [the Plotext README](https://github.com/piccolomo/plotext#readme):

```python
import plotext as plt
y = plt.sin() # sinusoidal test signal
plt.scatter(y)
plt.title("Scatter Plot") # to apply a title
plt.show() # to finally plot
```

The Textual equivalent of this (including everything needed to make this a
fully-working Textual application) is:

```python
from textual.app import App, ComposeResult

from textual_plotext import PlotextPlot

class ScatterApp(App[None]):

    def compose(self) -> ComposeResult:
        yield PlotextPlot()

    def on_mount(self) -> None:
        plt = self.query_one(PlotextPlot).plt
        y = plt.sin() # sinusoidal test signal
        plt.scatter(y)
        plt.title("Scatter Plot") # to apply a title

if __name__ == "__main__":
    ScatterApp().run()
```

The main differences to note are:

- We're not directly importing `plotext`.
- We use `PlotextPlot.plt` rather than `plt`.
- We don't call Plotext's `show` method, `PlotextPlot` takes care of this.

## Installation

The library can be installed from PyPi:

```sh
$ pip install textual-plotext
```

Once installed you can quickly test the library by running the demo:

```sh
$ python -m textual_plotext
```

The demo app includes many of the examples shown in the Plotext README.

## Version Compatibility

If you encounter issues running examples, it's likely due to version compatibility between different releases of plotext. The library currently works best with:

- `plotext==5.3.2` 
- `textual==8.2.8`

To install compatible versions:
```sh
pip uninstall plotext textual-plotext
pip install "plotext==5.3.2" "textual==8.2.8"
```

Then try running the demo:
```sh
python -m textual_plotext
```

Or run your own example with: 
```sh
python main.py
```

## Troubleshooting

If you still get errors about plotext._dict import issues, that is likely because your system has conflicting versions of `plotext` installed. The recommended approach is to use a clean Python environment with specified compatible versions.

The code structure in the example matches exactly what the README describes and should work properly when correctly versioned.