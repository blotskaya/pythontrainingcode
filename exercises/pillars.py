#Вдоль дороги расположены столбы на равном расстоянии друг от друга. Найдите длину участка дороги между первым
#и последним столбом в сантиметрах (не учитывая ширину крайних столбов).
#Расстояние между соседними столбами и ширина каждого столба одинаковы.
#Функция принимает три аргумента:

#— количество столбов (≥ 1);
#— расстояние между соседними столбами в метрах (от 10 до 30);
#— ширина столба в сантиметрах (от 10 до 50).

#Пример:
#Input: (2, 20, 25) Output: 2000;
#Input: (1, 10, 10) Output: 0;

from typing import Union

def pillars(count: int, s: Union[int, float], width: Union[int, float]) -> Union[int, float]:
    if count < 1 or s < 10 or s > 30 or width < 10 or width > 50:
        return "Invalid data"
    else:
        if count < 3:
            way_s = s*100*(count-1)
        else:
            way_s = s*100*(count-1) - width*(count-2)
    return(way_s)

#минимальные валидные данные
assert pillars(1, 10, 10) == 0, f"Expected: 0, got: {pillars(1, 10, 10)}"
#валидные данные без учета ширины столба
assert pillars(2, 20, 25) == 2000, f"Expected: 2000, got: {pillars(2, 20, 25)}"
#максимальные валидные данные с учетом ширины столба,
# кроме кол-ва столбов (нет данных о макс кол-ве столбов)
assert pillars(4, 30, 50) == 8900, f"Expected: 8900, got: {pillars(4, 30, 50)}"
#невалидное кол-во столбов
assert pillars(0, 30, 40) == "Invalid data", f"Expected: Invalid data, got: {pillars(0, 30, 40)}"
#граничное значение расстояния между столбами
assert pillars(2, 31, 40) == "Invalid data", f"Expected: Invalid data, got: {pillars(2, 31, 40)}"
#граничное значение ширины столба
assert pillars(2, 30, 51) == "Invalid data", f"Expected: Invalid data, got: {pillars(2, 30, 51)}"
#не целые числа
assert pillars(2, 29.9, 49.5) == 2990.0, f"Expected: 2990.0, got: {pillars(2, 29.9, 49.5)}"



