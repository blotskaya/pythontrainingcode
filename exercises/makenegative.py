#Функция принимает число и делает его отрицательным. Ноль не имеет какого-либо математического знака
#Если число отрицательное, тогда никаких действий не требуется
#Пример:
#Input: 1 Output: -1
#Input: -5 Output: -5

from typing import Union, List

def make_negative(num: Union[int, float]) -> Union[int, float]:
    """Решение для задачки, когда подается 1 число
    алгоритмическая сложность
    проверка типа числа: O(1)
    проверка знака числа: O(1)
    умножение числа на -1: O(1)
    всего: O(1) + O(1) + O(1)"""
    if not isinstance(num, int|float):
        return "num should be integer or float"
    else:
        if num > 0:
            return num*(-1)
        else:
            return num

#положительное число - преобразовано в отрицательное
assert make_negative(4) == -4, f"Expected: -4, got: {make_negative(4)}"
#отрицательное число - без изменений
assert make_negative(-77) == -77, f"Expected: -77, got: {make_negative(-77)}"
#ноль - без изменений
assert make_negative(0) == 0, f"Expected: 0, got: {make_negative(0)}"
#положительное число с плавающей точкой - преобразовано в отрицательное
assert make_negative(7.5) == -7.5, f"Expected: -7.5, got: {make_negative(7.5)}"
#не число
assert make_negative('7') == "num should be integer or float", f"Expected: num should be integer or float" \
                                                               f", got: {make_negative(7.5)}"




#УСЛОЖНЕНИЕ ЗАДАЧКИ СО СПИСКОМ ЧИСЕЛ

def make_negative_list_1(nums: List[Union[int, float]]) -> List[Union[int, float]]:
    """Решение для задачки, когда подается список чисел с помощью list comprehension
    алгоритмическая сложность
    проверка типа переменной: O(1)
    фильтрация списка: O(len(nums))
    преобразование списка: O(len(nums))
    всего: O(1) + O(len(nums)) + O(len(nums))"""
    if type(nums) != list:
        return "nums should be list"
    else:
        filtered_nums = list(filter(lambda x: isinstance(x, int|float), nums))
        return [num*(-1) if num > 0 else num for num in filtered_nums]

#список из положительных целых чисел, отрицательных, с плавающей точкой и 0
assert make_negative_list_1([-77, 8, -1, 0, 7.5, -8.2]) == [-77, -8, -1, 0, -7.5, -8.2], \
    f"Expected: [-77, -8, -1, 0, -7.5, -8.2], got: {make_negative_list_1([-77, 8, -1, 0, 7.5, -8.2])}"
#список не только из чисел - отфильтрован по числам и преобразован
assert make_negative_list_1(['-77', 8, 'one', 0, 7.5, -8.2, (1,)]) == [-8, 0, -7.5, -8.2], \
    f"Expected: [-8, 0, -7.5, -8.2], got: {make_negative_list_1(['-77', 8, 'one', 0, 7.5, -8.2, (1,)])}"
#пустой список
assert make_negative_list_1([]) == [], \
    f"Expected: [], got: {make_negative_list_1([])}"
#список из 1 числа
assert make_negative_list_1([1]) == [-1], \
    f"Expected: [-1], got: {make_negative_list_1([1])}"
#на вход подали не список
assert make_negative_list_1((1, 2, 3)) == "nums should be list", \
    f"Expected: nums should be list, got: {make_negative_list_1((1, 2, 3))}"


def make_negative_list_2(nums: List[Union[int, float]]) -> List[Union[int, float]]:
    """Решение для задачки, когда подается список чисел с помощью фп
    алгоритмическая сложность
    проверка типа переменной: O(1)
    фильтрация списка: O(len(nums))
    преобразование списка: O(len(nums))
    всего: O(1) + O(len(nums)) + O(len(nums))"""
    if type(nums) != list:
        return "nums should be list"
    else:
        filtered_nums = list(filter(lambda x: isinstance(x, int | float), nums))
        return list(map(lambda num: num*(-1) if num > 0 else num, filtered_nums))

#список из положительных целых чисел, отрицательных, с плавающей точкой и 0
assert make_negative_list_2([-77, 8, -1, 0, 7.5, -8.2]) == [-77, -8, -1, 0, -7.5, -8.2], \
    f"Expected: [-77, -8, -1, 0, -7.5, -8.2], got: {make_negative_list_2([-77, 8, -1, 0, 7.5, -8.2])}"
#список не только из чисел - отфильтрован по числам и преобразован
assert make_negative_list_2(['-77', 8, 'one', 0, 7.5, -8.2, (1,)]) == [-8, 0, -7.5, -8.2], \
    f"Expected: [-8, 0, -7.5, -8.2], got: {make_negative_list_2(['-77', 8, 'one', 0, 7.5, -8.2, (1,)])}"
#пустой список
assert make_negative_list_2([]) == [], \
    f"Expected: [], got: {make_negative_list_2([])}"
#список из 1 числа
assert make_negative_list_2([1]) == [-1], \
    f"Expected: [-1], got: {make_negative_list_2([1])}"
#на вход подали не список
assert make_negative_list_2((1, 2, 3)) == "nums should be list", \
    f"Expected: nums should be list, got: {make_negative_list_2((1, 2, 3))}"

