#Создайте функцию, которая принимает любое неотрицательное целое число в качестве
#аргумента и возвращать его цифры в порядке убывания.
#Пример:
#Input: 145263 Output: 654321
#Input: 123456789 Output: 987654321

def descending_order(num: int) -> int:
    """Решение задачки с помощью пузырьковой сортировки
    алгоритмическая сложность:
    проверка типа числа: O(1)
    пузырьковая сортировка: O(len(num)**2)
    всего: O(1) + O(len(num)**2)"""
    if type(num) != int:
        return "num should be integer"
    else:
        strnum = list(str(num))
        for i in range(len(strnum)):
            for i in range(len(strnum)-1):
                if strnum[i] < strnum[i+1]:
                    strnum[i], strnum[i+1] = strnum[i+1], strnum[i]
        return int(''.join(strnum))

#числа не упорядочены
assert descending_order(145263) == 654321, f"Expected: 654321, got: {descending_order(145263)}"
#числа уже упорядочены по убыванию
assert descending_order(98765) == 98765, f"Expected: 98765, got: {descending_order(98765)}"
#числа упорядочены по возрастанию
assert descending_order(12345) == 54321, f"Expected: 54321, got: {descending_order(12345)}"
#числа дублируются
assert descending_order(555) == 555, f"Expected: 555, got: {descending_order(555)}"
#однозначное число
assert descending_order(7) == 7, f"Expected: 7, got: {descending_order(7)}"
#число не целое
assert descending_order(555.5) == "num should be integer", f"Expected: num should be integer, " \
                                                           f"got: {descending_order(555.5)}"
#подали на вход не число
assert descending_order("5654") == "num should be integer", f"Expected: num should be integer, " \
                                                           f"got: {descending_order('5654')}"

def descending_order_2(num: int) -> int:
    """Решение задачки с помощью встроенных методов
    алгоритмическая сложность:
    проверка типа числа: O(1)
    перевод числа в строку: O(1)
    перевод строки в список: O(len(num))
    присвоение списка чисел в переменную: O(1)
    сортировка списка: O(len(num) log len(num))
    перевод списка в строку: O(len(num))
    перевод строки в число: O(1)
    присвоение числа в переменную: O(1)
    всего: O(1) + O(1) + O(1) + O(len(num))+ O(len(num)*log(len(num))) + O(len(num)) + O(1) + O(1)"""
    if not isinstance(num, int):
        return "num should be integer"
    else:
        strnum = list(str(num))
        strnum.sort(reverse=True)
        sorted_nums = int(''.join(strnum))
        return sorted_nums

#числа не упорядочены
assert descending_order_2(145263) == 654321, f"Expected: 654321, got: {descending_order(145263)}"
#числа уже упорядочены по убыванию
assert descending_order_2(98765) == 98765, f"Expected: 98765, got: {descending_order(98765)}"
#числа упорядочены по возрастанию
assert descending_order_2(12345) == 54321, f"Expected: 54321, got: {descending_order(12345)}"
#числа дублируются
assert descending_order_2(555) == 555, f"Expected: 555, got: {descending_order(555)}"
#однозначное число
assert descending_order_2(7) == 7, f"Expected: 7, got: {descending_order(7)}"
#число не целое
assert descending_order_2(555.5) == "num should be integer", f"Expected: num should be integer, " \
                                                           f"got: {descending_order(555.5)}"
#подали на вход не число
assert descending_order_2("5654") == "num should be integer", f"Expected: num should be integer, " \
                                                           f"got: {descending_order('5654')}"