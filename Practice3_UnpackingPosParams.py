
def print_params(a=1, b='string', c=True):
    print(a, b, c)

print_params(1)
print_params(2,5)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
print('\n \n')
values_list = [1, 'new', False]
values_dict = {'a' : 23, 'b' : 'dictNew', 'c' : True}

print_params(*values_list)
print_params(**values_dict)
print('\n \n')

values_list_2 = [34.33, 'strong string']
print_params(*values_list_2, 77)
