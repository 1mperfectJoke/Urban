def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input('Введите кол-во строк матрицы: '))
m = int(input('Введите кол-во столбцов матрицы: '))
value = input(f'Введите значение: ')
print('--------' * m)
matrix = get_matrix(n, m, value)

if n <= 0:
    print('Недопустимое кол-во строк: ', n)
elif m <= 0:
    print('Недопустимое кол-во столбцов:', m)
else:
    print('Результат: ')
    for i in matrix:
        print(*i)