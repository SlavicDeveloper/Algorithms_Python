"""Код, представляющий из себя рекурсию"""

from memory_profiler import profile

rand_list = []


# Неоптимизированная рекурсия (инкремент повышается на 0.1 MiB)
@profile
def grow(i, j):
    """Функция, рекурсивно добавляет j в список"""
    if i == 5:
        return "Конец"
    else:
        for el in range(1, 1000):
            rand_list.append(j)
        return grow(i + 1, j)


grow(0, 0)



"""Код, представляющий из себя рекурсию"""

from memory_profiler import profile

rand_list_2 = []


# Оптимизированный вариант при помощи использования оберточной функции
# Здесь не происходит повышение инкремента
@profile
def func():
    """Функция, рекурсивно добавляет j в список"""

    def grow(i=0, j=0):
        if i == 5:
            return "Конец"
        else:
            for el in range(1, 1000):
                rand_list_2.append(j)
            return grow(i + 1, j)


func()