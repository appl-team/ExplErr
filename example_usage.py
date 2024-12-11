import argparse

import appl

from explerr.exceptions import ExceptionWithExplanation

appl.init()

parser = argparse.ArgumentParser()
parser.add_argument("--example", "-e", type=int, default=1, help="Example to run")
args = parser.parse_args()


def main():
    if args.example == 0:
        # Example 4: Using it as a try-except wrapper
        1 / 0
        # call this with `expython example_usage.py --example 0`
    elif args.example == 1:
        # Example 1: Wrapping an existing exception
        try:
            x = 1 / 0
        except ZeroDivisionError as e:
            raise ExceptionWithExplanation(e)

    elif args.example == 2:
        # Example 2: Creating a new exception
        raise ExceptionWithExplanation(message="you are not allowed to do this")

    elif args.example == 3:
        # Example 3: Using it as a try-except wrapper
        try:
            # Some code that might raise an exception
            result = some_undefined_variable + 1
        except Exception as e:
            raise ExceptionWithExplanation(e)

    elif args.example == 4:
        print("example usage")
        # Example 4: Using it as a try-except wrapper
        appl.gen()


if __name__ == "__main__":
    main()
