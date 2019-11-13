#!/usr/bin/python
# -*- coding: UTF-8 -*-

for i in range(10,100):
	for n in range(2,i):
		if i%n == 0:
			j=i/n
			print('%d = %d*%d')%(i,j,n)
			break
	else:
		print('%d是一个质数')%(i)