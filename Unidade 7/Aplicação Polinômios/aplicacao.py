# coding: utf-8
# Aplicação Polinômios
# Iann Carvalho, 2016 / Programação1

entrada = raw_input()
while not entrada == "fim":
	result = 0
	expoente = 0
	if entrada[0] == "p":
		print "novo polinomio"
		entrada = entrada.split()
		entrada = entrada[1:]
		for el in range(len(entrada)):
			entrada[el] = int(entrada[el])
			polinomio = entrada
	else:
		entrada = int(entrada)
		for ele in range(len(polinomio)):
			result += polinomio[ele] * (entrada ** expoente)
			expoente += 1
			
		print result


	entrada = raw_input()
	
 
