# Seamless geometric desktop background generator

SVG generator to obtain a seamless geometric desktop backgrounds with each tile having a pseudo-random fill color selected from a predefined set. The line style and fill colors are defined in an embedded CSS that can be overridden by a custom style sheet to re-color the background image.

## Setup

### Using Nix

Clone this repository using `git` and enter the repository directory.

When using the [Nix](https://www.nixos.org) package manager, a development shell can be started using stable Nix as

```sh
nix-shell
```

while using Flakes-enabled Nix as

```sh
nix develop
```

### Manual installation into a virtual environment using `pip` (Linux)

Clone this repository using `git` and enter the repository directory.

Create a virtual environment, activate it, and install the package as

```sh
python -m venv env
. env/bin/activate
pip install .
```

Note that `python` might be invoked differently, depending on the Linux
distribution, e.g. as `python3` or `python312`.

For an editable installation with development dependencies, run

```sh
pip install -e .[devel]
```

instead.


## Usage

### SVG generation

To generate one of the SVGs, for instance, `hexagonal`, run the following
command:

```sh
python -m tilebg hexagonal > bg.svg
```

### Rendering to PNG

To render the resulting SVG to a PNG file, one can, for instance, use the
command-line application `rsvg-convert` of `librsvg`. It also supports
overriding the embedded CSS by a custom CSS file.

Consider we have the following color overrides, contained in `style.css`:

```css
.stroke { stroke:#000000 !important; }
.fill-0 { fill:#202020 !important; }
.fill-1 { fill:#404040 !important; }
.fill-2 { fill:#606060 !important; }
```

To render the SVG in 4K resolution and using our custom colors, we then run `rsvg-convert` as

```sh
rsvg-convert -a -w 3840 --stylesheet=style.css bg.svg > bg.png
```


## Gallery

### Tilings of the plane using randomly colored islands

#### `hexagons`

<a href="resources/hexagons.svg">
  <img src="resources/hexagons.svg" width="960">
</a>

#### `gosperflakes2`

[Gosper islands](https://mathworld.wolfram.com/GosperIsland.html) (2 iterations)

<a href="resources/gosperflakes2.svg">
  <img src="resources/gosperflakes2.svg" width="960">
</a>

#### `minkowskiflakes4`

[Minkowski islands](https://mathworld.wolfram.com/MinkowskiSausage.html) (4 iterations)

<a href="resources/minkowskiflakes4.svg">
  <img src="resources/minkowskiflakes4.svg" width="960">
</a>


## References

The randomly colored hexagonal grid pattern was inspired by [paepaestockphoto's artwork](https://www.vecteezy.com/vector-art/6941002-small-hexagon-shape-with-light-white-and-grey-color-seamless-pattern-background).
