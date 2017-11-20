# coding: utf-8
# Altera Vetor por Escalar
# Iann Carvalho, 2016 / Programação1

def is_substring(str1, str2):
	i = 0
	y = 0
	conta = 0
	repetido = False

	while i<len(str1):
		while y<(len(str2)):
			if str1[i] == str2[y]:
				conta += 1
				y += 1
				break
			else:
				conta = 0
				break
		i += 1
				
	if conta == len(str2):
		repetido = True

	return repetido
	
assert is_substring('boiada','oi')
assert not is_substring('casorio', 'casa')
