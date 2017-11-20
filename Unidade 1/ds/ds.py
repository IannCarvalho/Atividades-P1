# coding: utf-8
# Divisão da Safra
# Iann Carvalho, 2016 / Programação1

#entrada
qso = int(raw_input())
qca = int(raw_input())
qcv = int(raw_input())

#calculo
rca = qso / qca
rcv = (qso % qca) / float(qcv)

#printagem
print "Clientes no atacado = %dkg cada." % rca
print "Clientes no varejo = %.2fkg cada." % rcv
