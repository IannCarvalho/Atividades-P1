# coding: utf-8
# Único
# Iann Carvalho, 2016 / Programação1

def unico(string):
	nova_palavra=""
	if string != "":
		for i in range(len(string)-1):
			if string[i] != string[i+1]:
				nova_palavra += string[i]
		nova_palavra += string[-1]
	return nova_palavra

