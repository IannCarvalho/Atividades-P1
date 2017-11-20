# coding: utf-8
# Defensivos
# Iann Carvalho, 2016 / Programação1

##Fungi é 0.02l/h, herbi é 0.3l/h e inset 0,083333333l/h
##fungi é 1=320, herbi 1=100 e inset 1=160

import math

# Entrada
produto=(raw_input())
area=int(raw_input())

#definições
quantidade_fungi=math.ceil( (area * 1.0 ) / 50 )
quantidade_herbi=math.ceil( (0.3*area) / 1) 
quantidade_inset=math.ceil( (2.5 * area) / 30)
preco_fungi= quantidade_fungi * 320
preco_herbi= quantidade_herbi * 100
preco_inset= quantidade_inset * 160

#condicao
if produto=="Fungicida":
	print "%d Fungicida(s). %.2f reais." % (quantidade_fungi, preco_fungi)
elif produto=="Herbicida":
	print "%d Herbicida(s). %.2f reais." % (quantidade_herbi, preco_herbi)
elif produto=="Inseticida":
	print "%d Inseticida(s). %.2f reais." % (quantidade_inset, preco_inset)
else:
	print "Produto não existente"
