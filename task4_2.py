"""There we check user`s account for authentication status"""

db_users = [
    ["user1", "a133bn", "disabled"],
    ["user2", "a123dn", "activated"],
    ["user3", "a423bn", "disabled"],
    ["user4", "a1230n", "activated"]
]


# Способ 1, Сложность O(n^2)

for el1 in db_users:  # O(n)
    for el2 in el1:  # O(n)
        if el2 == "activated":  # O(len(el2))
            print("Аутефикация пройдена")
        elif el2 == "disabled":  # O(len(el2))
            print("Аутефикация не пройдена")
        else:
            pass

# Способ 2 Сложность # O(n)
new_list = []  # O(len(1))

for el2 in db_users:  # O(n)
    new_el = el2.pop(2)  # O(1)
    new_list.append(new_el)  # O(1)

for el3 in new_list:  # O(n)
    if el3 == "activated":  # O(len(el3))
        print("Аутефикация пройдена")
    elif el3 == "disabled":  # O(len(el3))
        print("Аутефикация не пройдена")
    else:
        pass
