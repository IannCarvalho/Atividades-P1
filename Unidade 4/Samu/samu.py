# coding: utf-8
# Atendimentos no SAMU
# Iann Carvalho, 2016 / Prog1

l=[]
acumulador = 0
for i in range(0, 12, 1):
	numero=int(raw_input())
	l.append(numero)
	acumulador = acumulador + numero
	
media = acumulador / 12.0

print "Média mensal de atendimentos: %.2f" % media
print "----"

for i in range(len(l)):
	if l[i] > media:
		print "Mês %d: %d" % (i+1, l[i])
