# coding: utf-8
# Sequencia Invertida 3 a 3
# Iann Carvalho, 2016 / Programação1

def inverte3a3(s):
	l=[]
	vazio=""
	for i in range(len(s)):
		if i%3!=0 or i==0:
			vazio += s[i]
		else:
			l.append(vazio)
			vazio = s[i]
	l.append(vazio)
	
	concatenador=""
	
	for i in range(len(l)-1, -1, -1):
		concatenador += l[i]

	return concatenador
	
assert inverte3a3("paisimtio") == "tiosimpai"
