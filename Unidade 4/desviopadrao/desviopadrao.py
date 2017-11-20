# coding: utf-8
# Desvio Padrão
# Iann Barbosa / prog1

sequencia1 = raw_input()
sequencia2 = raw_input()
# Implementando o split
lista_seq1 = []
lista_seq2 = []
da_vez1 = ''
da_vez2 = ''
for i in range(len(sequencia1)):
	if sequencia1[i] != ' ':
		da_vez1 += sequencia1[i]
	else:
		lista_seq1.append(da_vez1)
		da_vez1 = ''
for i in range(len(sequencia2)):
	if sequencia2[i] != ' ':
		da_vez2 += sequencia2[i]
	else:
		lista_seq2.append(da_vez2)
		da_vez2 = ''
lista_seq1.append(da_vez1)
lista_seq2.append(da_vez2)
# Começando de fato o programa
soma_seq1 = 0
soma_seq2 = 0
for i in range(len(lista_seq1)):
	soma_seq1 += float(lista_seq1[i])
for i in range(len(lista_seq2)):
	soma_seq2 += float(lista_seq2[i])

media_seq1 = float(soma_seq1) / len(lista_seq1)
media_seq2 = float(soma_seq2) / len(lista_seq2)

difvalor1_lista = []
difvalor2_lista = []
for i in range(len(lista_seq1)):
	difvalor = (float(lista_seq1[i]) - media_seq1)**2
	difvalor1_lista.append(difvalor)
for i in range(len(lista_seq2)):
	difvalor1 = (float(lista_seq2[i]) - media_seq2) ** 2
	difvalor2_lista.append(difvalor1)
soma_dif1 = 0
soma_dif2 = 0
for i in range(len(difvalor1_lista)):
	soma_dif1 += difvalor1_lista[i]
for i in range(len(difvalor2_lista)):
	soma_dif2 += difvalor2_lista[i]

final1 = (soma_dif1/(len(lista_seq1) - 1))**(0.5)
final2 = (soma_dif2/ (len(lista_seq2)-1))**(0.5)

if final1 > final2:
	print "A sequência 1 possui o maior desvio padrão (%.2f)." % final1
elif final1 == final2:
	print "As sequências possuem o mesmo desvio padrão (%.2f)." % (final1)
else:
	print "A sequência 2 possui o maior desvio padrão (%.2f)." % (final2)
		
