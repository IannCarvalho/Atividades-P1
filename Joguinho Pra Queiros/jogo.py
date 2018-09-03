# coding: utf-8

import random

while True:
	letra=(random.choice(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']))
	acumulador=0
	while True:
		escolha = (raw_input())
		if escolha == letra:
			print "%s é correto." % escolha
			acumulador += 1
			print "Você acertou em %d tentativas" % acumulador
			break
		else:
			print "%s é incorreto." % escolha
			acumulador += 1
	while True:		
		opcao = (raw_input('Quer jogar novamente (s/n):'))
		if opcao == 'n':
			break
		elif opcao == 's':
			break
	if opcao=='n':
		break
