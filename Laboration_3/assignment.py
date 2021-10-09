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

    file_path = RESOURCES / 'ass3_log_conf.json'                   #setting up filepath to json file to read and
    with open(file_path, 'r', encoding='utf-8') as file_hand:      #to create the logger
        config = json.load(file_hand)
        logging.config.dictConfig(config)

    LOGGER = logging.getLogger('ass_3_logger')

    return LOGGER


def measurements_decorator(func):
    """Function decorator, used for time measurements."""
    @wraps(func)
    def wrapper(nth_nmb: int) -> tuple:

        nth_list = []                                       #creating an empty list to store values
        start_time = timer()
        LOGGER.info("Starting measurements...")

        for i in range(nth_nmb, -1, -1):                    #nth_nmb being the maxnumber, counting down toward 0.
            nth_val = func(i)                               #calculating the value by calling respective function
            nth_list.append(nth_val)                        #appending the value to the empty list

            if i % 5 == 0:                                  #making sure to only log each 5th iteration in the logger
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

    memory = {0: 0, 1: 1}

    def fib_cal(n):
        return n if n <= 1 else fib_cal(n - 1) + fib_cal(n - 2)
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

    main_header = "DURATION FOR EACH APPROACH WITHIN INTERVAL: 30-0"
    print(f'{line}\n{main_header :>60}{line}')

    print(f"{'Seconds':^32}{'Milliseconds':^15}{'Microseconds':>13}{'Nanoseconds':>15}")

    for key, val in fib_details.items():                                       #for each key and value in fib_details;
                                                                               #retrieve duration from the tuple
        secs = (duration_format(fib_details[key][0], 'Seconds'))               #created in the decorator function, which
        millisecs = (duration_format(fib_details[key][0], 'Milliseconds'))     #is on position 0 in values.
        microsecs = (duration_format(fib_details[key][0], 'Microseconds'))
        nanosecs = (duration_format(fib_details[key][0], 'Nanoseconds'))


        print(f'{key.title():<20}{secs : <12}{millisecs : ^15}{microsecs: >13}{nanosecs : >15}')


def write_to_file(fib_details: dict):
    """Function to write information to file."""
    pass  # TODO: Replace with implementation!


    for key, val in fib_details.items():
        with open(f"{RESOURCES}/{key.replace(' ', '_')}.txt", "w", encoding="utf-8") as file:
            fib_values = fib_details[key][1]
            sequences = list(reversed(range(0, len(fib_values))))
            
            for i, fib_val in zip(sequences, fib_values):
                file.write(f'{i}: {fib_val}\n')



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
