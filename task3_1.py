"""Здесь необходимо найти топ-3 компании по прибыли.
Есть 2 решения
"""

db_companies = {
    "Company 1": 2500,
    "Company 2": 1000,
    "Сompany 3": 750,
    "Company 4": 500,
    "Сompany 5": 3400,
    "Company 6": 100,
}

# Способ 1. Сложность O(nlogn)
sorted_dict = sorted(db_companies.items(), key=lambda x: x[1],  reverse=True)  # O(nlogn)
print(sorted_dict[0:3:1])


# Способ 2. Сложность O(n^2)
max_val_companies = {}  # O(1)
max_val = 0  # O(1)
while len(max_val_companies) < 3:  # O(1)
    for key, value in db_companies.items():  # O(n)
        if max_val < value:  # O(1)
            max_val = value  # O(1)
            max_val_key = key  # O(1)
    max_val = db_companies.pop(max_val_key)  # O(1)
    max_val_companies.setdefault(max_val_key, max_val)  # O(1)
    max_val = 0  # O(1)

print(max_val_companies)

# Можно сделать вывод о том, что реализация по первому способу гораздо эффективнее, чем по второму способу,
# так как квадратичная сложность алгоритма превосходит линейно - логарифмическую сложность
