#coding: utf-8
# Aprovação Unidades
# Iann Carvalho, 2016 / Programação1

unidade = int(raw_input('Unidade? '))
media = float(raw_input('Média de aprovação na unidade? '))
proxima_unidade = unidade + 1
print("""
O aluno vai para a unidade %d com média %.1f.""") % (proxima_unidade,media)
