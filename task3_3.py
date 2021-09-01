"""Код предназначен для поиска уникальных подстрок"""

hash_list = []


def count_sub(inp_string="papa"):
    """Функция собирает возможные подстроки из строки в аргументах функции"""
    for el1 in range(len(inp_string)):
        for el2 in range(el1 + 1, len(inp_string)):
            to_hash_list = hash(inp_string[el1:el2])
            hash_list.append(to_hash_list)


def reversed_count_sub(inp_string="papa"):
    """Функция собирает возможные подстроки из реверсивной строки в аргументах функции"""
    rev_str = ''.join(reversed(inp_string))
    for el1 in range(len(rev_str)):
        for el2 in range(el1 + 1, len(rev_str)):
            to_hash_list = hash(rev_str[el1:el2])
            hash_list.append(to_hash_list)


def check():
    """Функция удаляет повторы из списка"""
    list_chk = list(set(hash_list))
    return len(list_chk)


count_sub()
reversed_count_sub()
print(check())
