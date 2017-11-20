# coding: utf-8
# Custo Empregado
# Iann Carvalho, 2016 / Programação1

# Entrada
salario=float(raw_input())
dias=int(raw_input())
custo=float(raw_input())

#custos
custo_transporte=custo*dias
custo_empregador=(0.08*salario)+(0.12*salario) + salario
excesso=(custo_transporte-(0.06*salario))

#printagem
print "O salário base é R$ %.2f" % salario

#condicao
if custo_transporte>(0.06*salario):
	custo_empregador = custo_empregador + excesso
	print "O custo mensal para o empregador é de R$ %.2f" % custo_empregador
	if salario<=1317.07:
		salario_liquido=salario - (0.08*salario) - (0.06*salario)
		print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % salario_liquido
	elif 1317.07<salario<=2195.12:
		salario_liquido=salario - (0.09*salario) - (0.06*salario)
		print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % salario_liquido
	else:
		salario_liquido=salario - (0.11*salario) - (0.06*salario)
		print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % salario_liquido
else:
	custo_empregador = custo_empregador
	print "O custo mensal para o empregador é de R$ %.2f" % custo_empregador
	if salario<=1317.07:
		salario_liquido=salario - (0.08*salario)
		print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % salario_liquido
	elif 1317.07<salario<=2195.12:
		salario_liquido=salario - (0.09*salario)
		print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % salario_liquido
	else:
		salario_liquido=salario - (0.11*salario)
		print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" % salario_liquido

