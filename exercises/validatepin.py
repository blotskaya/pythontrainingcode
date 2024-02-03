#Функция проверяет, является ли переданная ей строка верным PIN-кодом,
#и возвращает true или false в зависимости от результата.
#Банкомат позволяют вводить PIN-коды, состоящие из 4 или 6 цифр.
#Верные PIN-коды должны содержать только цифры и иметь длину 4 или 6 символов.
#Пример:
#Input: 1234 Output: true
#Input: a234 Output: false

def validatepin(pin):
    if 4 <= len(pin) <= 6 and pin.isnumeric():
        return True
    else:
        return False
assert validatepin("a235") == False #буква в строке
assert validatepin("1234") == True #4 цифры
assert validatepin("") == False #пустая строка
assert validatepin("556677") == True #6 цифр
assert validatepin("12&7") == False #спец символ в строке
assert validatepin("5566778") == False #цифр больше
assert validatepin("678") == False #цифр меньше

