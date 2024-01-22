#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        print_out = a / b

    except (FloatingPointError, ZeroDivisionError):
        print_out = None

    finally:
        print("Inside result: {}".format(print_out))

    return print_out
