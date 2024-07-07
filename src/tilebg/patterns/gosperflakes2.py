"""Parameters for a background image of randomly colored Gosper islands."""

__author__ = "ccornix"
__copyright__ = "Copyright (c) 2024 ccornix"
__license__ = "MIT"

from sympy import sqrt
from typing import Any

from ..lib.gosper import gosper_island
from ..lib.grid import (
    generate_grid,
    make_odd_row_shift_offsets_fn,
    make_random_fill_classes_fn,
)
from ..lib.path import scale


def parameters() -> dict[str, Any]:
    isle = gosper_island(iterations=2)
    resolution = 1920, 1080
    cell_width, cell_height = 32, 36
    element_paths = [scale(isle, (cell_width / sqrt(3), cell_height // 2))]
    spacings = (cell_width, 3 * cell_height // 4)

    return dict(
        author=__author__,
        title="Randomly colored Gosper islands",
        resolution=resolution,
        paths=generate_grid(
            element_paths=element_paths,
            spacings=spacings,
            resolution=resolution,
            offsets_fn=make_odd_row_shift_offsets_fn(cell_width // 2),
            classes_fn=make_random_fill_classes_fn(fill_count=3),
        ),
    )
