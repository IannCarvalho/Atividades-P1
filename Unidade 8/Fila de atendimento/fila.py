# coding: utf-8
# Iann Carvalho / Prog1
# Fila de Atendimento de Pacientes - Unidade 8

def filas_de_atendimento(fila_unica, n):
	l=[]
	for i in range(n):
		l.append([])

	# MED SÓ PODE CHEGAR ATÉ N - 1
	med = 0
	for i in range(len(fila_unica)):
		if n > med:
			l[med].append(fila_unica[i])
			med += 1
		else:
			med = 0
			l[med].append(fila_unica[i])
			med += 1
		
	return l
	
fila_1 = ['Andre', 'Antonio', 'Bianca', 'Carlos', 'Claudia']
assert filas_de_atendimento(fila_1, 3) == [['Andre','Carlos'],['Antonio', 'Claudia'], ['Bianca']]

fila_2 = ['Andre', 'Antonio', 'Bianca', 'Carlos']
assert filas_de_atendimento(fila_2, 2) == [['Andre','Bianca'],['Antonio', 'Carlos']]
