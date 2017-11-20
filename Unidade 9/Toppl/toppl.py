# coding: utf-8
# Iann Carvalho / Prog1
# Toppl - Unidade 9

def filtra_alunos(alunos, inscritos, n):
	contador = 0
	for i in range(len(alunos)-1, -1, -1):
		if alunos[i][0] not in inscritos:
			contador += 1
			alunos.pop(i) 
		elif alunos[i][1] <= n:
			contador += 1
			alunos.pop(i)
			
	return contador
	
inscritos = [121, 123, 124]
alunos = [ (120,8.0), (121,7.5), (122,5.0), (123,6.0), (124,9.0), (125,4.0) ]
assert filtra_alunos(alunos, inscritos, 7.0) == 4
assert alunos == [ (121,7.5), (124,9.0) ]
