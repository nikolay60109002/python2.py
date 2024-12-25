def gcd_euclid(a, b):
    while b:
        a, b = b, a % b
    return a

# Преобразуем число 255 в шестнадцатеричное представление
number = 255
hex_string = hex(number)
print(hex_string)  # Выведет '0xff'

import roman

def int_to_roman(num):
    return roman.toRoman(num)

# Пример использования
print(int_to_roman(1994))  # Выведет "MCMXCIV"

from fractions import Fraction

def sum_and_product(frac1_str, frac2_str):
    # Парсим входные данные
    frac1 = Fraction(frac1_str)
    frac2 = Fraction(frac2_str)
    
    # Вычисляем сумму и произведение
    sum_frac = frac1 + frac2
    product_frac = frac1 * frac2
    
    # Возвращаем результаты
    return str(sum_frac), str(product_frac)

from fractions import Fraction

def sum_and_product(frac1_str, frac2_str):
    # Парсим входные данные
    frac1 = Fraction(frac1_str)
    frac2 = Fraction(frac2_str)
    
    # Вычисляем сумму и произведение
    sum_frac = frac1 + frac2
    product_frac = frac1 * frac2
    
    # Возвращаем результаты
    return str(sum_frac), str(product_frac)

# Пример использования
result = sum_and_product("1/2", "3/4")
print(result)  # ('5/4', '3/8')





