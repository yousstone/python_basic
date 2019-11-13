#!/usr/bin/python
# -*- coding: UTF-8 -*-

for i in range(1,10):
	for j in range(11,20):
		if j== 18:
			continue
		else:
			print(i,j)
	print(i)
