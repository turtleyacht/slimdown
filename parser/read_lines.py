import sys

# Handlers must have an `on_line' function that handles
# the line "event" after it is read from the file.
def open_and_read(file, handler):
    with open(file, "r") as fp:
        for line in fp:
            handler.on_line(line)
