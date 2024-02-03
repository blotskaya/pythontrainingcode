#Создайте функцию, которая принимает любое неотрицательное целое число в качестве
#аргумента и возвращать его цифры в порядке убывания.
#Пример:
#Input: 145263 Output: 654321
#Input: 123456789 Output: 987654321

def descending_order(num):
    strnum = list(str(num))
    for i in range(len(strnum)):
        for i in range(len(strnum)-1):
            if strnum[i] < strnum[i+1]:
                strnum[i], strnum[i+1] = strnum[i+1], strnum[i]
    return int(''.join(strnum))


assert descending_order(145263) == 654321
assert descending_order(98765) == 98765
assert descending_order(12345) == 54321