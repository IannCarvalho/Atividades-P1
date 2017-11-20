# coding: utf-8
# Fli Flai
# Iann Carvalho, 2016 / Programação1

# Entrada
ent1=int(raw_input())
ent2=int(raw_input())
ent3=int(raw_input())

#calculo
rest2=ent1%2
rest3=ent2%3
rest5=ent3%5
rest101=ent1%10
rest102=ent2%10
rest103=ent3%10

#condições
if rest101==0 or rest102==0 or rest103==0:
	print "Tumba"
else:
	if rest2==0:
		print "Fli"
	if rest3==0:
		print "Flai"	
	if rest5==0:
		print "Flu"
