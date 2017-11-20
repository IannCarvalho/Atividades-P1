# coding: utf-8
# Iann Carvalho / Prog1
# Labir Move Direita - Unidade 9


def move_direita(labirinto):
	for i in range(len(labirinto)):
		for y in range(len(labirinto[i])):
			if labirinto[i][y] == '*':
				lugar = (i, y)
				if y != len(labirinto[0])-1:
					if labirinto[i][y+1] == ' ':
						labirinto[i][y], labirinto[i][y+1] = labirinto[i][y+1], labirinto[i][y]
						lugar = (i, y+1)
						break
	return lugar

labirinto1 = [
  ['P', '*', ' ', ' '],
  ['P', ' ', 'P', ' '],
  ['P', 'P', 'P', ' '],
]

assert move_direita(labirinto1) == (0, 2)

assert labirinto1 ==  [
  ['P', ' ', '*', ' '],
  ['P', ' ', 'P', ' '],
  ['P', 'P', 'P', ' '],
]

labirinto2 = [
  ['P', 'P', ' ', ' '],
  ['P', '*', 'P', ' '],
  ['P', 'P', 'P', ' '],
]
assert move_direita(labirinto2) == (1, 1)

