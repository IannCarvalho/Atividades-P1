# coding: utf-8
# Classificação de Elementos Utilizando a Média dos Extremos
# Iann Carvalho, 2016 / prog1

num=int(raw_input())
l=[]

acumulador=0
for i in range(0, num, 1):
	num_da_vez=int(raw_input())
	l.append(num_da_vez)
	acumulador = acumulador + num_da_vez

maior=l[0]
menor=l[0]
for numero in l:
	if maior<numero:
		maior = numero
	elif menor>numero:
		menor = numero
		
media = (menor + maior) / 2.0

print "Menor número: %d" % menor
print "Maior número: %d" % maior
print "Média dos extremos: %.2f" % media

contador_maior=0
contador_menor=0
for numero in l:
	if numero>media:
		contador_maior = contador_maior + 1
	elif numero<media:
		contador_menor = contador_menor + 1
	else:
		continue
		
print "%d número(s) abaixo da média" % contador_menor
print "%d número(s) acima da média" % contador_maior
