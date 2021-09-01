"""Функция кеширует сайты, если их нет в хеш-таблице"""

from hashlib import sha3_256
from urllib.parse import urlparse

cache = {'3353913560486fabb7acfb97c4ad20c0d2b0e08f8be1a00e91a0fd774a64c3bd':"https://gb.ru/"}


def cache_proc(url):
    """Функция кеширует сайты"""
    url_parse = urlparse(url)
    netloc_url = url_parse.netloc
    salty_hash = sha3_256(netloc_url.encode() + url.encode()).hexdigest()
    if salty_hash in cache.keys():
        print(url)
    else:
        cache[salty_hash] = url
        print("Страница успешно кэширована")


print(cache_proc("https://gb.ru/"))
