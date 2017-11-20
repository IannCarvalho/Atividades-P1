# coding: utf-8
# Calcula Moldura
# Iann Carvalho, 2016 / Programação1

#entrada
alt = float(raw_input())
lar = float(raw_input())

#conversao
alt = alt / 100
lar = lar / 100

#calculo
cal = (2 * alt) + (2 * lar)
cal = cal * 120

#printagem
print "R$ %.1f" % cal
