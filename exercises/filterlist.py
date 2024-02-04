#Функция принимает массив из чисел и строк и возвращает новый массив состоящий только из чисел.
#Пример:
#Input: [1,2,'a','b'] Output: [1,2];
#Input: [1,2,'aasf','1','123',123] Output: [1,2,123];

from typing import List, Union

def filter_list(list_: List[Union[str, int]]) -> List[int]:
    """Решение с помощью list comprehention и type"""
    return [i for i in list_ if type(i)==int]


#числа и строки
assert filter_list([1,2,'a','b']) == [1,2], f"Expected: [1, 2], got: {filter_list([1,2,'a','b'])}"
#только строки
assert filter_list(['aasf','1','123','abc']) == [], f"Expected: [], got: {filter_list(['aasf','1','123','abc'])}"
#только числа
assert filter_list([1, 2, 3]) == [1, 2, 3] , f"Expected: [], got: {filter_list([1, 2, 3])}"

def filter_list_2(list_: List[Union[str, int]]) -> List[int]:
    """Решение с помощью фп и isinstance"""
    num_list = list(filter(lambda num: isinstance(num, int), list_))
    return num_list

