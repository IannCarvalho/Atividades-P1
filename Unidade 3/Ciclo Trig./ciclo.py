# coding: utf-8
# Ciclo Trig.
# Iann Carvalho, 2016 / Programação1

# Entrada
angulo=float(raw_input())


#condicao
if 0>angulo>360:
	if angulo==0 or angulo==270 or angulo==180 or angulo==360 or angulo==90:
		print "Sobre eixos"
	elif 90>angulo>0:
		print "Quadrante 1"
	elif 180>angulo>90:
		print "Quadrante 2"
	elif 270>angulo>180:
		print "Quadrante 3"
	else:
		print "Quadrante 4"
else:
	angulo=angulo%360
	if angulo==0 or angulo==270 or angulo==180 or angulo==360 or angulo==90:
		print "Sobre eixos"
	elif 90>angulo>0:
		print "Quadrante 1"
	elif 180>angulo>90:
		print "Quadrante 2"
	elif 270>angulo>180:
		print "Quadrante 3"
	else:
		print "Quadrante 4"
