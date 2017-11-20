# coding: utf-8
# Palíndromo!
# Iann Carvalho, 2016 / Programação1

#entrada
num=int(raw_input())

l=[]
acumulador=0
contador=0
for indice in range(0, num, 1):
	numero_da_vez=int(raw_input())
	l.append(numero_da_vez)
	if numero_da_vez % 2 == 0:
		acumulador = acumulador + numero_da_vez
		contador = contador + 1
	
media = float(acumulador) / contador

print "soma: %d" % acumulador
print "média: %.1f" % media

contador_media=0
for indice in range(0, len(l), 1):
	if media>l[indice]:
		contador_media = contador_media + 1
	else:
		continue

print "%d número(s) abaixo da média" % contador_media
	
	
