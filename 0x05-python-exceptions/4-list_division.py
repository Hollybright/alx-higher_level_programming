#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    numb = []
    tmp_bet = 0
    for x in range(0, list_length):
        try:
            tmp_bet = my_list_1[x] / my_list_2[x]
        except TypeError:
            tmp_bet = 0
            print("wrong type")
        except ZeroDivisionError:
            tmp_bet = 0
            print("division by 0")
        except IndexError:
            tmp_bett = 0
            print("out of range")
        finally:
            pass
        numb.append(tmp_bet)
    return numb
