#!/usr/bin/python3 
def divisible_by_2(my_list=[]):
    listt = []
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            listt.append(True)
        else:
            listt.append(False)
    return listt
