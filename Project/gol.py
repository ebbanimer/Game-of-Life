#!/usr/bin/env python
"""
The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells,
each of which is in one of two possible states, alive or dead (populated or unpopulated).
Every cell interacts with its eight neighbours, which are the cells that are horizontally,
vertically, or diagonally adjacent.

At each step in time, the following transitions occur:

****************************************************************************************************
   1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
   2. Any live cell with two or three live neighbours lives on to the next generation.
   3. Any live cell with more than three live neighbours dies, as if by overpopulation.
   4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
****************************************************************************************************

The initial pattern constitutes the seed of the system.

The first generation is created by applying the above rules simultaneously to every cell in the
seed—births and deaths occur simultaneously, and the discrete moment at which this happens is
sometimes called a tick. The rules continue to be applied repeatedly to create further generations.

You run this script as a module:
    python -m Project.gol.py
"""

import argparse
import random
import json
import logging
import itertools
from pathlib import Path
from ast import literal_eval
from time import sleep

import Project.code_base as cb

__version__ = '1.0'
__desc__ = "A simplified implementation of Conway's Game of Life."

RESOURCES = Path(__file__).parent / "../_Resources/"


# -----------------------------------------
# IMPLEMENTATIONS FOR HIGHER GRADES, C - B
# -----------------------------------------

def load_seed_from_file(_file_name: str) -> tuple:
    """ Load population seed from file. Returns tuple: population (dict) and world_size (tuple). """
    pass


def create_logger() -> logging.Logger:
    """ Creates a logging object to be used for reports. """
    pass


def simulation_decorator(func):
    """ Function decorator, used to run full extent of simulation. """
    pass


# -----------------------------------------
# BASE IMPLEMENTATIONS
# -----------------------------------------

def parse_world_size_arg(_arg: str) -> tuple:
    """ Parse width and height from command argument. """

    size = _arg.replace("x", " ")
    size = size.split()
    size = tuple([int(i) for i in size])

    try:
        if len(size) != 2:
            raise AssertionError("World size should contain width and height, separated by ‘x’. Ex: ‘80x40’")

        # if len(size) == 2:
        #    try:
        #        size = tuple([int(i) for i in size])
        #    except AssertionError:
        #        print("World size should contain width and height, separated by ‘x’. Ex: ‘80x40’")

        if any(i < 1 for i in size):
            raise ValueError("Both width and height needs to have positive values above zero.")

    except (AssertionError, ValueError) as e:
        print(e)
        print("Using default world size: 80x40")
        size = (80, 40)

    return size


def populate_world(_world_size: tuple, _seed_pattern: str = None) -> dict:
    """ Populate the world with cells and initial states. """

    population = {}

    # If _seed_pattern contains a value, call get_pattern function in code_base
    if _seed_pattern is not None:
        pattern = cb.get_pattern(_seed_pattern, _world_size)

    rows = _world_size[0]
    columns = _world_size[1]

    # For each coordinate in rows and columns create an inner dictionary for each cell with values.
    for x, y in itertools.product(range(rows + 1), range(columns + 1)):
        cell = {}

        # If rim-cell, set value to None
        if x == 0 or x == rows or y == 0 or y == columns:
            population[(x, y)] = None
            continue

        # Determine cell_state for alive and dead cells, either by randomization or based on _seed_pattern.
        if _seed_pattern is not None:
            if (x, y) in pattern:
                cell_state = cb.STATE_ALIVE
            else:
                cell_state = cb.STATE_DEAD
        else:
            rand = random.randint(0, 20)
            if rand <= 16:
                cell_state = cb.STATE_DEAD
            else:
                cell_state = cb.STATE_ALIVE

        # Map values to dictionary and calculate neighbours by passing the coordinates to calc_ function.
        cell['state'] = cell_state
        cell['neighbours'] = calc_neighbour_positions((x, y))
        population[(x, y)] = cell

    return population


def calc_neighbour_positions(_cell_coord: tuple) -> list:
    """ Calculate neighbouring cell coordinates in all directions (cardinal + diagonal).
    Returns list of tuples. """

    # Split the tuple into coordinates, and calculate neighbours by adding or subtracting values to change position.

    x = _cell_coord[0]
    y = _cell_coord[1]

    neighbours = [(x, y - 1), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y),
                  (x + 1, y - 1)]

    return neighbours


def run_simulation(_generations: int, _population: dict, _world_size: tuple):
    """ Runs simulation for specified amount of generations. """

    # For each iteration through given generations, clear the console and get new generation from update_world.
    for i in range(0, _generations):
        cb.clear_console()
        update_world(_population, _world_size)
        sleep(0.2)


def update_world(_cur_gen: dict, _world_size: tuple) -> dict:
    """ Represents a tick in the simulation. """
    pass

    # next_gen = {}

    for i, (x, y) in enumerate(_cur_gen, start=1):

        width = _world_size[0] - 1

        if _cur_gen[(x, y)] is None:
            cell_state = cb.STATE_RIM
            status = cb.get_print_value(cell_state)
            cb.progress(status)
            if i % width == 0:
                cb.progress('\n')
                # break
        else:
            cell_state = _cur_gen[(x, y)]['state']
            status = cb.get_print_value(cell_state)
            cb.progress(status)


    '''
    
        neighbours = calc_neighbour_positions((x, y))

        alive_cells = count_alive_neighbours(neighbours, _cur_gen)

        cell_state = _cur_gen[(x, y)]['state']

        if cell_state is cb.STATE_ALIVE:
            if alive_cells == 2 or 3:
                next_state = cb.STATE_ALIVE
                next_gen[(x, y)]['state'] = next_state
            else:
                next_state = cb.STATE_DEAD
                next_gen[(x, y)]['state'] = next_state
        elif cell_state is cb.STATE_DEAD:
            if alive_cells == 3:
                next_state = cb.STATE_ALIVE
                next_gen[(x, y)]['state'] = next_state
            else:
                next_state = cb.STATE_DEAD
                next_gen[(x, y)]['state'] = next_state
                '''

    # return next_gen


def count_alive_neighbours(_neighbours: list, _cells: dict) -> int:
    """ Determine how many of the neighbouring cells are currently alive. """

    # Define living counter
    living = 0

    # For each cell in neighbours, if cell is not rim-cell and is alive, increment living.
    for (x, y) in _neighbours:
        if (x, y) is not None and cb.STATE_ALIVE:
            living = + 1
    return living


def main():
    """ The main program execution. YOU MAY NOT MODIFY ANYTHING IN THIS FUNCTION!! """
    epilog = "DT179G Project v" + __version__
    parser = argparse.ArgumentParser(description=__desc__, epilog=epilog, add_help=True)
    parser.add_argument('-g', '--generations', dest='generations', type=int, default=50,
                        help='Amount of generations the simulation should run. Defaults to 50.')
    parser.add_argument('-s', '--seed', dest='seed', type=str,
                        help='Starting seed. If omitted, a randomized seed will be used.')
    parser.add_argument('-ws', '--worldsize', dest='worldsize', type=str, default='80x40',
                        help='Size of the world, in terms of width and height. Defaults to 80x40.')
    parser.add_argument('-f', '--file', dest='file', type=str,
                        help='Load starting seed from file.')

    args = parser.parse_args()

    try:
        if not args.file:
            raise AssertionError
        population, world_size = load_seed_from_file(args.file)
    except (AssertionError, FileNotFoundError):
        world_size = parse_world_size_arg(args.worldsize)
        population = populate_world(world_size, args.seed)

    run_simulation(args.generations, population, world_size)


if __name__ == "__main__":
    main()
