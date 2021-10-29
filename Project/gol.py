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

import code_base as cb

__version__ = '1.0'
__desc__ = "A simplified implementation of Conway's Game of Life."

RESOURCES = Path(__file__).parent / "../_Resources/"


# -----------------------------------------
# IMPLEMENTATIONS FOR HIGHER GRADES, C - B
# -----------------------------------------

def load_seed_from_file(_file_name: str) -> tuple:
    """ Load population seed from file. Returns tuple: population (dict) and world_size (tuple). """

    # If .json suffix is not in provided filename, add it via f'string.
    if '.json' not in _file_name:
        seed_file = f'{_file_name}.json'
    else:
        seed_file = _file_name

    #  Create a filepath and open it in readmode. Load the json content and name the dictionary to seeds.
    file_path = RESOURCES / seed_file
    with open(file_path, 'r') as file:
        seeds = json.load(file)

    # Create an empty dictionary to store the population from seeds.
    pop = {}

    # In seeds dictionary, the coordinates in "population" are tuples inside a string. For each coordinate,
    # mask out the tuple from the string and name the tuple-coordinate to cell. Map the coordinate to population
    # dictionary.
    for key in seeds["population"]:
        cell = literal_eval(key)
        pop[cell] = {}

        # If the original coordinates are rimcells, add the rimcells to new dictionary.
        if seeds["population"][key] is None:
            pop[cell] = None
            continue

        # The state for the coordinate in original dictionary shall be the same in pop dictionary.
        status = seeds["population"][key]["state"]
        pop[cell]["state"] = status

        # The neighbours in original dictionary shall be the same in pop dictionary. The neighbours are in
        # 'list' format, so they need to be converted to tuples through a loop.
        nbrs = seeds["population"][key]["neighbours"]
        neighbours = [tuple(nbr) for nbr in nbrs]
        pop[cell]["neighbours"] = neighbours

    # The world size in seeds dictionary is in a 'list' format, and needs to be converted to tuple.
    world_size = tuple(seeds["world_size"])

    # Dictionary and world_size are now converted to correct format. Return the items as tuple.
    return pop, world_size


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

    # Replace the x in the string and split the elements in order to validate them.
    size = _arg.replace("x", " ")
    size = size.split()

    try:
        # If the string has two items, convert them to integers in a tuple. If not, raise error.
        if len(size) == 2:
            size = tuple([int(i) for i in size])
        else:
            raise AssertionError("World size should contain width and height, separated by ‘x’. Ex: ‘80x40’")

        # If the input passed len(size) == 2 and converting to int, check if the int's are larger than 1.
        if any(i < 1 for i in size):
            raise ValueError("Both width and height needs to have positive values above zero.")

    # Print errors if occurred and set size back to default values.
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

    # For each coordinate in rows and columns create an inner dictionary for each cell with values. The coordinates are
    # in format y, x instead of x, y. In code_base the coordinates are [1], [0] instead of [0], [1] - hence my
    # decision to do the assignment in same format.
    for y, x in itertools.product(range(columns), range(rows)):
        cell = {}

        # If rim-cell, set value to None
        if y == 0 or y == columns - 1 or x == 0 or x == rows - 1:
            population[(y, x)] = None
            continue

        # Determine cell_state for alive & dead cells, either by randomization or based on _seed_pattern from codebase.
        if _seed_pattern is not None:
            if (y, x) in pattern:
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
        cell['neighbours'] = calc_neighbour_positions((y, x))
        population[(y, x)] = cell

    return population


def calc_neighbour_positions(_cell_coord: tuple) -> list:
    """ Calculate neighbouring cell coordinates in all directions (cardinal + diagonal).
    Returns list of tuples. """

    # Split the tuple into coordinates, and calculate neighbours by adding or subtracting values to change position.
    y = _cell_coord[0]
    x = _cell_coord[1]

    neighbours = [(y, x - 1), (y - 1, x - 1), (y - 1, x), (y - 1, x + 1), (y, x + 1), (y + 1, x + 1), (y + 1, x),
                  (y + 1, x - 1)]

    return neighbours


def run_simulation(_nth_generation: int, _population: dict, _world_size: tuple):
    """ Runs simulation for specified amount of generations. """

    # If generation is 0, return empty space.
    if _nth_generation == 0:
        return None

    # Clear console and call population by passing through arguments to update_world and store the new generation.
    cb.clear_console()
    _population = update_world(_population, _world_size)
    sleep(0.2)

    # If it is only one generation, return initial population.
    if _nth_generation == 1:
        return _population

    # If there are more generations, continue calling run_simulation until _nth_generation is 0.
    else:
        return run_simulation(_nth_generation - 1, _population, _world_size)


def update_world(_cur_gen: dict, _world_size: tuple) -> dict:
    """ Represents a tick in the simulation. """

    # Create a new empty dictionary to store the next generation.
    next_gen = {}
    width = _world_size[0] - 1  # Width is needed for linebreak. -1 for compensating for rim-cell.

    for (y, x) in _cur_gen:

        # Create an inner dictionary for new values for next_gen
        coord = {}

        # Print out in console by calling functions in codebase.
        if _cur_gen[(y, x)] is None:
            cb.progress(cb.get_print_value(cb.STATE_RIM))

            # Break when the x is equal to width in order to achieve the desired shape of world grid.
            if x == width:
                cb.progress('\n')

            # Rim-cells should remain the same for next generation. Set value to none.
            next_gen[(y, x)] = None
            continue
        else:
            cell_state = _cur_gen[(y, x)]['state']
            cb.progress(cb.get_print_value(cell_state))

            # Retrieve neighbours and pass them to count_alive_neighbours in order to determine alive cells.
            neighbours = _cur_gen[(y, x)]['neighbours']
            alive_neighbours = count_alive_neighbours(neighbours, _cur_gen)

            # If the current cell is alive and if it has 2 or 3 alive neighbours,
            # it will remain alive in next generation. If it has more or less alive neighbours, it will die. Map the
            # states to coord.
            if _cur_gen[(y, x)]['state'] == cb.STATE_ALIVE:
                if alive_neighbours == 2:
                    coord['state'] = cb.STATE_ALIVE
                elif alive_neighbours == 3:
                    coord['state'] = cb.STATE_ALIVE
                else:
                    coord['state'] = cb.STATE_DEAD

            # If the current cell is dead but it has 3 alive neighbours, it will be alive in next generation. Else,
            # it remain dead. Map values to coord.
            elif _cur_gen[(y, x)]['state'] == cb.STATE_DEAD:
                if alive_neighbours == 3:
                    coord['state'] = cb.STATE_ALIVE
                else:
                    coord['state'] = cb.STATE_DEAD

            # Map neighbours to coord, and then map coord to the next_generation.
            coord['neighbours'] = calc_neighbour_positions((y, x))
            next_gen[(y, x)] = coord

    return next_gen


def count_alive_neighbours(_neighbours: list, _cells: dict) -> int:
    """ Determine how many of the neighbouring cells are currently alive. """

    # Define living counter
    living = 0

    # The values of neighbours can be retrieved in _cells. If value is none, it is a rim-cell and should not
    # be considered in calculation of alive neighbours, hence continue. However, if the state for neighbour is alive,
    # increment living counter and return it.
    for (y, x) in _neighbours:
        rim_cell = _cells[(y, x)] is None
        if rim_cell:
            continue

        alive_cell = _cells[(y, x)]['state'] is cb.STATE_ALIVE
        if alive_cell:
            living = living + 1

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
