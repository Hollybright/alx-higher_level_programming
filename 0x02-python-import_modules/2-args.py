#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    name = len(sys.argv) #arg length
    if name == 1:
        print("{} arguments.".format(name - 1))
    elif name == 2:
        print("{} argument:".format(name - 1))
    else:
        print("{} arguments:".format(name - 1))

    for i in range(1, name):
        print("{}: {}".format(i, sys.argv[i]))
