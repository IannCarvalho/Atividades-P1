# coding: utf-8
# Maioridade Penal
# Iann Carvalho, 2016 / Prog1

num=int(raw_input())

for i in range(2, num, 1):
	if num%i==0:
		if i%2==0:
			print i
