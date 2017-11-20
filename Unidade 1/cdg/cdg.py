# coding: utf-8
# Consumo de gasolina
# Iann Carvalho, 2016 / Programação1

#entrada
pi = float(raw_input())
li = float(raw_input())
pf = float(raw_input())
lf = float(raw_input())

#calculo
resul=( (pf - pi) / (li - lf) )

#printagem +calculo
print "%.1f" %resul
