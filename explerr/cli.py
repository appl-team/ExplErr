import re
import subprocess
import sys

import rich

from .exceptions import get_explanation


def main():
    args = sys.argv[1:]  # Get all arguments after 'expython'

    # Run the subprocess, capturing stdout and stderr
    result = subprocess.run(
        ["python"] + args,
        stderr=subprocess.PIPE,  # Capture stderr
        text=True,  # Decode stdout/stderr as text (str)
    )
    if result.stderr:
        rich.print(result.stderr, file=sys.stderr)  # Print errors to stderr

    pos = result.stderr.find("Traceback (most recent call last):")
    if pos != -1:
        import appl

        appl.init()  # TODO: disable logging here
        explaination = get_explanation(traceback=result.stderr[pos:])
    else:
        explaination = ""

    # Check if there were errors (exceptions or otherwise)
    if explaination:
        rich.print(explaination, file=sys.stderr)

    # Return the same exit code as the Python process
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
