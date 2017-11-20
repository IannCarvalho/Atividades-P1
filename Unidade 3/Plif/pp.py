# coding: utf-8
# Plif Plof
# Iann Carvalho, 2016 / Programação1

# Entrada
ent1=int(raw_input())
ent2=int(raw_input())
ent3=int(raw_input())

#calculo
soma=ent1+ent2+ent3
divi=soma%5
divi2=soma%3

#condições
if divi==0 and divi2==0:
	print "plifplof"
elif divi2==0:
	print "plif"
elif divi==0:
	print "plof"
else:
	print soma 
