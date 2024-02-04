#Напишите функцию, которая принимает два целых числа (a, b, где a < b)
#и возвращает массив всех целых чисел между введеными числами, включая их.
#Пример:
#Input: (1, 4) Output: [1,2,3,4]
#Input: (-2,2) Output: [-2,-1,0,1,2]

from typing import List

def between(num1: int, num2: int) -> List[int]:
    between_nums = [i for i in range(num1, num2+1)]
    return between_nums

assert between(1, 4) == [1,2,3,4], f"Expected: [1, 2, 3, 4], got: {between(1, 4)}"
assert between(-2, 2) == [-2,-1,0,1,2], f"Expected: [-2,-1,0,1,2], got: {between(1, 4)}"

#не знаю, что еще придумать по проверкам, четко сказано в условии, что два integer, точно первое число меньше второго

