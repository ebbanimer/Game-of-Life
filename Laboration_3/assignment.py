#!/usr/bin/env python

""" DT179G - LAB ASSIGNMENT 3
You find the description for the assignment in Moodle, where each detail regarding requirements
are stated. Below you find the inherent code, some of which fully defined. You add implementation
for those functions which are needed:

 - create_logger()
 - measurements_decorator(..)
 - fibonacci_memory(..)
 - print_statistics(..)
 - write_to_file(..)
"""
import itertools
from pathlib import Path
from timeit import default_timer as timer
from functools import wraps
import argparse
import logging
import logging.config
import json

__version__ = '1.1'
__desc__ = "Program used for measuríng execution time of various Fibonacci implementations!"

RESOURCES = Path(__file__).parent / "../_Resources/"


def create_logger() -> logging.Logger:
    """Create and return logger object."""
    pass  # TODO: Replace with implementation!

    file_path = RESOURCES / 'ass3_log_conf.json'
    with open(file_path, 'r', encoding='utf-8') as file_hand:
        config = json.load(file_hand)
        logging.config.dictConfig(config)

    LOGGER = logging.getLogger('ass_3_logger')

    return LOGGER


def measurements_decorator(func):
    """Function decorator, used for time measurements."""
    @wraps(func)
    def wrapper(nth_nmb: int) -> tuple:
        pass  # TODO: Replace with implementation!

        nth_list = []
        start_time = timer()
        LOGGER.info("Starting measurements...")

        for i in range(nth_nmb, -1, -1):
            nth_val = func(i)
            nth_list.append(nth_val)

            if i % 5 == 0:
                LOGGER.debug(f'{i}: {nth_val}')

        end_time = timer()
        duration = end_time - start_time

        return duration, nth_list

    return wrapper


@measurements_decorator
def fibonacci_iterative(nth_nmb: int) -> int:
    """An iterative approach to find Fibonacci sequence value.
    YOU MAY NOT MODIFY ANYTHING IN THIS FUNCTION!!"""
    old, new = 0, 1
    if nth_nmb in (0, 1):
        return nth_nmb
    for __ in range(nth_nmb - 1):
        old, new = new, old + new
    return new


@measurements_decorator
def fibonacci_recursive(nth_nmb: int) -> int:
    """An recursive approach to find Fibonacci sequence value.
    YOU MAY NOT MODIFY ANYTHING IN THIS FUNCTION!!"""
    def fib(_n):
        return _n if _n <= 1 else fib(_n - 1) + fib(_n - 2)
    return fib(nth_nmb)


@measurements_decorator
def fibonacci_memory(nth_nmb: int) -> int:
    """An recursive approach to find Fibonacci sequence value, storing those already calculated."""
    pass  # TODO: Replace with implementation!

    memory = {0: 0, 1: 1}

    if nth_nmb in memory:
        return memory[nth_nmb]

    def fib_cal(n):
        return n if n <= 1 else \
            fib_cal(n - 1) + fib_cal(n - 2)

    num = fib_cal(nth_nmb)

    new_memory = {nth_nmb: num}
    memory.update(new_memory)
    return num


def duration_format(duration: float, precision: str) -> str:
    """Function to convert number into string. Switcher is dictionary type here.
    YOU MAY NOT MODIFY ANYTHING IN THIS FUNCTION!!"""
    switcher = {
        'Seconds': "{:.5f}".format(duration),
        'Milliseconds': "{:.5f}".format(duration * 1_000),
        'Microseconds': "{:.1f}".format(duration * 1_000_000),
        'Nanoseconds': "{:d}".format(int(duration * 1_000_000_000))
    }

    # get() method of dictionary data type returns value of passed argument if it is present in
    # dictionary otherwise second argument will be assigned as default value of passed argument
    return switcher.get(precision, "nothing")


def print_statistics(fib_details: dict, nth_value: int):
    """Function which handles printing to console."""
    line = '\n' + ("---------------" * 5)
    pass  # TODO: Replace with implementation!


    print(line)
    main_header = "\t\t\tDURATION FOR EACH APPROACH WITHIN INTERVAL: 30-0"
    print(f'{main_header}{line}')

    column_headers = "\t\t\t\t\tSeconds\t\tMilliseconds\t\tMicroseconds\t\tNanoseconds"
    print(column_headers)

    row_headers = fib_details.keys()
    row_headers = "\n".join(row_headers).title()
    print(row_headers)

    print(duration_format(0.5, 'Seconds'))
    print(duration_format(0.5, 'Milliseconds'))






def write_to_file(fib_details: dict):
    """Function to write information to file."""
    pass  # TODO: Replace with implementation!

    


def main():
    """The main program execution. YOU MAY NOT MODIFY ANYTHING IN THIS FUNCTION!!"""
    epilog = "DT179G Assignment 3 v" + __version__
    parser = argparse.ArgumentParser(description=__desc__, epilog=epilog, add_help=True)
    parser.add_argument('nth', metavar='nth', type=int, nargs='?', default=30,
                        help="nth Fibonacci sequence to find.")

    global LOGGER  # ignore warnings raised from linters, such as PyLint!
    LOGGER = create_logger()

    args = parser.parse_args()
    nth_value = args.nth  # nth value to sequence. Will fallback on default value!

    fib_details = {  # store measurement information in a dictionary
        'fib iteration': fibonacci_iterative(nth_value),
        'fib recursion': fibonacci_recursive(nth_value),
        'fib memory': fibonacci_memory(nth_value)
    }

    print_statistics(fib_details, nth_value)    # print information in console
    write_to_file(fib_details)                  # write data files


if __name__ == "__main__":
    main()
