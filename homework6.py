# Работа со словарями
my_dict = {'Max': 1, 'Alyona': 4, 'Sveta': 16, 'Dima': 5, 'Katya': 84}
print(my_dict)
print(my_dict['Sveta'], my_dict.get('Seryoga'))
my_dict.update({'Denis': 3, 'Lyosha': 4})
del my_dict['Dima']
print(my_dict.get('Dima'))
print(my_dict)

#Работа с множествами
my_set = (1,25,6,8,1,25,9,8,True,'Pika',1,True,False,'Kaka')
my_set = set(my_set)
print(my_set)
my_set.add(13)
my_set.add('Yeah')
my_set.remove(9)
print(set(my_set))
