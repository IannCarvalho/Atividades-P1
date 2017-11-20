# coding: utf-8
# Série: Substitui terminados em 7 ou divisíveis por 7
# Iann Carvalho, 2016 / Programação1

for i in range (1, 102, 2):
	if i%7==0 or i%10==7:
		print "*"
	else:
		print i
