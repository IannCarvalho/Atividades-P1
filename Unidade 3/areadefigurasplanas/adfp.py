# coding: utf-8
# Custo Empregado
# Iann Carvalho, 2016 / Programação1

import math

# Entrada
tipo=(raw_input())

if tipo=="círculo" or tipo=="quadrado":
	raio_ou_lado=float(raw_input())
	if tipo=="círculo":
		a = math.pi * (raio_ou_lado)**2
		print "Área do %s: %.2f (cm2)" % (tipo, a)
	else:
		a = raio_ou_lado**2
		print "Área do %s: %.2f (cm2)" % (tipo, a)
elif tipo=="retângulo" or tipo=="triângulo":
	base=float(raw_input())
	altura=float(raw_input())
	if tipo=="triângulo":
		a = (base * altura)/2
		print "Área do %s: %.2f (cm2)" % (tipo, a)
	else:
		a = base * altura
		print "Área do %s: %.2f (cm2)" % (tipo, a)
else:
	print "Figura plana inválida"
