#Задайте переменные разных типов данных
immutable_var = (1, 'два', True)
print(immutable_var)

#Изменение значений переменных
#immutable_var[0] = 2
#print(immutable_var) кортеж не поддерживает обращение по элементам

#Создание изменяемых структур данных
mutable_list = [1, 'two', True]
print(mutable_list)
mutable_list[1] = 2
mutable_list[2] = 3+4
print(mutable_list)