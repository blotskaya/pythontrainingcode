#Функция принимает массив из чисел и строк и возвращает новый массив состоящий только из чисел.
#Пример:
#Input: [1,2,'a','b'] Output: [1,2];
#Input: [1,2,'aasf','1','123',123] Output: [1,2,123];

from typing import List, Union

def filter_list(list_: List[Union[str, int]]) -> List[int]:
    """Решение с помощью list comprehention и type
    алгоритмическая сложность
    проверка типа переменной: O(1)
    фильтрация списка: O(len(list_))
    всего O(1) + O(len(list_))"""
    if type(list_) != list:
        return "list_ should be list"
    else:
        return [i for i in list_ if type(i)==int]


#числа и строки
assert filter_list([1,2,'a','b']) == [1,2], f"Expected: [1, 2], got: {filter_list([1,2,'a','b'])}"
#только строки
assert filter_list(['aasf','1','123','abc']) == [], f"Expected: [], got: {filter_list(['aasf','1','123','abc'])}"
#только числа
assert filter_list([1, 2, 3]) == [1, 2, 3], f"Expected: [1, 2, 3], got: {filter_list([1, 2, 3])}"
#пустой список
assert filter_list([]) == [], f"Expected: [], got: {filter_list([])}"
#не список
assert filter_list({1, 2, 3}) == "list_ should be list", f"Expected: list_ should be list" \
                                                         f", got: {filter_list({1, 2, 3})}"
#пустая строка
assert filter_list([1,2,'','b']) == [1,2], f"Expected: [1, 2], got: {filter_list([1,2,'','b'])}"

#не думаю, что нам нужно проверять, какие данные нам подали на вход, так как список всё равно фильтрует по целым числам


def filter_list_2(list_: List[Union[str, int]]) -> List[int]:
    """Решение с помощью фп и isinstance
    алгоритмическая сложность:
    проверка типа переменной: O(1)
    фильтрация списка: O(len(list_))
    всего O(1) + O(len(list_))"""
    if type(list_) != list:
        return "list_ should be list"
    else:
        return list(filter(lambda num: isinstance(num, int), list_))

#числа и строки
assert filter_list_2([1,2,'a','b']) == [1,2], f"Expected: [1, 2], got: {filter_list_2([1,2,'a','b'])}"
#только строки
assert filter_list_2(['aasf','1','123','abc']) == [], f"Expected: [], got: {filter_list_2(['aasf','1','123','abc'])}"
#только числа
assert filter_list_2([1, 2, 3]) == [1, 2, 3], f"Expected: [1, 2, 3], got: {filter_list_2([1, 2, 3])}"
#пустой список
assert filter_list_2([]) == [], f"Expected: [], got: {filter_list_2([])}"
#не список
assert filter_list_2({1, 2, 3}) == "list_ should be list", f"Expected: list_ should be list" \
                                                         f", got: {filter_list_2({1, 2, 3})}"
#пустая строка
assert filter_list_2([1,2,'','b']) == [1,2], f"Expected: [1, 2], got: {filter_list_2([1,2,'','b'])}"
#не думаю, что нам нужно проверять, какие данные нам подали на вход, так как список всё равно фильтрует по целым числам