#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    name = 0
    for i in range(1, len(sys.argv)):
        name += int(sys.argv[i])
    print("{}".format(name))
