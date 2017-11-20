# coding: utf-8
# Criptografando uma Senha
# Iann Carvalho, 2016 / Programação1

#Entrada
palavra=raw_input()
contador=0
vazio=""
vazio = palavra[0] 

for indice in range(1, len(palavra), 1):
	if palavra[indice]=="a" or palavra[indice]=="A":
		letra_nova="4"
		letra_nova="4"
		contador= contador + 1
		vazio = vazio + letra_nova
	elif palavra[indice]=="e" or palavra[indice]=="E":
		letra_nova="3"
		letra_nova="3"
		contador= contador + 1
		vazio = vazio + letra_nova
	elif palavra[indice]=="i" or palavra[indice]=="I":
		letra_nova="1"
		letra_nova="1"
		contador= contador + 1
		vazio = vazio + letra_nova
	elif palavra[indice]=="o" or palavra[indice]=="O":
		letra_nova="0"
		letra_nova="0"
		contador= contador + 1
		vazio = vazio + letra_nova
	else:
		vazio = vazio + palavra[indice]

print "%s (%d troca(s))" % (vazio, contador)
