# coding: utf-8
# Aprovados e Reprovados
# Iann Carvalho, 2016 / Prog1

numero_de_alunos=int(raw_input())

acumulador_reprovados=0
acumulador_aprovados=0
reprovados=0
aprovados=0
for i in range(numero_de_alunos):
	nota=float(raw_input())
	if nota >= 7:
		aprovados = aprovados + 1
		acumulador_aprovados += nota
	else:
		reprovados = reprovados + 1
		acumulador_reprovados += nota

if reprovados==0:
	print """Reprovados: 0
"""
else:
	media_reprovados = acumulador_reprovados / reprovados
	print "Reprovados: %d" % (reprovados)
	print """Média: %.1f
""" % (media_reprovados)

if aprovados==0:
	print "Aprovados: 0"
else:
	media_aprovados = acumulador_aprovados / aprovados
	print "Aprovados: %d" % (aprovados)
	print "Média: %.1f" % (media_aprovados)
	
