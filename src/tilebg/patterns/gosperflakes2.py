"""Parameters for a background image of randomly colored Gosper islands."""

__author__ = "ccornix"
__copyright__ = "Copyright (c) 2024 ccornix"
__license__ = "MIT"

from sympy import sqrt
from typing import Any

from ..gosper import gosper_island
from ..grid import (
    generate_grid,
    make_odd_row_shift_offsets_fn,
    make_random_fill_svg_class_fn,
)
from ..path import scale


def parameters() -> dict[str, Any]:
    isle = gosper_island(iterations=2)
    resolution = 1920, 1200
    cell_width, cell_height = 30, 32
    element_path = scale(isle, (cell_width / sqrt(3), cell_height // 2))
    spacings = (cell_width, 3 * cell_height // 4)

    return dict(
        author=__author__,
        title="Randomly colored Gosper islands",
        resolution=resolution,
        paths=generate_grid(
            element_path=element_path,
            spacings=spacings,
            resolution=resolution,
            offsets_fn=make_odd_row_shift_offsets_fn(cell_width // 2),
            svg_class_fn=make_random_fill_svg_class_fn(fill_count=3),
        ),
    )
