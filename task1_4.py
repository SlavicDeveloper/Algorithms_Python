"""Использование timeit"""

from timeit import Timer


def func_1(nums):
    """Функция возврата индекса числа из другого списка при определенных условиях"""
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(func_1([1, 2, 3]))

t1 = Timer("func_1([1, 2, 3])", 'from __main__ import func_1')
print("t1", t1.timeit(number=1000))


def func_2(nums_2):
    """Функция возврата индекса числа из другого списка при определенных условиях"""
    return [j for j, k in enumerate(nums_2) if k % 2 == 0]

print(func_2([1, 2, 3]))
t2 = Timer("func_2([1, 2, 3])", 'from __main__ import func_2')
print("t2", t2.timeit(number=1000))
