#Функция принимает число и делает его отрицательным. Ноль не имеет какого-либо математического знака
#Если число отрицательное, тогда никаких действий не требуется
#Пример:
#Input: 1 Output: -1
#Input: -5 Output: -5

def make_negative(num):
    if num > 0:
        return num*(-1)
    else:
        return num

assert make_negative(4) == -4 #положительное число
assert make_negative(-77) == -77 #отрицательное число
assert make_negative(0) == 0 #ноль
assert make_negative(7.5) == -7.5 #число с плавающей точкой
