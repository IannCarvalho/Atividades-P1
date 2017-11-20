# coding: utf-8
# Criação de uma Nova Palavra
# Iann Carvalho, 2016 / Prog1

meta_geral=float(raw_input())

acumulador=0
contador=0
l=[]

for i in range(0, 6, 1):
	venda_individual=float(raw_input())
	acumulador = acumulador + venda_individual
	meta_individual = meta_geral / 6
	l.append(venda_individual)
	if venda_individual>=meta_individual:
		contador=contador+1
		
if contador==6:
	print "Total de vendas: R$ %.2f (meta atingida)" % acumulador
	print "----"
	print "Bonificação:"
	for i in range(len(l)):
		calculo = l[i] / 100.0
		print "Funcionário %d: R$ %.2f" % (i+1, calculo)
		
else:
	print "Total de vendas: R$ %.2f (meta não foi atingida)" % acumulador
	print "----"
