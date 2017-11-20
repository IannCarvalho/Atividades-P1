# coding: utf-8
# Tabela de Quadrados
# Iann Carvalho, 2016 / Prog1

x = int(raw_input())
y = int(raw_input())

if x > y:
	print "---"
else:
	for i in range(x, y+1, 1):
		print "%d %d" % (i, i**2)
