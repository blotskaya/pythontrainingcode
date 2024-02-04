#Создайте функцию, которая принимает любое неотрицательное целое число в качестве
#аргумента и возвращать его цифры в порядке убывания.
#Пример:
#Input: 145263 Output: 654321
#Input: 123456789 Output: 987654321

def descending_order(num: int) -> int:
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