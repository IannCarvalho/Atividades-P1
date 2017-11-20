# coding: utf-8
# Classifica Letra como Vogal ou Consoante
# Iann Carvalho, 2016 / Programação1

#Entrada
palavra=raw_input()

for indice in range(len(palavra)):
	if palavra[indice]=="a" or palavra[indice]=="A":
		print "<%s> sim" %(palavra[indice])
	elif palavra[indice]=="e" or palavra[indice]=="E":
		print "<%s> sim" %(palavra[indice])
	elif palavra[indice]=="i" or palavra[indice]=="I":
		print "<%s> sim" %(palavra[indice])
	elif palavra[indice]=="o" or palavra[indice]=="O":
		print "<%s> sim" %(palavra[indice])
	elif palavra[indice]=="u" or palavra[indice]=="U":
		print "<%s> sim" %(palavra[indice])
	else:
		print "<%s> nao" %(palavra[indice])
