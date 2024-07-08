first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))
if first == second and second == third:
    print('Вы ввели 3 одинаковых числа')
elif first == second or second == third or first == third:
    print ('Вы ввели 2 одинаковых числа')
else:
    print('Вы ввели разные числа')