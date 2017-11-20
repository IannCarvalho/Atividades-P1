# coding: utf-8
# Calcula ingressos do cinema
# Iann Carvalho, 2016 / Programação1

#entrada
adu = int(raw_input())
cri = int(raw_input())
ing = float(raw_input())

#calculo
tot = float((cri * ( ing / 2 )) + (adu * ing))

#saida
print "Total: R$", tot
