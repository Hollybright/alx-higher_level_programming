
def replace_in_list(my_list, idx, element):
    my_list_len = len(my_list)
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list

