# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать
# сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions

a = input("Введите первую дробь с числителем и знаменателем в формате a/b: ")
b = input("Введите вторую дробь с числителем и знаменателем в формате a/b: ")

parts_a = a.split('/')
numerator_a  = int(parts_a[0])
denominator_a = int(parts_a[1])

parts_b = b.split('/')
numerator_b  = int(parts_b[0])
denominator_b = int(parts_b[1])

a_fr = fractions.Fraction(numerator_a,denominator_a)
b_fr = fractions.Fraction(numerator_b, denominator_b)

print (a_fr, b_fr)
print (a_fr * b_fr)