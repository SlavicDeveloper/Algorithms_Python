"""Сравнение эффективность использования list и deque"""

from timeit import Timer
from collections import deque
from datetime import datetime


def list_creation():
    """Создание list"""
    simple_list = list('bcd')


t1 = Timer("list_creation()", "from __main__ import list_creation")
print("t1", t1.timeit(number=1000))


def deque_creation():
    """Создание deque"""
    simple_lst = list("bcd")
    deq_obj = deque(simple_lst)


t2 = Timer("deque_creation()", "from __main__ import deque_creation")
print("t2", t2.timeit(number=1000))


def list_insert():
    """Добавление элемента впред списка"""
    simple_list = list('bcd')
    i = 0
    start = datetime.now()
    while i < 10000:
        simple_list.insert(5, 0)
        i += 1
    return datetime.now() - start


def deque_appendleft():
    """Добавление элемента вперед deque"""
    simple_lst = list("bcd")
    deq_obj = deque(simple_lst)
    i = 0
    start = datetime.now()
    while i < 10000:
        deq_obj.appendleft(5)
        i += 1
    return datetime.now() - start


list_creation()
deque_creation()
print(list_insert())
print(deque_appendleft())
