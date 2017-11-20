# coding: utf-8
# Pré-vogais
# Iann Carvalho, 2016 / Programação1

def pre_vogais(palavra):
	palavra=palavra.lower()
	lista_vogais = ['a', 'e', 'i', 'o', 'u']
	l=[]
	for i in range(1, len(palavra)):
		for vogais in lista_vogais:
			if palavra[i]==vogais:
				if len(l)==0:
					l.append(palavra[i-1])
				else:
					contador=0
					for letras in l:
						if letras != palavra[i-1]:
							contador+=1
						if contador==len(l):
							l.append(palavra[i-1])
	return l
	

				
	
assert pre_vogais("Andrade") == ['r', 'd']
assert pre_vogais("exemplo") == ['x', 'l']
assert pre_vogais("hiaTO") == ['h', 'i', 't']
assert pre_vogais("Arara") == ['r']   
