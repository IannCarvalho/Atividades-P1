# coding: utf-8
# Dígitos de Verificação do CPF
# Iann Carvalho, 2016 / Programação1

def calcula_digitos_verificacao(string):
	numero = 1
	acumulador = 0
	for i in range(len(string)-1, -1, -1):
		numero += 1
		resultado = int(string[i]) * numero
		acumulador += resultado

	algarismo1 = str(10*(acumulador) % 11)
	if algarismo1 == '10':
		algarismo1 = '0'
	string = string + algarismo1
	numero = 1
	acumulador = 0
	for i in range(len(string)-1, -1, -1):
		numero += 1
		resultado = int(string[i]) * numero
		acumulador += resultado
		
	algarismo2 = str(10*(acumulador) % 11)
	if algarismo2 == '10':
		algarismo2 = '0'
	final = algarismo1 + algarismo2
	return final


	
	
	
