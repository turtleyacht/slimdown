import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../emitters")

import html_emitter as emitter


def on_line(line, info):
    line_count = info["line_count"]
    processed_line_count = info["processed_line_count"]
    emitter.emit(line, info)
    info["previous_line"] = line
