

str_a = 'hello'
str_b = 'world'

a_add_b = str_a + str_b
print(a_add_b)
print(str_a.find('l'), str_a.rfind('l'))
print(str_a.count('a'))
print(str_a.replace('e', 'x'), str_a)
print(str_a.isalpha(), str_a.isdigit(),str_a.isalnum())



a_add_b = str_a + str_b
print(a_add_b)
print(str_a.find('l'), str_a.rfind('l'))
print(str_a.count('a'))
print(str_a.replace('e', 'x'), str_a)
print(str_a.isalpha(), str_a.isdigit(), str_a.isalnum())


int_a = 123456789
str_int_a = str(int_a)
int_str_a = int(str_int_a)

int_a = 123456789
str_int_a = str(int_a)
int_str_a = int(str_int_a)
print(type(str_int_a), str_int_a)
print(type(int_str_a))

print(str_a.startswith('hello'), str_a.endswith('o'))

print(str_a.upper())

print(str_a.split(' '))
print(str_a.istitle())
print('hello {name}, {age}, {name}, {name}'.format(name="Tom", age=18))

str_list = ['hello', 'world', 'Andy']
print('+'.join(str_a))

print('0X123'.isdecimal())
print(str_a.capitalize())
print('asdf_@@@'.isidentifier())
print('  hello world        @     \t \r\n'.strip())