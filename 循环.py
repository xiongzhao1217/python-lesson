# while循环
# 实现斐波拉契数列
(a, b) = [0, 1]    # 等价a, b = (0, 1), 等价a, b = [0, 1], 等价[a, b] = 0, 1,等价(a, b) = 0, 1
print('a={},b={}'.format(a, b))
while b < 100:
    # end= 的作用是打印结束不默认换行，改为引号内的字符结尾
    print(b, end=' ')
    # 注意，不是严格等价a = b, b = a + b, 如果严格等价可知b = b + b,这与运行结果不符
    a, b = b, a + b

# 计算幂级数：e^x = 1 + x + x^2 / 2! + x^3 / 3! + ... + x^n / n! （0 < x < 1）
x = float(input("Enter the value of x: "))
n = term = num = 1
result = 1.0
while n <= 100:
    term *= x / n
    result += term
    n += 1
    if term < 0.0001:
        break
print("No of Times= {} and Sum= {}".format(n, result))

# 打印10以内的乘法表
i, j, col, row = 1, 1, 10, 10
# '-'*50 表示打印50个中划线
print('-' * 50)
while i <= 10:
    while j <= 10:
        # :4d的意思是站位4哥字符长度
        print("{:4d}".format(i * j), end=" ")
        j += 1
    j = 1
    i += 1
    print()
print('-' * 50)

# 打印直角三角形
i, n = 0, int(input("输入行数"))
while i < n:
    i += 1
    print('* ' * i)

# for循环
a = ['ShiYanLou', 'is', 'powerful']
for x in a:
    print(a)
# 带计数的for循环, 如果你需要一个数值序列，内置函数 range() 会很方便，它生成一个等差数列（并不是列表,是一个可迭代对象)
for x in range(5):
    print(x)
print('range(5) is ', list(range(5)))  # range(5) is  [0, 1, 2, 3, 4]
# 我们可以在循环后面使用可选的 else 语句。它将会在循环完毕后执行，除非有 break 语句终止了循环。
for i in range(0, 5):
    print(i)
else:
    print("Bye bye")
for i in range(0, 5):
    if i > 3:
        break
    print(i)
else:
    print("Bye bye")




