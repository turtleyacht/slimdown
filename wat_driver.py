# wat_driver.py

import parser.handlers.sanity_handler
import parsers.line_counter_parser

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print(
            """\
Usage: python wat_driver.py FILE\
"""
        )
    else:
        file = sys.argv[1]
        parsers.line_counter_parser.open_and_read(file, parser.handlers.sanity_handler)
else:
    print("I was invoked as a module. What do I do?")
    exit(1)
