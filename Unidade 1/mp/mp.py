# coding: utf-8
nota1 = float(raw_input())
if nota1>10:
	print "Nota maior que 10"
	nota1 = float(raw_input())
nota2 = float(raw_input())
if nota2>10:
	print "Nota maior que 10"
	nota2 = float(raw_input())
nota3 = float(raw_input())
if nota3>10:
	print "Nota maior que 10"
	nota3 = float(raw_input())
peso1 = float(raw_input())
if peso1>100:
	print "Peso maior que 100"
	peso1 = float(raw_input())
peso2 = float(raw_input())
if peso2>100:
	print "Peso maior que 100"
	peso2 = float(raw_input())

peso1 = float(peso1) / 100
peso2 = float(peso2) / 100
peso3 = 1 - (peso2 + peso1)

mediafinal = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)

print "Média Final: %.1f" % mediafinal
