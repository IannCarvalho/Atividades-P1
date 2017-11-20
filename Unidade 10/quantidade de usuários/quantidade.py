# coding: utf-8
# Iann Carvalho / Prog1
# Quantidade de Usuários - Unidade 10

def quantidade_usuarios(cadastro):
	contador = 0
	for i in range(len(cadastro.values())):
		contador += len(cadastro.values()[i])
	if 9999 in (cadastro.keys()):
		contador -= 1
	return contador


