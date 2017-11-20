# coding: utf-8
# Mais velho entre duas pessoas
# Iann Carvalho, 2016 / Programação1

# Entrada
nome1=(raw_input())
data1=int(raw_input())
mes1=int(raw_input())
ano1=int(raw_input())
nome2=(raw_input())
data2=int(raw_input())
mes2=int(raw_input())
ano2=int(raw_input())

#condicao
if ano1>ano2:
	print nome2
elif ano2>ano1:
	print nome1
else:
	if mes1>mes2:
		print nome2
	elif mes2>mes1:
		print nome1
	else:
		if data1>data2:
			print nome2
		elif data2>data1:
			print nome1
		else:
			print "nenhuma"
