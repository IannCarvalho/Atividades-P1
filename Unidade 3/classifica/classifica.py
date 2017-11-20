# coding: utf-8
# Classifica Corredor
# Iann Carvalho, 2016 / Programação1

#entrada
kilometro = float(raw_input())
tempo = float(raw_input())

#calculos media
media=kilometro/tempo

#condições
if media<10:
	print "Velocidade: %.1fkm/h. Corredor amador." % media
elif media>15:
	print "Velocidade: %.1fkm/h. Corredor profissional." % media
else:
	print "Velocidade: %.1fkm/h. Corredor aspirante." % media
