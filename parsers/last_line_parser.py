import sys


# Handlers must have an `on_line' function that handles
# the line "event" after it is read from the file.
def open_and_read(file, handler):
    info = {}
    info["line_count"] = 0
    info["processed_line_count"] = 0
    with open(file, "r") as fp:
        for line in fp:
            info["line_count"] = info["line_count"] + 1
            handler.on_line(line, info)
            info["processed_line_count"] = info["processed_line_count"] + 1
            # you don't print the last processed line count!
