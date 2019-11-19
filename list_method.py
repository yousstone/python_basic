#!/usr/bin/python
# -*- coding: UTF-8 -*-

# list的一些方法
# append, count ,extend, index, insert, pop,remove ,reverse, sort
# https://www.runoob.com/python/python-lists.html
li = range(7)
print('li:'),li

# 列表最后增加一个元素
li.append(7)
print('append之后的li:'),li


l2 = [1,2,3,4,5,2,3,4,3,5,6,7,3,4,2]
print('l2列表中有%d个2')%l2.count(2)



l3 = range(7)
l4 = range(7,11)
l3.extend(l4)
print('l3 extend l4:'),l3

print('l2的第一个2的索引是:%d')%l2.index(2)

l2.insert(5,100)
print('l2中在索引5处插入100:'),l2

print('l2删除最后一个元素:'),l2.pop()
print(l2)
print('l2删除索引为3的元素'),l2.pop(3)
print(l2)

l2.remove(2)

print('l2删除第一个匹配的2'),l2

l2.reverse()
print('l2反向排列'),l2



