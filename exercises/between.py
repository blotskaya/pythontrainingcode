#Напишите функцию, которая принимает два целых числа (a, b, где a < b)
#и возвращает массив всех целых чисел между введеными числами, включая их.
#Пример:
#Input: (1, 4) Output: [1,2,3,4]
#Input: (-2,2) Output: [-2,-1,0,1,2]

from typing import List

def between(num1: int, num2: int) -> List[int]:
    if not isinstance(num1, int) or not isinstance(num2, int):
        return "num1 and num2 should be integers"
    elif num1 > num2 or num1==num2:
        return "num1 should be less than num2"
    else:
        between_nums = [i for i in range(num1, num2+1)]
        return between_nums

#положительные целые числа, первое меньше второго
assert between(1, 4) == [1,2,3,4], f"Expected: [1, 2, 3, 4], got: {between(1, 4)}"
#отрицательные целые числа, первое меньше второго
assert between(-5, -2) == [-5,-4,-3,-2], f"Expected: [-5,-4,-3,-2], got: {between(1, 4)}"
#одно из чисел не является integer, а string
assert between(4, '1') == "num1 and num2 should be integers", f"Expected: num1 and num2 should be " \
                                                                       f"integers, got: {between(4, '1')}"
#одно из чисел не является integer, а string
assert between('one', 5) == "num1 and num2 should be integers", f"Expected: num1 and num2 should be " \
                                                                         f"integers, got: {between('one', 5)}"
#первое число больше второго
assert between(4, 1) == "num1 should be less than num2", f"Expected: num1 should be less than num2, " \
                                                         f"got: {between(4, 1)}"
#одно из чисел не является integer, а float
assert between(1.5, 5) == "num1 and num2 should be integers", f"Expected: num1 and num2 should be " \
                                                                         f"integers, got: {between(1.5, 5)}"
#одно из чисел не является integer, а float
assert between(1, 5.25) == "num1 and num2 should be integers", f"Expected: num1 and num2 should be " \
                                                                         f"integers, got: {between(1, 5.25)}"
#числа равны друг другу
assert between(1, 1) == "num1 should be less than num2", f"Expected: num1 should be less than num2" \
                                                         f", got: {between(1, 1)}"


