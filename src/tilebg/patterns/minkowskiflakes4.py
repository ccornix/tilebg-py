"""Parameters for a background image of randomly colored Minkowski islands."""

__author__ = "ccornix"
__copyright__ = "Copyright (c) 2024 ccornix"
__license__ = "MIT"

from typing import Any

from ..lib.minkowski import minkowski_island
from ..lib.grid import (
    generate_grid,
    make_odd_row_shift_offsets_fn,
    make_random_fill_classes_fn,
)
from ..lib.path import scale


def parameters() -> dict[str, Any]:
    isle = minkowski_island(iterations=4)
    resolution = 1920, 1080
    cell_width, cell_height = 120, 120
    element_paths = [scale(isle, (cell_width // 2, cell_height // 2))]
    spacings = (cell_width, cell_height // 2)

    return dict(
        author=__author__,
        title="Randomly colored Minkowski islands",
        resolution=resolution,
        paths=generate_grid(
            element_paths=element_paths,
            spacings=spacings,
            resolution=resolution,
            offsets_fn=make_odd_row_shift_offsets_fn(cell_width // 2),
            classes_fn=make_random_fill_classes_fn(fill_count=3),
        ),
    )
