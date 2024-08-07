# wat_driver.py

import parser.handlers.html_handler as handler
import parsers.last_line_parser

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
        parsers.last_line_parser.open_and_read(file, handler)
else:
    print("I was invoked as a module. What do I do?")
    exit(1)
