
print('hi world')

print('hi world')


str_b = str_a = 'hello world'
print(str_b[0])

str_b=str_a = 'hello world'
print(str_b[0])

str_a = str_a.replace('hello','hi')


str_a = str_a.replace('hello', 'hi')

print(str_a)
print(str_b)


print(str_a)
print(str_b)


tuple_a = ('a', 'b', 'c', 'd')
print(type(tuple_a),tuple_a)


tuple_a = ('a', 'b', 'c', 'd')
print(type(tuple_a), tuple_a)
# a[0] = 'hello world'

list_a = ['a', 'b', 'c', 1, 2, 3.14, False]
print(type(list_a), list_a)
list_a[0] = 'hello'
print(list_a)
list_a.append('world')
print(list_a)


dict_a = {'name': 'Leon', 'age': 18}  #{key:value1, key2:value2, key3:value2}
print(type(dict_a), dict_a)
print(dict_a['name'], dict_a['age'])
dict_a['car'] = False
print(dict_a)

set_a = {'name', 'age', 'Leon', 18}  # {value1, value2, value3, value4.....}
print(type(set_a), set_a)

for j in set_a:
    print(j)

set_a.add('car')
print(set_a)
