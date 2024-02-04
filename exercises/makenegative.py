#Функция принимает число и делает его отрицательным. Ноль не имеет какого-либо математического знака
#Если число отрицательное, тогда никаких действий не требуется
#Пример:
#Input: 1 Output: -1
#Input: -5 Output: -5

from typing import Union

def make_negative(num: Union[int, float]) -> Union[int, float]:
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
