# 1. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('Введите число x '))
# y = int(input('Введите число y '))
# z = int(input('Введите число z '))

# a = x * y * z
# b = x + y + z

# if a > 0:
#     a = 0
# elif a < 1:
#     a = 1
# if b > 0:
#     b = 1
# elif b < 1:
#     b = 1

# if a == b:
#     print('Утверждение истинно')
# elif a != b:
#     print('Утверждение ложно')

# leftSide = not (x or y or z)
# rightSide = not x and not y and not z
# result = leftSide == rightSide

# if result == True:
#     print('Утверждение истинно')
# else:
#     print('Утверждение ложно')


#Или можно так

for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)


# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# и выдаёт номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x = int(input('input x: '))
y = int(input('input y: '))
if x > 0 and y > 0:
    print('1')
if x < 0 and y > 0:
    print('2')
if x < 0 and y < 0:
    print('3')
if x > 0 and y < 0:
    print('4')