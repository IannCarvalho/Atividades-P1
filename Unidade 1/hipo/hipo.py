# coding: utf-8
# Hipotenusa
# Iann Carvalho, 2016 / Programação1

import math

#entrada
cat1 = float(raw_input("Medida do Cateto 1? "))
cat2 = float(raw_input("Medida do Cateto 2? "))

#calculo
hipo = math.sqrt((cat1**2) + (cat2**2))

#printagem
print "Medida da Hipotenusa: %.2f" % hipo
