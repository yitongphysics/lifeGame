"""
Core Game of Life engine (no I/O or patterns).
"""

from typing import Iterable, List, Tuple


Cell = Tuple[int, int]


class GameOfLife:
    """
    Conway's Game of Life on a 2D rectangular grid.
    """

    def __init__(self, rows: int, cols: int, initial_live_cells: Iterable[Cell] | None = None) -> None:
        """
        Initialize the grid.

        Args:
            rows: Number of rows in the grid.
            cols: Number of columns in the grid.
            initial_live_cells: Optional iterable of (row, col) positions that start alive.
        """
        self.rows = rows
        self.cols = cols
        self.grid: List[List[int]] = [[0 for _ in range(cols)] for _ in range(rows)]

        if initial_live_cells is not None:
            for r, c in initial_live_cells:
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    self.grid[r][c] = 1

    def count_neighbors(self, row: int, col: int) -> int:
        """
        Count the number of live neighbors around the cell at (row, col).
        Uses periodic boundary conditions (toroidal grid), so neighbors
        wrap around edges.
        """
        count = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr = (row + dr) % self.rows
                nc = (col + dc) % self.cols
                count += self.grid[nr][nc]
        return count

    def next_generation(self) -> None:
        """
        Compute the next generation according to Conway's rules:
        - Any live cell with 2 or 3 live neighbors survives.
        - Any dead cell with exactly 3 live neighbors becomes a live cell.
        - All other live cells die in the next generation; all other dead cells stay dead.
        """
        new_grid: List[List[int]] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                neighbors = self.count_neighbors(r, c)
                alive = self.grid[r][c] == 1

                if alive and neighbors in (2, 3):
                    new_grid[r][c] = 1
                elif not alive and neighbors == 3:
                    new_grid[r][c] = 1
                else:
                    new_grid[r][c] = 0

        self.grid = new_grid

