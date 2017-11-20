# coding: utf-8
# Autorização voos
# Iann Carvalho, 2016 / prog1

aviao=int(raw_input())

sequencia=int(raw_input())

contador=0

for i in range(0, sequencia, 1):
	numero_da_vez = int(raw_input())
	if numero_da_vez <= aviao:
		contador = contador + 1
	else:
		continue
		
print "%d voo(s) autorizados." % contador
