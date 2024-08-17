def list_to_string(lst):
    if len(lst) == 0:
        return ''
    elif len(lst) == 1:
        return str(lst[0])
    else:
        return ', '.join(map(str, lst[:-1])) + ' and ' + str(lst[-1])

frutas = ['maçãs', 'bananas', 'uvas', 'peras']
string_frutas = list_to_string(frutas)
print(string_frutas) 