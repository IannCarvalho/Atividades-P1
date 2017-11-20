# coding: utf-8
# Divisores Próprios
# Iann Carvalho, 2016 / Prog1

ano_inicial=int(raw_input())
ano_final=int(raw_input())
diferenca = (ano_final - ano_inicial) + 1

numero_maiores=0
acumulador_maiores=0
acumulador_menores=0
numero_menores=0
for i in range(0, diferenca, 1):
	salario=float(raw_input())
	if salario>100:
		acumulador_maiores += salario
		numero_maiores += 1
	else:
		acumulador_menores += salario
		numero_menores += 1

sinal="%"
if numero_menores>0:
	media_menores = acumulador_menores / numero_menores
	percentagem_menores = (100.0 * numero_menores) / diferenca
	print "%d ano(s) abaixo (%.0f%s dos anos)" % (numero_menores, percentagem_menores, sinal)
	print "média dos anos abaixo: U$ %.2f" %media_menores
else:
	print "0 ano(s) abaixo (0% dos anos)"
	
if numero_maiores>0:
	media_maiores = acumulador_maiores / numero_maiores
	percentagem_maiores = (100.0 * numero_maiores) / diferenca
	print "%d ano(s) acima (%.0f%s dos anos)" % (numero_maiores, percentagem_maiores, sinal)
	print "média dos anos acima: U$ %.2f" % (media_maiores)
else:
	print "0 ano(s) acima (0% dos anos)"
