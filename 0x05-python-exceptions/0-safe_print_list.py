#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    best = 0

    for b in range(0, x):
        try:
            print("{:d}".format(my_list[b]), end="")
            best += 1
        except IndexError:
            pass
    print()
    return best
