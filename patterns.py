"""
Predefined and utility Game of Life patterns.
"""

import random
from typing import List, Tuple

Cell = Tuple[int, int]


def glider(offset_row: int = 0, offset_col: int = 0) -> List[Cell]:
    """
    Classic glider pattern.
    """
    base = [
        (1, 2),
        (2, 3),
        (3, 1),
        (3, 2),
        (3, 3),
    ]
    return [(r + offset_row, c + offset_col) for r, c in base]


def random_cells(rows: int, cols: int, density: float = 0.2) -> List[Cell]:
    """
    Generate a random set of live cells.

    Args:
        rows: Grid rows.
        cols: Grid columns.
        density: Approximate fraction of cells that start alive (0.0–1.0).
    """
    cells: List[Cell] = []
    for r in range(rows):
        for c in range(cols):
            if random.random() < density:
                cells.append((r, c))
    return cells

