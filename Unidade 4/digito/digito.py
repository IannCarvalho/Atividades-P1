# coding: utf-8
# Iann Carvalho, 2016 / prog1
# Dígito Verificador de Conta Bancária

numero=raw_input()

acumulador=0
for i in range(	len(numero)):
	inteiro=int(numero[i])
	acumulador=acumulador + inteiro

resto = acumulador % 11

if resto==10:
	resto="X"

print "%s-%s" % (numero, resto)

	
