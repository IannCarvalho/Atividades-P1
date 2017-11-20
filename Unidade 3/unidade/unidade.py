# coding: utf-8
# Unidade P1
# Iann Carvalho, 2016 / Programação1

#entrada
ultimo_mini=float(raw_input())
quantidade_mini=int(raw_input())

if quantidade_mini>1:
	media=float(raw_input())
	media_final=(ultimo_mini * 0.6) + (media * 0.4)
	if media_final>=6:
		print "%.1f. Aprovado."  % media_final
	else:
		print "%.1f. Ainda não aprovado."  % media_final
elif quantidade_mini==0:
	print "Ainda não fez prova"	
else:
	print "%.1f. Ainda não aprovado."  % ultimo_mini
	
