'''
Write a function which takes a list of integers as input and return True if it has three 15 and two 5, and false otherwise
my_func([15, 15, 5, 15, 5, 2, 4, 6]) == True
my_func([15, 5, 15, 6]) == False
my_func([2, 3, 4, 5]) == False
'''

from typing import Dict, List


def my_func(inp: List[int]) -> bool:
    count_15 = 0
    count_5 = 0
    for i in inp:
        if int(i) == 15:
            count_15 += 1

        elif int(i) == 5:
            count_5 += 1

    if count_15 == 3 and count_5 == 2:
        return True

    else:
        return False
    
print(my_func([15, 15, 5, 15, 5, 2, 4, 6]))
print(my_func([15, 5, 15, 6]))
print(my_func([2, 3, 4, 5]))


my_dict: Dict[int, str] = {}

my_dict: Dict = dict()

