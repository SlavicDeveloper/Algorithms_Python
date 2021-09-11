"""Код, представляющий из себя рекурсию"""

from memory_profiler import profile

rand_list = []

# Оптимизированный вариант при помощи использования оберточной функции
# Здесь не происходит повышение инкремента, в отлоичие от task6_3
@profile
def func():
    """Функция, рекурсивно добавляет j в список"""
    def grow(i=0, j=0):
        if i == 5:
            return "Конец"
        else:
            for el in range(1, 1000):
                rand_list.append(j)
            return grow(i + 1, j)

func()