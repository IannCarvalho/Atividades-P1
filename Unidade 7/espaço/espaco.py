# coding: utf-8
# Espaço em Disco 
# Iann Carvalho, 2016 / Programação1

def percentualUSO(lista,totalocupado):
	print "SPLab - Espaço utilizado pelos usuários"
	print "---------------------------------------------"
	print "Nr., Usuário, Espaço Utilizado, % do uso\n"
	for i in range(len(lista)):
		totalpessoa = lista[i][1]
		porcentagematual = (totalpessoa/totalocupado) * 100
		nome = lista[i][0]
		print "%d, %s, %.2f MB, %.2f%%" % (i+1,nome,totalpessoa,porcentagematual)
	
	print "\nEspaço total ocupado: %.2f MB" % totalocupado
	print "Espaço médio ocupado: %.2f MB" % (totalocupado/len(lista))
	


def conversaoBytes(numero):
	mb = int(numero)/1048576.0
	return mb

entrada = raw_input().split()
relatorio = []
totalocupado = 0
while entrada[0] != "fim":
	megabytes = conversaoBytes(entrada[1])
	relatorio.append((entrada[0],megabytes))
	totalocupado += megabytes
	entrada = raw_input().split()

percentualUSO(relatorio,totalocupado)
