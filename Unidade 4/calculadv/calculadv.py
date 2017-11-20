# coding: utf-8
# Calcula DV
# Iann Carvalho, 2016 / prog1

num=raw_input()

acumulador_impares=0
limpares=[]
lpares=[]
acumulador_pares=0

#pares
for i in range (0, len(num), 2):
	numero_da_vez=int(num[i])
	acumulador_pares = acumulador_pares + numero_da_vez

#impares
for i in range (1, len(num), 2):
	numero_da_vez=int(num[i])
	acumulador_impares = acumulador_impares + numero_da_vez

resto = str((acumulador_impares * acumulador_pares) % 11)

if resto=="10":
	resto="X"

print "%s-%s" % (num, resto)
