'''
Created on 2016年11月14日

@author: Administrator
'''
counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串
print (counter)
print (miles)
print (name)

a = b = c = 1
print(a,b,c)
print(type(a), type(b), type(c))

a, b, c = 1, 2+3j, "runoob"
print(a,b,c)
print(type(a), type(b), type(c))

# Python3 中有六个标准的数据类型：
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Sets（集合）
# Dictionary（字典）

# Python3 支持 int、float、bool、complex（复数）。
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

# 数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。
print(22/5)
print(22//5)

# 字符串的截取的语法格式如下：
# 变量[头下标:尾下标]
str = 'running'
print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个个到倒数第二个的所有字符
print (str[0] * 6)       # 重复6次输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次
print (str + "TEST") # 连接字符串


