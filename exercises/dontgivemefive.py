#Функция принимает на вход начальное и конечное число. Возвращает общее количество чисел между этими
#двумя числами (включительно), за исключением чисел с цифрой 5.
#Пример:
#Input: 1, 9 Output: 8
#Input: 4, 17 Output: 12

def dontgivemefive(num1: int, num2: int) -> int:
    if type(num1) != int or type(num2) != int:
        return "num1 and num2 should be integer"
    elif num1 > num2 or num1==num2:
        return "num1 should be less than num2"
    else:
        num_list = [num for num in range(num1, num2+1) if '5' not in str(num)]
        return len(num_list)

#есть 5 в числах на последней позиции
assert dontgivemefive(4, 17) == 12, f"Expected: 12, got: {dontgivemefive(4, 17)}"
#отсчет с 5
assert dontgivemefive(5, 17) == 11, f"Expected: 11, got: {dontgivemefive(5, 17)}"
#все цифры содержат 5
assert dontgivemefive(50, 56) == 0, f"Expected: 0, got: {dontgivemefive(50, 56)}"
#нет чисел с цифрой 5
assert dontgivemefive(0, 4) == 5, f"Expected: 5, got: {dontgivemefive(0, 4)}"
#первое число больше второго
assert dontgivemefive(17, 1) == "num1 should be less than num2", f"Expected: num1 should be less than num2, " \
                                                                 f"got: {dontgivemefive(17, 1)}"
#первое число не целое
assert dontgivemefive(1.77, 11) == "num1 and num2 should be integer", f"Expected: num1 and num2 should be integer, " \
                                                                 f"got: {dontgivemefive(1.77, 11)}"
#второе число не целое
assert dontgivemefive(5, "ten") == "num1 and num2 should be integer", f"Expected: num1 and num2 should be integer, " \
                                                                 f"got: {dontgivemefive(5, 'ten')}"
#числа равны друг другу
assert dontgivemefive(5, 5) == "num1 should be less than num2", f"Expected: num1 should be less than num2, " \
                                                                 f"got: {dontgivemefive(5, 'ten')}"

