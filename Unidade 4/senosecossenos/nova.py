# coding: utf-8
# Senos e Cossenos
# Iann Carvalho, 2016 / Prog1

import math

inicial=float(raw_input())
progressao=float(raw_input())
num=int(raw_input())

print "|Angulo|   Seno|Cosseno|"
da_vez = inicial
for i in range(num):
	da_vez_str = str(da_vez)
	numero_espacos = 6 - len(da_vez_str)
	espacos = " " * numero_espacos
	ang = math.radians(da_vez)
	cos_da_vez = math.cos(ang)
	seno_da_vez = math.sin(ang)
	print "|%s%.1f|%.5f|%.5f|" % (espacos, da_vez, seno_da_vez, cos_da_vez)
	da_vez = da_vez + progressao
