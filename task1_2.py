"""Данный код является калькулятором"""


def calc():
    """Внутри функции задаем два числовых аргумета и аргумент, обозначающий арифметический знак.
    Ноль используется в качестве выхода из калькулятора. Если введено неккоректное значение,
    калькулятор просит исправить его.
    """
    oper = input("Введите операцию (+, -, *, / или 0 для выхода): ")

    if oper == "0":
        oper_var = "0"
        print(f"Вы нажали {oper_var}, выход из калькулятора")

    else:
        if oper in "+-*/":
            try:
                num1 = int(input("Введите первое число: "))
                num2 = int(input("Введите второе число: "))

                if oper == "+":
                    summ = num1 + num2
                    print(f"Ответ: {summ}")
                    return calc()

                elif oper == "-":
                    minn = num1 - num2
                    print(f"Ответ: {minn}")
                    return calc()

                elif oper == "*":
                    mul = num1 * num2
                    print(f"Ответ: {mul}")
                    return calc()

                elif oper == "/":
                    try:
                        div = num1 / num2
                        print(f"Ответ: {div}")
                        return calc()

                    except ZeroDivisionError:
                        print("На ноль делить нельзя!")
                        return calc()

            except ValueError:
                print("Вы ввели неподерживаемое значение")
                return calc()

        else:
            print("Вы ввели неверное значение. Введите '+', '-', '*', '/', число или '0' для выхода")
            return calc()
calc()
