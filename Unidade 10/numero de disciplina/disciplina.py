def numero_disciplinas(grade, horarios, lista):
	contador = 0
	for i in range(len(grade.values())):
		if grade.values()[i] == lista:
			contador += 1
	return contador

grade = {"p1": [], "lp1": [], "ic": [],"calc1": [], "p2": ["ic", "p1", "lp1"],
"lp2": ["ic", "p1", "lp1"], "grafos": ["ic", "p1", "lp1"], "calc2"  : ["calc1"], 
"edados": ["ic", "p1", "lp1", "p2", "lp2", "grafos"],
"leda": ["ic", "p1", "lp1", "p2", "lp2", "grafos"]}

horarios= {"p1": "s082", "lp1": "x082", "ic": "i142", "calc1": "q082", "p2": "t162",
"lp2": "s082", "grafos": "q082", "calc2": "x162", "edados": "x162", "leda": "t102"}

assert numero_disciplinas(grade, horarios, []) == 4
assert numero_disciplinas(grade, horarios, ["ic", "p1", "lp1"]) == 3
