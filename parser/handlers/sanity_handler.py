import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../emitters")

import echo_emitter as emitter


def on_line(line, line_count, processed_line_count):
    print(
        __name__
        + "("
        + str(line_count)
        + "/"
        + str(processed_line_count)
        + "): "
        + line
    )
    emitter.emit(line)
