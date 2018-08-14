#!/usr/bin/env python

print('hello world!')

# 求平方、立方
print('9的平方：', 9**2)
print('9的立方：', 9**3)


# 从终端接收一个字符,并与100比较大小
number = int(input("Enter an integer: "))
if number <= 100:
    print("比100小")
else:
    print("比100大")

# 计算投资收益
amount = float(input("Enter amount: "))  # 输入数额
inrate = float(input("Enter Interest rate: "))  # 输入利率
period = int(input("Enter period: "))  # 输入期限
value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("Year {} Rs. {:.2f}".format(year, value))
    amount = value
    year = year + 1

# 变量赋值
a, b = 45, 54
print("a: {}, b: {}".format(a, b))
a, b = b, a
print("交换后, a: {}, b: {}".format(a, b))
name, country, language = ("shiyanlou", "China", "Python")
print('name: {}, country: {}, language: {}'.format(name, country, language))

# 运算符和表达式
a = 20 / 7
print(a)
a = 20 // 7
print("取整：{}".format(a))

# divmod(num1, num2) 返回一个元组，这个元组包含两个值，
# 第一个是 num1 和 num2 相整除得到的值，第二个是 num1 和 num2 求余得到的值，
# 然后我们用 * 运算符拆封这个元组，得到这两个值。
days = int(input("Enter days: "))
print("Months = {} Days = {}".format(*divmod(days, 30)))

# 这里与nodejs && || ！操作很像
5 and 4  # 4
0 and 4  # 0
False or 3 or 0  # 3
2 > 1 and not 3 > 5 or 4  # True

# 类型转换
float("3.14")  # 字符串 -> 浮点值
int("5")  # 字符串 -> 整数值
str(52)	 # 整数值 -> 字符串
str(5.23)  # 浮点值 -> 字符串

# 引入包
import math
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
d = b * b - 4 * a * c
if d < 0:
    print("ROOTS are imaginary")
else:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Root 1 = ", root1)
    print("Root 2 = ", root2)

# 计算圆的面积
import math
print(math.pi)
print("半径为2的圆的面积是：{:.10f}".format(2*math.pi*2))

# else if 缩写 elif
a = int(input("输入一个整数："))
if a < 0:
    print('a is 负数')
elif a == 0:
    print('a is zero')
elif a == 1:
    print('a is one')
else:
    print('a大于zero')