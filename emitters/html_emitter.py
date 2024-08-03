import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../parser")

import strategies.by_regex as by_regex


def emit(line):
    if by_regex.is_command(line):
        print("<pre>\n" + line + "\n</pre>")
    elif by_regex.is_list(line):
        print("<li>" + line + </li>\n")
    elif by_regex.is_paragraph(line):
        print("<p>\n" + line + "</p>\n")
    elif by_regex.is_section(line):
        print("<h2>" + line + "</h2>\n")
    elif by_regex.is_title(line):
        print("<h1>" + line + "</h1>\n")
    else:
        print("<!-- unparsed -->\n" + line + "<!-- end unparsed -->\n")
