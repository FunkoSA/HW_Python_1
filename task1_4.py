
number = int(input('Введите номер четверти координат: '))
if number == 1:
    print (f'Точка принадлежит {number} если ее координатами следующие Х > 0 Y > 0')
elif number == 2:
    print (f'Точка принадлежит {number} если ее координатами следующие Х < 0 Y > 0')
elif number == 3:
    print (f'Точка принадлежит {number} если ее координатами следующие Х < 0 Y < 0')
elif number == 4:
    print (f'Точка принадлежит {number} если ее координатами следующие Х > 0 Y < 0')
else:
    print (f'Четверти №{number} не существует')