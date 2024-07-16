"""Generator of a seamless grid of path tiles."""

__author__ = "ccornix"
__copyright__ = "Copyright (C) 2024 ccornix"
__license__ = "MIT"
__all__ = [
    "generate_grid",
    "make_odd_row_shift_offsets_fn",
    "make_random_fill_svg_class_fn",
]

from collections.abc import Callable, Sequence
from random import randrange
from sympy import Matrix
from typing import cast
import operator

from .path import TNum, shift
from .svg import SVGPath


def generate_grid(
    *,
    element_path: Sequence[Matrix],
    spacings: tuple[int, int],
    resolution: tuple[int, int],
    offsets_fn: Callable[[int, int], tuple[TNum, TNum]] | None,
    svg_class_fn: Callable[[int, int], list[str]],
) -> list[SVGPath]:
    """Generate a whole grid of SVG paths.

    The path for a single element in the grid is passed through `element_path`,
    which is then cloned and layed out with given `spacings`. Function
    `offests_fn` may define an index-dependent offset, which can be used, for
    instance, to define a hexagonal grid with alternating horizontal row
    offsets. The `resolution` of the target image is used to estimate how many
    times elements needs to be repeated in the horizontal and vertical
    directions. Finally, `svg_class_fn` should yield an index-dependent SVG
    class for the path of the element.

    A list of SVG path data is returned.
    """
    dx, dy = spacings
    w, h = resolution
    assert w % dx == 0 and h % dy == 0
    Nx, Ny = w // dx, h // dy

    offsets_fn = offsets_fn or (lambda ix, iy: (0, 0))

    edge_svg_class_cache: dict[tuple[int, int], list[str]] = {}

    def wrapped_svg_class(ix: int, iy: int) -> list[str]:
        jx = ix % Nx
        jy = iy % Ny
        try:
            svg_class = edge_svg_class_cache[jx, jy]
        except KeyError:
            svg_class = svg_class_fn(jx, jy)
            if jx == 0 or jy == 0:
                edge_svg_class_cache[jx, jy] = svg_class
        return svg_class

    return [
        SVGPath(
            points=shift(
                element_path,
                # HACK: https://github.com/python/mypy/issues/7509
                cast(
                    tuple[TNum, TNum],
                    tuple(
                        map(
                            operator.add,
                            offsets_fn(ix, iy),
                            (ix * dx, iy * dy),
                        )
                    ),
                ),
            ),
            svg_class=wrapped_svg_class(ix, iy),
        )
        for iy in range(Ny + 1)
        for ix in range(Nx + 1)
    ]


def make_odd_row_shift_offsets_fn(
    shift_width: TNum,
) -> Callable[[int, int], tuple[TNum, TNum]]:
    """Make an elements offsets factory function."""
    assert shift_width > 0

    def offsets_fn(ix: int, iy: int) -> tuple[TNum, TNum]:
        """Return offsets for shifting every odd row only."""
        return shift_width * (iy % 2), 0

    return offsets_fn


def make_random_fill_svg_class_fn(
    fill_count: int
) -> Callable[[int, int], list[str]]:
    """Make an SVG class factory function for a path."""
    assert fill_count > 0

    def svg_class_fn(ix: int, iy: int) -> list[str]:
        """Return SVG path class with a randomly selected fill style."""
        return ["stroke", f"fill-{randrange(fill_count)}"]

    return svg_class_fn
