"""Код для проверки пароля пользователя"""

from uuid import uuid4
from hashlib import sha3_256

def pass_check(passwd):
    """Функция создает 'соленый хеш' пароля, а затем требует ввести пароль повторно для сравнения хешей"""
    salt = uuid4().hex
    user_salt = salt
    user_hash = sha3_256(salt.encode() + passwd.encode()).hexdigest()
    print(user_hash)
    passwd = input("Введите пароль повторно: ")
    new_hash = sha3_256(user_salt.encode() + passwd.encode()).hexdigest()
    print(new_hash)
    if user_hash == new_hash:
        return "Вы прошли авторизацию"
    else:
        return "Вы не прошли авторизацию"

print(pass_check(input("Введите пароль: ")))
