# coding: utf-8
# Espaço por Vírgula
# Iann Carvalho, 2016 / Programação1

#entrada
frase = raw_input()
num1 = int(raw_input())
num2 = int(raw_input())


for i in range (num1, num2, 1):
	if frase[i] == " ":
		print ",",
	else:		
		print frase[i],

	

