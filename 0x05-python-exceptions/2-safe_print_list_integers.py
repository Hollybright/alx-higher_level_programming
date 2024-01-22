#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    best = 0
    for x in range(0, x):
        try:

            print("{:d}".format(my_list[x]), end="")
            best += 1

        except (ValueError, TypeError):
            pass

        print()
        return best
