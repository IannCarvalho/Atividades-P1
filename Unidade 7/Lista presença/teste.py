# coding: utf-8
# Dígitos de Verificação do CPF
# Iann Carvalho, 2016 / Programação1

def cria_lista_presenca(turmas, nomes, turma):
	presenca=[]
	for i in range(len(turmas)):
		if turmas[i]==turma:
			presenca.append(nomes[i])
	return presenca

