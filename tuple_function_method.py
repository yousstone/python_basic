#!/usr/bin/python
# -*- coding: UTF-8 -*-

# https://www.runoob.com/python/python-tuples.html

# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合

tup1 = (12,34.56)
tup2 = ('abc','xyz')

tup3 = tup1 + tup2

print(tup3)

# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tup4 = (1,'zhejiang',3.14)
print(tup4)
del tup4
# print('after deleting tup4:')
# print(tup4)

# tupe元素的复制
for i in range(1,11):
    print(('hi',)*i)