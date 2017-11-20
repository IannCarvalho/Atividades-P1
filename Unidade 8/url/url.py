# coding: utf-8
# Filtra URLs
# Iann Carvalho, 2016 / Programação1

def filtra_urls(l):
	l2=[]
	conta = 0
	y = 0
	base = 'google.com'
	google = False
	
	for url in l:
		for i in range(len(url)):
			while y<len(base):
				if url[i] == base[y]:
					y += 1
					conta += 1
					break
				else:
					conta = 0
					break
		if conta == len(base):
			l2.append(url)
	return l2
	
p1 = ['www.uol.com','www.google.com','http://mail.google.com']
assert filtra_urls(p1) == ['www.google.com','http://mail.google.com']
