# 列表操作
a = [23, 45, 1, -3434, 45, 43624356, 234]
# 末尾添加元素
a.append(88)
print(a)
# 指定位置添加元素
a.insert(1, 18)
print(a)
# 获取列表中某个元素的数量
print('45 in a counts: ', a.count(45))
# 移除某个元素,只移除匹配到的第一个元素
a.remove(45)
print('remove 45:', a)
# 反转列表
a.reverse()
print("反转列表: ", a)
# 向a中添加b的所有元素
b = [45, 56, 90]
a.extend(b)  # 等价于 a += b
print('向a中添加b的所有元素: ', a)
b = [45, 56, 90]
# 使用del关键字删除指定位置的列表元素
del a[0]
print('del a[0], a is ', a)

# 列表>>>栈(后进先出)
a = [1, 2, 3]
a.pop()
print('a.pop() is ', a)
# 列表>>>队列(先进先出)
a = [1, 2, 3]
a.pop(0)
print('a.pop(0) is ', a)

# 列表推导式
# 列表推导式由包含一个表达式的中括号组成，表达式后面跟随一个 for 子句，
# 之后可以有零或多个 for 或 if 子句。结果是一个列表，
# 由表达式依据其后面的 for 和 if 子句上下文计算而来的结果构成。
squares = [x**2 for x in range(10)]
print('squares is ', squares)
a = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print('a =', a)  # a = [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# 元组, 元组不可变，不能对元素进行添加、修改和删除
a = 'Fedora', 'ShiYanLou', 'Kubuntu', 'Pardus'
print('a =', a)  # a = ('Fedora', 'ShiYanLou', 'Kubuntu', 'Pardus')
print('元组也可以a[1]: ', a[1])
# 创建只有一个元素的元组，只需要在末尾加逗号
a = 'abc',
print('a = ', a)

# 集合，集合无序，基本功能包括关系测试和消除重复元素
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# 空集合,不能使用{},这个是字典
emptySet = set()
# 演示对两个单词中的字母进行集合操作
a = set('abracadabra')
b = set('alacazam')
# >>>a                                  # a 去重后的字母
{'a', 'r', 'b', 'c', 'd'}
# >>>a - b                              # a 有而 b 没有的字母
{'r', 'd', 'b'}
# >>>a | b                              # 存在于 a 或 b 的字母
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
# >>>a & b                              # a 和 b 都有的字母
{'a', 'c'}
# >>>a ^ b                              # 存在于 a 或 b 但不同时存在的字母
{'r', 'd', 'b', 'm', 'z', 'l'}

# 字典，类似java map
data = {'kushal': 'Fedora', 'kart_': 'Debian', 'Jace': 'Mac'}
# 空字典
map = {}
# 元组转map
map2 = dict((('Indian', 'Delhi'), ('Bangladesh', 'Dhaka')))
# 字典添加键值对
data['parthan'] = 'Ubuntu'
# 获取value
# 如果key不存在会报错，建议用get的方式,并且如果不存在可以指定默认值
print("data['Jace'] =", data['Jace'])
print("data.get('Jace') =", data.get('aaaa'))
print("data.get('Jace') =", data.get('aaaa', 0))
# 删除元素
del data['kushal']
# 判断字典是否包含key
'xiong' in data
# 遍历
for x, y in data.items():
    print('{} use {}'.format(x, y))

# 遍历列表的时候获取索引值
for i, j in enumerate(['a', 'b', 'c']):
    print(i, j)
for i, j in enumerate({'a', 'b', 'c'}):
    print(i, j)
# 同时遍历多个序列类型，你可以使用 zip() 函数
a = ['Pradeepto', 'Kushal']
b = ['OpenSUSE', 'Fedora']
c = ['java', 'python']
for x, y, z in zip(a, b, c):
    print("{} uses {} language {}".format(x, y, z))

# 练习题，要求输入学生数量，以及各个学生物理、数学、历史三科的成绩，
# 如果总成绩小于 120，程序打印 “failed”，否则打印 “passed”。
n = int(input("Enter the number of students: "))
data = {}  # 用来存储数据的字典变量
Subjects = ('Physics', 'Maths', 'History')  # 所有科目
for i in range(0, n):
    name = input('Enter the name of the student {}: '.format(i + 1))  # 获得学生名称
    marks = []
    for x in Subjects:
        marks.append(int(input('Enter marks of {}: '.format(x))))  # 获得每一科的分数
    data[name] = marks
for x, y in data.items():
    print('{} score is {}'.format(x, y))
    total = sum(y)
    print("{}'s total marks {}".format(x, total))
    if total < 120:
        print(x, "failed :(")
    else:
        print(x, "passed :)")

# 计算两个矩阵的 Hadamard 乘积。要求输入矩阵的行/列数（在这里假设我们使用的是 n × n 的矩阵）
# 这里我们使用了几次列表推导式。[int(x) for x in input().split()]
# 首先通过 input() 获得用户输入的字符串，再使用 split() 分割字符串得到一系列的数字字符串，
# 然后用 int() 从每个数字字符串创建对应的整数值。
# 我们也使用了 [a[i][j] * b[j][i] for j in range(n)] 来得到矩阵乘积的每一行数据。
n = int(input("Enter the value of n: "))
print("Enter values for the Matrix A")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print("Enter values for the Matrix B")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j] * b[i][j] for j in range(n)])
print("After matrix multiplication")
print("-" * 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5), end=' ')
    print()
print("-" * 7 * n)