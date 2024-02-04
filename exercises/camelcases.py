#Заполните решение так, чтобы функция разбивала верблюжью нотацию, используя пробел между словами.
#Пример:
#Input: "camelCasing" Output: "camel Casing"
#Input: "identifier" Output: "identifier"

def camel_casing(string_: str) -> str:
    new_string = (''.join([" "+letter if letter.isupper() else letter for letter in string_])).rstrip().lstrip()
    return new_string

#одна большая буква в центре строки
assert camel_casing("camelCasing") == "camel Casing", f"Expected: 'camel Casing', got: {camel_casing('camelCasing')}"
#нет больших букв
assert camel_casing("identifier") == "identifier", f"Expected: 'identifier', got: {camel_casing('identifier')}"
#одна большая буква в начале строки, до нее нет пробела
assert camel_casing("Apple") == "Apple", f"Expected: 'Apple', got: {camel_casing('Apple')}"
#несколько больших букв
assert camel_casing("AppleBananaPineapple") == "Apple Banana Pineapple", \
    f"Expected: 'Apple Banana Pineapple', got: {camel_casing('AppleBananaPineapple')}"
#большая буква в конце строки, после нее нет пробела
assert camel_casing("ABC") == "A B C", f"Expected: 'A B C', got: {camel_casing('ABC')}"

