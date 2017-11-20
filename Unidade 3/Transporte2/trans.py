# coding: utf-8
# Transporte Modificado
# Iann Carvalho, 2016 / Prog1

import math

#entrada
passa = float(raw_input())
reais = float(raw_input())

#calculos de custo
tav=100*passa
onibus=22*passa
taxi=200

#taxi
numero_de_taxis=math.ceil(passa/4.0)
if passa%numero_de_taxis!=0:
	numero_de_taxis = numero_de_taxis + 1
if passa > 4.0:
	taxi = 200 * numero_de_taxis
else:
	taxi = 200

#condições
if reais>=tav:
	print "TAV. R$ %.2f" % tav
elif reais>=taxi:
	print "Táxi. R$ %.2f" % taxi
elif reais>=onibus:
	print "Ônibus. R$ %.2f" % onibus
else:
	print "Não é possível realizar a viagem."


