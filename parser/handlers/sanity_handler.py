import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../emitters")

import echo_emitter as emitter

def on_line(line):
    print(__name__ + ": " + line)
    emitter.emit(line)
