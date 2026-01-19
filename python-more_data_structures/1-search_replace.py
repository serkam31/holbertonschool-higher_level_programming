#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if i == search:
            new_list.append(replace)
            pass
        else:
            new_list.append(i)
            pass
    return new_list
#return [replace if x == search else x for x in my_list]