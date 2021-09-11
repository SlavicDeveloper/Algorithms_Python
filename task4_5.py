"""Сравнение обычного словаря и OrderedDict"""

from collections import OrderedDict
from timeit import Timer, timeit
from datetime import datetime


def dict_creation():
    """Создание словаря"""
    dict_1 = {"1": 1, "2": 2, "3": 3}


t1 = Timer("dict_creation()", "from __main__ import dict_creation")
print("t1", timeit(number=1000))


def ordered_dict_creation():
    """Создание OrderedDict"""
    ordered_dict_creation = OrderedDict([("1", 1), ("2", 2), ("3", 3)])


t2 = Timer("ordered_dict_creation()", "from __main__ import ordered_dict_creation")
print("t2", timeit(number=1000))


def dict_val():
    """Добавление элементов в словарь"""
    dict_1 = {}
    i = 0
    j = 0
    start = datetime.now()
    while i < 10000:
        dict_1[i] = j
        i += 1
        j += 1
    return datetime.now() - start


def ordered_dict_val():
    """Добавление элементов в OrderedDict"""
    ordered_dict = OrderedDict()
    i = 0
    j = 0
    start = datetime.now()
    while i < 10000:
        ordered_dict[i] = j
        i += 1
        j += 1
    return datetime.now() - start

print(dict_val())
print((ordered_dict_val()))
