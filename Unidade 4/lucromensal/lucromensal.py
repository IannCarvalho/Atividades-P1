# coding: utf-8
# Lucro Mensal de uma Empresa
# Iann Carvalho, 2016 / Prog1

vazio = ""
l = []
for i in range (0, 12, 1):
	entrada = raw_input()
	for i in range (len(entrada)):
		if entrada[i] != " ":
			vazio = vazio + entrada[i]
		else:
			l.append(vazio)
			vazio = ""
	l.append(vazio)
	vazio=""

for i in range(0, len(l), 2):
	primeiro = float(l[i])
	segundo = float(l[i+1])
	resultado = primeiro - segundo
	if resultado >= 0:
		resultado = str(resultado)
		resultado = " " + resultado
	print resultado
