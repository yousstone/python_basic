#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 随着随机次数的增加
# 平均值越来越趋向于5.5
# 也就是(1+10)/2

import random
s1 = 0
s2 = 0
s3 = 0
s4 = 0
for i in range(1,10**1+1):
	p = random.choice(range(1,11))
	# print('从1到9中取个随机值,第一次是:%d') % p
	s1 += p
i1 = float(i)
print('1到10之间，取10次随机值之和是：%d，平均值是：%f') % (s1,s1/i1)

for j in range(1,10**3+1):
	p2 = random.choice(range(1,11))
	s2 += p2
j1=float(j)
print('1到10之间，取1000次随机值之和是：%d，平均值是：%f') % (s2,s2/j1)

for k in range(1,10**5+1):
	p3 = random.choice(range(1,11))
	s3 += p3
k1 = float(k)
print('1到10之间，取10万次随机值之和是：%d，平均值是：%f') % (s3,s3/k1)

# for g in range(1,10**7+1):
# 	p4 = random.choice(range(1,11))
# 	s4 += p4
# g1 = float(g)
# print('1到10之间，取1000万次随机值之和是：%d，平均值是：%f') % (s4,s4/g1)

f = 100 * random.random()
print("1-100的随机数是: %.2f") % round(f,2)
print("1-100的随机数是: %2f") % round(f,2)
# 比较下这两者的区别


