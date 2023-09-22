import json
import os
import sys

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("JSON IS VALID!")
    else:
        print(sys.argv[1] + "not found")

else:
    print("Usage: check_in.py <file>")