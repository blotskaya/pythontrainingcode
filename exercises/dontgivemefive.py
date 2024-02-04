#Функция принимает на вход начальное и конечное число. Возвращает общее количество чисел между этими
#двумя числами (включительно), за исключением чисел с цифрой 5.
#Пример:
#Input: 1, 9 Output: 8
#Input: 4, 17 Output: 12

def dontgivemefive(num1: int, num2: int) -> int:
    num_list = [num for num in range(num1, num2+1) if '5' not in str(num)]
    return len(num_list)

assert dontgivemefive(4, 17) == 12 #есть 5 в числах на последней позиции
assert dontgivemefive(5, 17) == 11 #отсчет с 5
assert dontgivemefive(50, 56) == 0 #все цифры содержат 5
assert dontgivemefive(0, 4) == 5 #нет чисел с цифрой 5