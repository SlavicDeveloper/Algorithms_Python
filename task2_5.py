from collections import defaultdict


def sum_sixteen(num1=input(), num2=input()):
    num1_list = []
    num2_list = []
    [num1_list.append(int(el, 16)) for el in num1]
    [num2_list.append(int(el, 16)) for el in num2]
    if len(num1_list) < len(num2_list):
        num1_list.insert(0, 0)
        nums_dict = dict()
        nums_dict["num1_1"] = num1_list
        nums_dict["num2_2"] = num2_list
        sum_nums = [x+y for x,y in zip(nums_dict["num1_1"], nums_dict["num2_2"])]
        for el in sum_nums:
            el += el
            print(hex(el))
    elif len(num2_list) < len(num1_list):
        num2_list.insert(0, 0)
        nums_dict = dict()
        nums_dict["num1_1"] = num1_list
        nums_dict["num2_2"] = num2_list
        sum_nums = [x + y for x, y in zip(nums_dict["num1_1"], nums_dict["num2_2"])]
        for el in sum_nums:
            el += el
            print(hex(el))


sum_sixteen()
