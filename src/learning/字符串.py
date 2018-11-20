# 按照原来的格式输出，可以使用"""或'''
print("""
Usage: thingy [OPTIONS]
    -h                        Display this usage message
    -H hostname               Hostname to connect to
 """)

# 读取文件中的内容并把其中的数字提取出来
import os
print(os.getcwd())

s = open('C:\\Users\\xiongzhao\\jd\\python-lesson\\src\\resources\\string.txt')
print('原始内容:', s)
num = ''
for c in s:
    if c.isdigit():
        num += c
print('过滤后：', num)