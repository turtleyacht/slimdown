# wat_driver.py

import parser.handler
import parser.read_lines

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print """\
Usage: python wat_driver.py FILE\
"""
    else:
        file = sys.argv[1]
        parser.read_lines.open_and_read(file, parser.handler)
else:
    print("I was invoked as a module. What do I do?")
    exit(1)
