# coding: utf-8
# Palíndromo!
# Iann Carvalho, 2016 / Programação1

#entrada
palavra=raw_input()
vazio=""
palavrajunta=""

for indice in range(0, len(palavra), 1):
	if palavra[indice]==" ":
		continue
	else:
		palavrajunta = palavrajunta + palavra[indice]

for indice in range(-1, -(len(palavra))-1, -1):
	if palavra[indice]==" ":
		continue
	else:
		vazio = vazio + palavra[indice]

if palavrajunta==vazio:
	print "%s é palíndromo" % palavra
else:
	print "%s não é palíndromo" % palavra
