# Создайте функцию, которая конвертирует доллары США (USD) в китайские юани (CNY).
# Функция принимает сумму долларов США как целое число, а на выходе должна быть строка,
# содержащая сумму юаней и надпись 'Chinese Yuan.
# Курс конвертации - 7.75 юаней за 1 доллар. Все числа должны быть в виде строки с 2 знаками после запятой.
# Пример:
# Input: 15 Output: '101.25 Chinese Yuan';
# Input: 465 Output: '3138.75 Chinese Yuan';

from typing import Union


def usdcny(usd: Union[int, float]) -> str:
    cny = usd * 7.75
    return f"{cny:.2f} Chinese Yuan"

assert usdcny(15) == "116.25 Chinese Yuan", f"Expected: 116.25 Chinese Yuan, got: {usdcny(15)}"
assert usdcny(465) == "3603.75 Chinese Yuan", f"Expected: 3603.75 Chinese Yuan, got: {usdcny(465)}"
assert usdcny(0) == "0.00 Chinese Yuan", f"Expected: 0.00 Chinese Yuan, got: {usdcny(0)}"


