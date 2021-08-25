"""Проверка пользователей на статус их аутефикации"""

db_users = [
    ["user1", "a133bn", "disabled"],
    ["user2", "a123dn", "activated"],
    ["user3", "a423bn", "disabled"],
    ["user4", "a1230n", "activated"]
]

# Способ 1, Сложность O(n^2)

for el1 in db_users:  # O(n)
    for el2 in el1:  # O(n)
        if el2 == "activated":  # O(1)
            print("Аутефикация пройдена")
        elif el2 == "disabled":  # O(1)
            print("Аутефикация не пройдена")
        else:
            pass

# Способ 2 Сложность # O(n)
new_list = []  # O(len(1))

for el2 in db_users:  # O(n)
    new_el = el2.pop(2)  # O(1)
    new_list.append(new_el)  # O(1)

for el3 in new_list:  # O(n)
    if el3 == "activated":  # O(1)
        print("Аутефикация пройдена")
    elif el3 == "disabled":  # O(1)
        print("Аутефикация не пройдена")
    else:
        pass


# Способ 3 Сложность O(1)
def check_users(user_name, password, status):
    """Создаем словарь-базу с данными пользователя, при помощи if/else проверяем статус"""
    db_users_2 = {  # O(len(1))
        "user": user_name,
        "pass": password,
        "stat": status
    }
    if db_users_2["stat"] == "activated":  # O(1)
        return f"Здравствуйте, {db_users_2['user']}, Вы прошли аутефикацию"  # получение элемента О(1)
    elif db_users_2["stat"] == "disabled":  # O(1)
        return f"Здравствуйте, {db_users_2['user']}, Вы не прошли аутефикацию"  # получение элемента O(1)


print(check_users("Jack", "123", "activated"))

print(check_users("Paul", "123", "disabled"))
