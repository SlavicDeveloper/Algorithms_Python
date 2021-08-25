# Задание 2_2. Общая сложность O(n)
"""This is a docstring for module
There is a code which can help to search for min number
"""


def search_min_num(num_list):
    """There we use an average value to find min number"""
    avg = 0  # O(1)
    min_avg = 0  # O(1)
    min_avg_lst = []  # O(len(1))
    for el_1 in num_list:  # O(n)
        avg += el_1  # O(1)
    avg = avg / len(num_list)  # O(1)

    for el_1 in num_list:  # O(n)
        if el_1 < avg:  # O(len(el))
            min_avg += el_1  # O(1)
            min_avg_lst.append(el_1)  # O(1)
            min_avg_lst_len = len(min_avg_lst)  # O(1)
    min_avg = min_avg / min_avg_lst_len  # O(1)

    for el_1 in num_list:  # O(n)
        if el_1 < min_avg:  # O(len(el))
            min_val = el_1  # O(1)
    return min_val  # O(1)


num_list = [5, 1, 2, 6, 2]
print(search_min_num(num_list))
