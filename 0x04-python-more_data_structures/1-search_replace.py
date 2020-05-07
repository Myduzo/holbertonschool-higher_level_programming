#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if idx == search else idx for idx in my_list]
