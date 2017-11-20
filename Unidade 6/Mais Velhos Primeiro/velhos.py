# coding: utf-8
# Mais Velhos Primeiro
# Iann Carvalho, 2016 / Programação1

def idosos_inicio(fila):
	for i in range(len(fila)):
		if fila[i]>=60:
			for j in range(i):
				if fila[j]<60:
					fila[i], fila[j] = fila[j], fila[i]	
					break

fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
idosos_inicio(fila)
assert fila == [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]
