"""Код, направленный на поиск лучшего способа хранения строковых данных"""
from memory_profiler import profile

# Вариант с использованием обычных строк (появляется инкремент 0.3 MiB (19.6 MiB))
@profile
def ordinary_str(el3, el4):
    """Используем обычные строки"""
    obj2 = (el3 + "+" + el4 + "+" + el3 + "+" + el4)
    return obj2


ordinary_str("rrr" * 10000, "ttt" * 10000)
