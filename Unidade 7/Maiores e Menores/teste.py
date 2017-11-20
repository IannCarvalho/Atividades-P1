# coding: utf-8
# Maiores e Menores
# Iann Carvalho, 2016 / Programação1

pivot=int(raw_input())
maiores=[]
menores=[]
while True:
	numeros=int(raw_input())
	if numeros<0:
		break
	elif numeros>pivot:
		maiores.append(numeros)
	else:
		menores.append(numeros)
		
print menores
print pivot
print maiores
	

			
			
