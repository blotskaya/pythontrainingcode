#Заполните решение так, чтобы функция разбивала верблюжью нотацию, используя пробел между словами.
#Пример:
#Input: "camelCasing" Output: "camel Casing"
#Input: "identifier" Output: "identifier"

def camel_casing(string_):
    new_string = (''.join([" "+letter if letter.isupper() else letter for letter in string_])).rstrip().lstrip()
    return new_string

assert camel_casing("camelCasing") == "camel Casing" #одна большая буква в центре строки
assert camel_casing("identifier") == "identifier" #нет больших букв
assert camel_casing("Apple") == "Apple" #одна большая буква в начале строки
assert camel_casing("AppleBananaPineapple") == "Apple Banana Pineapple" #несколько больших букв
assert camel_casing("ABC") == "A B C" #большая буква в конце строки

