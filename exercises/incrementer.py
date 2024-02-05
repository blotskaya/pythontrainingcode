#Получив на вход массив чисел, верните массив с каждой цифрой, увеличенной на ее позицию в массиве:
#первая цифра будет увеличена на 1, вторая — на 2 и т.д. Обязательно начинайте отсчет с 1 (а не с 0).
#Внимание!
#Ваш результат может содержать только однозначные числа, поэтому, если при сложении цифры с
#ее позицией получается двузначное число, то возвращается только последняя цифра числа.
#Пример:
#Input: [1, 2, 3] Output: [2, 4, 6]
#Input: [4, 6, 9, 1, 3] Output: [5, 8, 2, 5, 8]

from typing import List

def incrementer(numlist: List[int]) -> List[int]:
    if type(numlist) != list:
        return "numlist should be list"
    else:
        filtered_numlist = list(filter(lambda x: type(x) == int, numlist))
        incrementer_list = [(i + filtered_numlist.index(i) + 1) % 10 for i in filtered_numlist]
        return incrementer_list

#есть числа, которые при сложении с индексом вернут 2-значное число
assert incrementer([4, 6, 9, 1, 3]) == [5, 8, 2, 5, 8], f"Expected: [5, 8, 2, 5, 8], got: {incrementer([4, 6, 9, 1, 3])}"
#все числа вернут однозначное число при сложении с индексом
assert incrementer([1, 2, 3]) == [2, 4, 6], f"Expected: [2, 4, 6], got: {incrementer([1, 2, 3])}"
#числа больше, чем 2-значные
assert incrementer([10, 100, 2000]) == [1, 2, 3], f"Expected: [1, 2, 3], got: {incrementer([10, 100, 2000])}"
#отрицательные числа
assert incrementer([-1, -2, -3]) == [0, 0, 0], f"Expected: [0, 0, 0], got: {incrementer([-1, -2, -3])}"
#пустой список
assert incrementer([]) == [], f"Expected: [], got: {incrementer([])}"
#не список
assert incrementer({1, 2, 3}) == "numlist should be list", f"Expected: numlist should be list, " \
                                                           f"got: {incrementer({1, 2, 3})}"
#не все числа целые - список отфильтровывается до целых чисел, а затем увеличивает их на индексы + 1
assert incrementer([1, '2', 3, 3.5]) == [2, 5], f"Expected: [2, 5], got: {incrementer([1, '2', 3, 3.5])}"
#одно число
assert incrementer([1]) == [2], f"Expected: [2], got: {incrementer([1])}"
#в списке одно значение, не являющееся целым число - возвращается пустой список
assert incrementer(['1']) == [], f"Expected: [], got: {incrementer(['1'])}"
