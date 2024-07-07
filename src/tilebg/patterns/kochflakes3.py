"""Parameters for a background image of randomly colored Koch islands."""

__author__ = "ccornix"
__copyright__ = "Copyright (c) 2024 ccornix"
__license__ = "MIT"

from sympy import Rational, pi, sqrt
from typing import Any

from ..lib.koch import koch_island
from ..lib.grid import (
    generate_grid,
    make_odd_row_shift_offsets_fn,
    make_random_fill_classes_fn,
)
from ..lib.path import scale, shift, rotate


def parameters() -> dict[str, Any]:
    isle = koch_island(iterations=3)
    resolution = 1920, 1080
    cell_width, cell_height = 64, 72
    spacings = (2 * cell_width, cell_height // 2)
    offsets_fn = make_odd_row_shift_offsets_fn(cell_width)

    big_isle = scale(isle, (cell_width / sqrt(3), cell_height // 2))
    big_element_paths = [big_isle]
    big_classes_fn = make_random_fill_classes_fn(fill_count=3)

    small_isles = scale(
        rotate(isle, pi / 6),
        (Rational(1, 3) * cell_width, Rational(1, 2) / sqrt(3) * cell_height),
    )
    small_element_paths = [
        shift(small_isles, (-cell_width * Rational(2, 3), 0)),
        shift(small_isles, (cell_width * Rational(2, 3), 0)),
    ]
    small_classes_fn = make_random_fill_classes_fn(
        fill_count=3, element_count=2
    )

    return dict(
        author=__author__,
        title="Randomly colored Koch islands",
        resolution=resolution,
        paths=(
            generate_grid(
                element_paths=big_element_paths,
                spacings=spacings,
                resolution=resolution,
                offsets_fn=offsets_fn,
                classes_fn=big_classes_fn,
            )
            + generate_grid(
                element_paths=small_element_paths,
                spacings=spacings,
                resolution=resolution,
                offsets_fn=offsets_fn,
                classes_fn=small_classes_fn,
            )
        ),
    )
