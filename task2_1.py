# Задание 2_1. Общая сложность O(n^2)
"""This is a docstring for module
There is a code which can help to search for min number
"""


def search_min_num(num_list):
    """This is a docstring for function search_min_num
    Here we find a min_num using 2 'for' loops"""
    global min_num  # O(n)
    for i in num_list:  # O(n)
        min_num = i  # O(1)
        for j in range(len(num_list)):  # O(n)
            if min_num > num_list[j]:  # O(len(num_list[j]))
                min_num = num_list[j]  # O(1)
    return min_num  # O(1)


num_list = [5, 1, 2, 0]
print(search_min_num(num_list))
