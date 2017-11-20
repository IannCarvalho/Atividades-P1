# coding: utf-8
# Série: Sequencia de floats
# Iann Carvalho / prog1 2016

#entrada
ent1=(raw_input())

somatorio_finais=0
for i in range(len(ent1)):
    posicao=(ent1[i])
    exponencia=(8**(len(ent1)-i-1))
    posicao=int(posicao)
    resultado_final= posicao * exponencia
    somatorio_finais = somatorio_finais + resultado_final
    print "%s * 8^%s = %d " %(ent1[i], len(ent1)-i-1, resultado_final)
print "%s(8) = %d(10)" % (ent1, somatorio_finais)
