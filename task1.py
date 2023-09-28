# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex 
# используйте для проверки своего результата.
a = int(input("Введите целое число: "))
result = ""
DIVIDER = 16
START = 2
b = hex(a)
while a > 0:
    result = str(a%DIVIDER) + result
    a = a//DIVIDER
print (b, result)
if result == b[START:]:
    print(True)