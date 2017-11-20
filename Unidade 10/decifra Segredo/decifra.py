# coding: utf-8
# Iann Carvalho / Prog1
# Decifra Segredo - Unidade 10

def decifra(chave,mensagem):
	chaves = chave.keys()
	valores = chave.values()
	concatenador = ""

	for i in range(len(mensagem)):
		for y in range(len(chaves)):
			if mensagem[i] == chaves[y]:
				concatenador += valores[y]
			
	return concatenador

chave1={'@':'V','a':'v','n':'o','l':'i','#':' ','4':'a','+':'u'}
assert decifra( chave1, '+a4') == 'uva'
assert decifra(chave1, '@nan#al+#4#+a4') == 'Vovo viu a uva'

