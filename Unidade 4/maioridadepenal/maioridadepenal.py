# coding: utf-8
# Maioridade Penal
# Iann Carvalho, 2016 / Prog1

###COLOCANDO NOMES EM LISTA
nomes=raw_input()
lnomes=[]
vazio=""
for i in range(len(nomes)):
	if nomes[i] == " ":
		lnomes.append(vazio)
		vazio=""
	else:
		vazio = vazio + nomes[i]
lnomes.append(vazio)

###COLOCANDO AS IDADES EM LISTA
idades=raw_input()
lidades=[]
vazio=""
for i in range(len(idades)):
	if idades[i] == " ":
		lidades.append(vazio)
		vazio=""
	else:
		vazio = vazio + idades[i]
	
lidades.append(vazio)

### VERIFICANDO IDADES
for i in range(len(lidades)):
	idade_da_vez=int(lidades[i])
	if idade_da_vez<18:
		continue
	else:
		print lnomes[i]



		
