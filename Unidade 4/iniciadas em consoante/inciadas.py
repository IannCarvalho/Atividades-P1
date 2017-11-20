# coding: utf-8
# Iniciadas por consoantes
# Iann Carvalho, 2016 / Programação1

#entrada
num=int(raw_input())

contador = 0

for indice in range(0, num, 1):
	palavra=raw_input()
	if palavra[0]=="a" or palavra[0]=="A":
		continue
	elif palavra[0]=="e" or palavra[0]=="E":
		continue
	elif palavra[0]=="i" or palavra[0]=="I":
		continue
	elif palavra[0]=="o" or palavra[0]=="O":
		continue
	elif palavra[0]=="u" or palavra[0]=="U":
		continue
	else:
		contador = contador + 1

num = float(num)
porcentagem = (contador / num) * 100
simbolo_porcentagem="%"

print "total de palavras: %d" % num
print "iniciadas por consoantes: %d (%.2f%s)" % (contador, porcentagem, simbolo_porcentagem)

