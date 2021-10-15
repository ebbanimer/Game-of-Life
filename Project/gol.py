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

    #DO THE APLHA CHECK AS WELL

    size = _arg.replace("x", " ")
    size = size.split()
    size = [int(i) for i in size]

    try:
        if len(size) != 2:
            raise AssertionError("World size should contain width and height, separated by ‘x’. Ex: ‘80x40’")
        #if (i.isdigit() for i in size):
        #    raise ValueError("Both width and height needs to have positive values above zero.")
        if any(i < 1 for i in size):
            raise ValueError("Both width and height needs to have positive values above zero.")
    except (AssertionError, ValueError) as e:
        print(e)
        print("Using default world size: 80x40")
        size = (80, 40)

    #print(size)

    return size


def populate_world(_world_size: tuple, _seed_pattern: str = None) -> dict:
    """ Populate the world with cells and initial states. """

    population = {}

    if _seed_pattern is not None:
        pattern = cb.get_pattern(_seed_pattern, _world_size)

    rows = _world_size[0]
    columns = _world_size[1]

    for x, y in itertools.product(range(rows + 1), range(columns + 1)):
        cell = {}

        if x == 0 or x == rows or y == 0 or y == columns:
            population[(x, y)] = None
            continue

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

        cell['state'] = cell_state
        cell['neighbours'] = calc_neighbour_positions((x, y))
        population[(x, y)] = cell

    return population



def calc_neighbour_positions(_cell_coord: tuple) -> list:
    """ Calculate neighbouring cell coordinates in all directions (cardinal + diagonal).
    Returns list of tuples. """

    x = _cell_coord[0]
    y = _cell_coord[1]

    nbrs = [(x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1)]

    return nbrs


def run_simulation(_generations: int, _population: dict, _world_size: tuple):
    """ Runs simulation for specified amount of generations. """
    pass

    for i in range(0, _generations):
        cb.clear_console()
        update_world(_population, _world_size)             #and store new population states
        sleep(0.2)
    


def update_world(_cur_gen: dict, _world_size: tuple) -> dict:
    """ Represents a tick in the simulation. """
    pass

    #next_gen = _cur_gen.copy()

    #for (x, y) in _cur_gen:                      #line break? worldsize?
    #    cb.progress(), cb.get_print_value()      #together with state constants?
    #    count_alive_neighbours() -> next_gen     #calc next gen and store
    #return next_gen




def count_alive_neighbours(_neighbours: list, _cells: dict) -> int:
    """ Determine how many of the neighbouring cells are currently alive. """
    pass

    living = []

    populate_world()

    nbr = _cells['neighbour']

    for nbr in _neighbours:
        if nbr is not None and cb.STATE_ALIVE:
            living =+ 1
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
