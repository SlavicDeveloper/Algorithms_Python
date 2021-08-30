"""Данный код возвращает таблицу ASCII с 32 по 127 значения"""

dict_tbl = {}


def table(i_chr=32, i=32):
    """Функция принимает 2 заранее заданных аргумента.
    i_chr выступает как счетчик, который фиксирует вход в базовый случай.
    Создается словарь, в который посредством рекурсии вносятся ключи-значения таблицы ASCII.
    При достижении базового случая словарь преобразуется в список и распаковывается.
    """
    if i_chr == 128:
        items_list = list(dict_tbl.items())
        start = 0
        end = 10
        for el in range(0, len(items_list)):
            print(*items_list[start:end])
            start += 10
            end += 10
    else:
        dict_tbl[ord(chr(i))] = chr(i)
        return table(i_chr + 1, i + 1)


table()
