#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:

        rest = fct(*args)
        return rest

    except Exception as s:
        print("Exception: {}".format(s), file=sys.stderr)
        return None
