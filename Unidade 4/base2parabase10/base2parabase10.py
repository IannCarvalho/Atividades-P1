# coding: utf-8
# Conversão de Número na Base 2 para a Base 10
# Iann Carvalho, 2016 / Prog1

binario=raw_input()

acumulador=0
for i in range(len(binario)):
	binario_da_vez = int(binario[i])
	multiplicando_da_vez=2**(len(binario)-1-i)
	resultado = binario_da_vez * multiplicando_da_vez	
	print "%s * %d = %d" % (binario[i], multiplicando_da_vez, resultado)
	acumulador = acumulador + resultado

print "%s(2) = %d(10)" %(binario, acumulador)
