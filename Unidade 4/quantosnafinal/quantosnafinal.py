# coding: utf-8
# Quantos na Final?
# Iann Carvalho, 2016 / Prog1

numero = int(raw_input())

acumulador=0
alunos_na_final=0

for i in range(numero):
	nota = float(raw_input())
	if 4<=nota<7:
		alunos_na_final = alunos_na_final + 1
		acumulador = acumulador + nota



if alunos_na_final>0:
	media = acumulador / alunos_na_final
	percentagem = ((alunos_na_final * 100) / numero)
	sinal="%"
	print "%d (%.1f%s) alunos na final" % ( alunos_na_final , percentagem, sinal )
	print "Média das notas: %.1f" % (media)
else:
	print "0 (0.0%) alunos na final"
