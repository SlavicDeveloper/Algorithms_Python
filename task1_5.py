"""Определение компаний с прибылью выше/ниже среднего"""

from collections import namedtuple

i = 1
j = 1

income = []
comp_list = []
comp_amount = int(input("Введите количество компаний: "))
while i <= 2:
    comp_name = (input("Введите название компании: "))
    i += 1
    while j <= 4:
        comp_in_data = income.append(int(input(f"Введите прибыль компании за {j} квартал: ")))
        j += 1
    j = 1
    one_comp_income = sum(income)
    comp_tuple = namedtuple("companies", ["comp_name_info", 'comp_income'])
    all_comp_income = comp_tuple(
        comp_name_info=comp_name,
        comp_income=one_comp_income
        )

    comp_list.append(all_comp_income._asdict())

av_income = sum(income) / len(income)

for el in comp_list:
    if el['comp_income'] < av_income:
        print(f"Компания с прибылью ниже среднего {el['comp_name_info']}")
    elif el['comp_income'] > av_income:
        print(f"Компания с прибылью выше среднего {el['comp_name_info']}")
