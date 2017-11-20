# coding: utf-8
# CSF
# Iann Carvalho, 2016 / Programação1

#entrada
nota=float(raw_input())
credito=int(raw_input())

#20% de credito=83.2 , 90% de credito= 374.4

if nota>=600 and 84<=credito<=374:#classificado em tudo
	print "Todas as condições satisfeitas."
elif nota>=600:#classificado só no enem
	print "Condição CRÉDITOS não satisfeita."
elif 84<credito<375:#classificado só em credito
	print "Condição ENEM não satisfeita."
else:
	print "Nenhuma condição satisfeita."
