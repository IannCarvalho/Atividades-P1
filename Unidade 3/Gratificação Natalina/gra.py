# coding: utf-8
# Gratificação Natalina
# Iann Carvalho, 2016 / Programação1

codigo=int(raw_input())
if codigo==1:
	print "Deverá receber em dezembro R$ 25000.00."
elif codigo==2:
	print "Deverá receber em dezembro R$ 15000.00."
else:
	faltou=int(raw_input())
	if codigo==3:
		if faltou==0:
			print "Valor da gratificação R$ 500.00."
			print "Deverá receber em dezembro R$ 8500.00."
		else:
			G = (235 - faltou) * 2
			final=8000 + G
			print "Valor da gratificação R$ %.2f." % G
			print "Deverá receber em dezembro R$ %.2f." % final
	elif codigo==4:
		if faltou==0:
			print "Valor da gratificação R$ 300.00."
			print "Deverá receber em dezembro R$ 5300.00."
		else:
			G = (235 - faltou)
			final=5000 + G
			print "Valor da gratificação R$ %.2f." % G
			print "Deverá receber em dezembro R$ %.2f." % final
	else:
		if faltou==0:
			print "Valor da gratificação R$ 200.00."
			print "Deverá receber em dezembro R$ 3000.00."
		else:
			G = (235 - faltou) * 0.7
			final=2800 + G
			print "Valor da gratificação R$ %.2f." % G
			print "Deverá receber em dezembro R$ %.2f." % final
	
