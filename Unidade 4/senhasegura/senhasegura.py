# coding: utf-8
# Produzindo uma Senha Segura
# Iann Carvalho, 2016 / Programação 1

#entrada
ent = raw_input()
acumulador_letras = ""

for i in range(0, len(ent), 1):
	if ent[i] == " ":
		acumulador_letras = acumulador_letras + ent[i]
	else:
		acumulador_letras = acumulador_letras + (2*(ent[i]))

print acumulador_letras

if len(acumulador_letras)>=13:
	print "senha segura"
else:
	print "senha insegura"
