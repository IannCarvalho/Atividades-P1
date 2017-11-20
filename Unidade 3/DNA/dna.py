# coding: utf-8
# DNA
# Iann Carvalho, 2016 / Programação1

#entrada
dna1=raw_input()
dna2=raw_input()
dna3=raw_input()

c_dna1=len(dna1)
c_dna2=len(dna2)
c_dna3=len(dna3)

if c_dna1<=c_dna2 and c_dna1<=c_dna3:
	print "%s %d" % (dna1, c_dna1)
elif c_dna2<=c_dna3 and c_dna2<c_dna1:
	print "%s %d" % (dna2, c_dna2)
else:
	print "%s %d" % (dna3, c_dna3)
