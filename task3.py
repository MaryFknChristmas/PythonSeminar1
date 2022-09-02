#Напишите программу, которая принимает на вход координаты точки (X и Y),
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#в которой находится эта точка (или на какой оси она находится).

coord1 = int(input('Введите координату икс '))
coord2 = int(input('Введите координату игрек '))

if coord1 > 0 and coord2 > 0:
    print('1')
elif coord1 < 0 and coord2 > 0:
    print('2')
elif coord1 < 0 and coord2 < 0:
    print('3')
elif coord1 > 0 and coord2 < 0:
    print('4')