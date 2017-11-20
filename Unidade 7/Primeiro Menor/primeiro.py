# coding: utf-8
# Primeiro Menor
# Iann Carvalho, 2016 / Programação1

def main():
	entrada = raw_input().split()
	num = int(raw_input())
	resultado = primeiro_menor(num,entrada)



	if resultado == -1:
		print "sem menores que %d" % num
	else:
		print "primeiro menor que %d: %s" % (num,entrada[resultado])
	
def primeiro_menor(num,seq):
	for i in range(len(seq)):
		if int(seq[i]) < num:
			return i
	return -1

if __name__ == '__main__':
    main()
