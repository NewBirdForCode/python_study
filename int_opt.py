
from math import *

int_add_float = 3 + 0.1
print(int_add_float)

int_x_float = 3 * 0.1
print(int_x_float)

int_div_float = 3 / 0.1
print(int_div_float)

print(floor(3.4))
print(ceil(3.4))


a = 21
b = 10
c = 0


c = a + b
print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为: ", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)

c = a % b
print("5 - c 的值为：", c)

a = 2
b = 3
c = a ** b
print("6 - c 的值为：", c )

a = 10
b = 5
c = a // b
print("7 - c 的值为: ", c )


a = 21
b = 10
c = 0

if(a == b):
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if(a != b):
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if( a < b ):
    print("3 - a 小于 b")
else:
    print("3 - a 大于等于 b")

if(a > b ):
    print("4 - a 大于 b")
else:
    print("4 - a 小于等于 b")


a = 5
b = 20
if( a <= b ):
    print("5 - a 小于等于 b")
else:
    print("5 - a 大于 b")

if (b >= a ):
    print("6 - b大于等于 a ")
else:
    print("6 - b小于 a ")


a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c )

c += a
print("2 - c 的值为：", c )

c *= a
print("3 - c 的值为：", c )

c /= a
print("4 - c 的值为：", c )

c = 2
c %= a
print("5 - c 的值为：", c )

c **= a
print("6 - c 的值为：", c )

c //= a
print("7 - c 的值为：", c )


a = 10
b = 20

if( a and b ):
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 都为 true,或其中一个变量为 true")

if( a or b ):
    print("2 - 变量 a 和 b 都为 true,或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")


a = 10
b = 20
list = [1, 2, 3, 4, 5 ]

if( a in list):
    print("1 - 变量 a 在给定的列表中 list 中"
          )