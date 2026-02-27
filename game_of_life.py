"""
Conway's Game of Life - thin entry point.
"""

import os
import time

from core import GameOfLife
from patterns import random_cells


def display_console(game: GameOfLife) -> None:
    """
    Console rendering for a GameOfLife instance.
    """
    os.system("cls" if os.name == "nt" else "clear")

    horizontal_border = "+" + "-" * game.cols + "+"
    print(horizontal_border)
    for row in game.grid:
        line = "|"
        for cell in row:
            line += "█" if cell == 1 else " "
        line += "|"
        print(line)
    print(horizontal_border)


def run_with_console(game: GameOfLife, generations: int, delay: float = 0.3) -> None:
    """
    Run the simulation, rendering each generation to the console.
    """
    for gen in range(generations):
        print(f"Generation {gen + 1}/{generations}")
        display_console(game)
        if gen < generations - 1:
            time.sleep(delay)
            game.next_generation()


def main() -> None:
    """
    Example entry point that runs a random initial condition.
    """
    rows, cols = 20, 40
    game = GameOfLife(rows=rows, cols=cols, initial_live_cells=random_cells(rows, cols, density=0.1))
    run_with_console(game, generations=60, delay=0.1)


if __name__ == "__main__":
    main()

