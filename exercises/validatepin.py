#Функция проверяет, является ли переданная ей строка верным PIN-кодом,
#и возвращает true или false в зависимости от результата.
#Банкомат позволяют вводить PIN-коды, состоящие из 4 или 6 цифр.
#Верные PIN-коды должны содержать только цифры и иметь длину 4 или 6 символов.
#Пример:
#Input: 1234 Output: true
#Input: a234 Output: false

def validatepin(pin: str) -> bool:
    if 4 <= len(pin) <= 6 and pin.isnumeric():
        return True
    else:
        return False

#буква в строке
assert validatepin("a235") == False, f"Expected: False, got: {validatepin('a235')}"
#4 цифры
assert validatepin("1234") == True, f"Expected: True, got: {validatepin('1234')}"
#пустая строка
assert validatepin("") == False, f"Expected: False, got: {validatepin('')}"
#6 цифр
assert validatepin("556677") == True, f"Expected: True, got: {validatepin('556677')}"
#спец символ в строке
assert validatepin("12&7") == False, f"Expected: False, got: {validatepin('12&7')}"
#цифр больше
assert validatepin("5566778") == False, f"Expected: False, got: {validatepin('5566778')}"
#цифр меньше
assert validatepin("678") == False, f"Expected: False, got: {validatepin('678')}"

