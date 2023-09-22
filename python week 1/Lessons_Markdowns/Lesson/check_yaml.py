
import os
import sys
import yaml


if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        yaml.safe_load()
        file.close()
        print("YAML VALID!")
    else:
        print(sys.argv[1] + "not found")

else:
    print("Usage: check_in.py <file>")