"""Замеры времени и оптимизация алгоритмов"""

from timeit import Timer


array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    """Функция вывода наиболее часто встречающегося в списке числа"""
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    """Функция вывода наиболее часто встречающегося в списке числа"""
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(func_1())
t1 = Timer("func_1()", "from __main__ import func_1")
print(t1.timeit(number=1000))

print(func_2())
t2 = Timer("func_1()", "from __main__ import func_1")
print(t2.timeit(number=1000))


def func_3():
    """Функция вывода наиболее часто встречающегося в списке числа"""
    num = max(array, key=array.count)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'




print(func_3())
t3 = Timer("func_3()", "from __main__ import func_3")
print(t3.timeit(number=1000))
