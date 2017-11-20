# coding: utf-8
# Ataque
# Iann Carvalho, 2016 / Programação1

# Entrada
num=int(raw_input())

#laço
total_gols=0
lgols=[]
ltime=[]
for indice in range(num):
	time=raw_input()
	ltime.append(time)
	gols=int(raw_input())
	lgols.append(gols)
	total_gols = float(total_gols + gols)

media_gols=total_gols/num

#maior=maior quantidade de gols e indice=indice do time que mais fez gols
maior = 0
lgoleadores = []
for indice in range(0, len(lgols), 1):
	if lgols[indice] > maior:
		maior = lgols[indice]
		lgoleadores.append(indice)
		
maior_gols=lgoleadores[-1]
print "Time(s) com melhor ataque (%d gol(s)):" % (maior)

for indice in range(len(lgols)):
	if lgols[indice] == maior:
		print ltime[indice]

print """
Média de gols marcados: %.1f""" % (media_gols)
