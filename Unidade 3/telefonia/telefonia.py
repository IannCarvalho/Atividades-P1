# coding: utf-8
# Telefonia
# Iann Carvalho, 2016 / Programação1

# Entrada
ent1=int(raw_input())

#calculo
taxa=1
resul3=(ent1*0.50)+1
divi=ent1/5
rest=ent1%5
resul5=(divi*3)+(rest*0.70)+1

#condições
if ent1<=3:
	print "R$ %.2f" % resul3
elif ent1>3:
	print "R$ %.2f" % resul5
