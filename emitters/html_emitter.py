import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../parser")

import strategies.by_regex as by_regex


def emit(line, info):
    # print("Previous line: " + str(info["previous_line"]))
    previous_line = str(info["previous_line"])
    if by_regex.is_command(line):
        if should_close_paragraph(line, previous_line):
            print("</p>\n")
        if should_close_list(line, previous_line):
            print("</ul>\n")
        print("<pre>\n" + line + "\n</pre>")
    elif by_regex.is_list(line):
        if should_close_paragraph(line, previous_line):
            print("</p>\n")
        if not by_regex.is_list(previous_line):
            print("<ul>\n")
        print("<li>" + line + "</li>\n")
    elif by_regex.is_paragraph(line):
        if not by_regex.is_paragraph(previous_line):
            print("<p>\n")
        if should_close_list(line, previous_line):
            print("</ul>\n")
        print("\n" + line + "\n")
    elif by_regex.is_section(line):
        if should_close_paragraph(line, previous_line):
            print("</p>\n")
        if should_close_list(line, previous_line):
            print("</ul>\n")
        print("<h2>" + line + "</h2>\n")
    elif by_regex.is_title(line):
        print("<h1>" + line + "</h1>\n")
    else:
        if should_close_paragraph(line, previous_line):
            print("</p>\n")
        if should_close_list(line, previous_line):
            print("</ul>\n")
        print("<!-- unparsed -->\n" + line + "<!-- end unparsed -->\n")


def should_close_list(line, previous_line):
    return not by_regex.is_list(line) and by_regex.is_list(previous_line)


def should_close_paragraph(line, previous_line):
    return not by_regex.is_paragraph(line) and by_regex.is_paragraph(previous_line)
