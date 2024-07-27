# 1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print('_____________________________________________')

# 2
values_list = ['Чупапик', 999, [1, 2, 3]]
values_dict = {'a': [1, 2, 3], 'b': 'Чупапик', 'c': 999}
print_params(*values_list)
print_params(**values_dict)
print('_____________________________________________')

# 3
values_list_2 = ['дрын', [1, 1, 7]]
print_params(*values_list_2, 42)