y = 0
conta = 0
repetido = False

for i in range(len(str1)):
    if str1[i] == str2[y]:
        conta += 1
        y += 1
    else:
        conta = 0
        y = 0
    if y == len(str2):
        return True
				
return False
