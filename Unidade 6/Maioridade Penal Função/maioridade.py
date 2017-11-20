# coding: utf-8
# Maioridade Penal Função
# Iann Carvalho, 2016 / Programação1

def maioridade_penal(nome, idade):
	nome=nome.split()
	idade=idade.split()
	adultos=""
	for i in range(len(idade)):
		idade_da_vez = int(idade[i])
		if idade_da_vez >= 18:
			adultos += nome[i] + " "
	adultos = adultos[:-1]	
	return adultos
	
assert maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"
