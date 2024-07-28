##!/usr/bin/env python

# Is this a module or a script?

import sys

print("Value of sys.argv[0] is:")
print(sys.argv[0])

print("Is my __name__ '__main__'?")
print(__name__ == "__main__")  # surprising
print("Is my __name__ 'simple_module'?")
print(__name__ == "simple_module")

# sys.argv[0] is empty when invoked with stdin or interpreter with no args
if sys.argv[0] == "simple_module.py":
    print("Invoked as a script")
elif sys.argv[0] == "-c":
    print("Implicitly invoked with -c. May need to exclude '.py' from -m arg?")
elif sys.argv[0] != "-c":
    print("simple_module.py considered a module (full name printed above)")
