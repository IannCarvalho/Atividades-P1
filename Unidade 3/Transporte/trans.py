# coding: utf-8
# Hipotenusa
# Iann Carvalho, 2016 / Programação1

#entrada
passa = float(raw_input())
reais = float(raw_input())

#calculos media
media=reais/passa

#calculos de custo
tav=100*passa
onibus=22*passa

#condições
if media>=100:
	print "TAV. R$ %.2f" % tav
elif 50<=media<100 and passa==3 or passa==4:
	print "Táxi. R$ 200.00"
elif media>=22:
	print "Ônibus. R$ %.2f" % onibus
else:
	print "Não é possível realizar a viagem."
