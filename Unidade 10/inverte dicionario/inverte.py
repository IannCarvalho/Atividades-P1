# coding: utf-8
# Iann Carvalho / Prog1
# Inverte Dicionário - Unidade 10

def inverte_dicionario(dicionario):
	novo = {}
	for k in dicionario.keys():
		if dicionario[k] in novo.keys():
			novo[dicionario[k]] += k
			for i in range(len(novo[dicionario[k]])-1,0,-1):
				if novo[dicionario[k]][i] < novo[dicionario[k]][i-1]:
					novo[dicionario[k]][i], novo[dicionario[k]][i-1] = novo[dicionario[k]][i-1],novo[dicionario[k]][i]
		else:
			novo[dicionario[k]] = [k]
	return novo   

def test_exemplo(self):
    m = {"a": 2, "b": 3, "c": 2}
    assert inverte_dicionario(m) == {
      2: ["a", "c"],
      3: ["b"]
    }
