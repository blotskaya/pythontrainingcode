#Функция принимает массив из чисел и строк и возвращает новый массив состоящий только из чисел.
#Пример:
#Input: [1,2,'a','b'] Output: [1,2];
#Input: [1,2,'aasf','1','123',123] Output: [1,2,123];

def filter_list(list_):
    return [i for i in list_ if type(i)==int]


assert filter_list([1,2,'a','b']) == [1,2] #числа и строки
assert filter_list(['aasf','1','123','abc']) == [] #только строки
assert filter_list([1, 2, 3]) == [1, 2, 3] #только числа
