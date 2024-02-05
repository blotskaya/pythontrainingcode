# Создайте функцию, которая конвертирует доллары США (USD) в китайские юани (CNY).
# Функция принимает сумму долларов США как целое число, а на выходе должна быть строка,
# содержащая сумму юаней и надпись 'Chinese Yuan.
# Курс конвертации - 7.75 юаней за 1 доллар. Все числа должны быть в виде строки с 2 знаками после запятой.
# Пример:
# Input: 15 Output: '101.25 Chinese Yuan';
# Input: 465 Output: '3138.75 Chinese Yuan';

from typing import Union


def usdcny(usd: Union[int, float]) -> str:
    if not isinstance(usd, int|float):
        return "usd should be integer or float"
    else:
        cny = usd * 7.75
        return f"{cny:.2f} Chinese Yuan"

#целое число
assert usdcny(15) == "116.25 Chinese Yuan", f"Expected: 116.25 Chinese Yuan, got: {usdcny(15)}"
#число с плавающей точкой
assert usdcny(465.5) == "3607.62 Chinese Yuan", f"Expected: 3607.62 Chinese Yuan, got: {usdcny(465)}"
#ноль
assert usdcny(0) == "0.00 Chinese Yuan", f"Expected: 0.00 Chinese Yuan, got: {usdcny(0)}"
#не число
assert usdcny('78') == "usd should be integer or float", f"Expected: usd should be integer or floatusd " \
                                                         f"should be integer or float, got: {usdcny('78')}"


