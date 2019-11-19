#!/usr/bin/python
# -*- coding: UTF-8 -*-

# shuffle() 方法将序列的所有元素随机排序。


import random
list = range(10)
random.shuffle(list)
print(list)


# randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1

n1 = random.choice(range(1,101))
print("1-100的随机整数实现方式之一：%d") % n1

n2 = random.randrange(1,101)
print("1-100的随机整数实现方式之二：%d") % n2

