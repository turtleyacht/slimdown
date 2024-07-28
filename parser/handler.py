# Think we'll need classes to store runtime state
line_count = 0

# Called by reader with the line read.
def on_line(line):
    # print(line_count)  # line_count referenced before assignment
    print("Received a line. The line was:")
    print(line)
    # line_count = line_count + 1
