#!/usr/bin/python3
if __name__ == "__main__":
    import  hidden_4

    sort_list = dir(hidden_4)
    my_list = [x for x in sort_list if not x.startswith('__')]

    lists = sorted(my_list)
    for item in lists:
        print("{}".format(item))
