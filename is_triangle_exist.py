# Треугольник существует только тогда, когда сумма любых двух его
# сторон больше третьей. Дано: a, b, c – стороны предполагаемого
# треугольника. Напишите программу, которая укажет, существует ли
# такой треугольник или нет.

a = int(input())
b = int(input())
c = int(input())

res = True if a + b > c and a + c > b and b + c > a else False
print(res)
