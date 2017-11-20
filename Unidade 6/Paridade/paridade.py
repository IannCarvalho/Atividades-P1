# coding: utf-8
# Paridade
# Iann Carvalho, 2016 / Programação1

while True:
	binario=raw_input()
	contador=0
	for i in range(len(binario)-1):
		if binario[i] == '1':
			contador += 1
	chave=0
	if contador % 2 == 0 or contador == 0:
		if binario[-1] == '1':
			print "ERRO"
			chave += 1
	else:
		if binario[-1] == '0':
			print "ERRO"
			chave += 1
	if chave==1:
		break
