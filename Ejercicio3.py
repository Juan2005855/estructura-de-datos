#Contar los elementos pares e impares de la lista[11, 20, 33, 44, 54, 74, 12, 6, 2, 10]
lista= [11, 20, 33, 44, 54, 74, 12, 6, 2, 10]
pares = 0
impares = 0
for i in range (len (lista)):
    if lista[i] % 2 == 0:
        pares += 1
    else:
        impares += 1
print ("La lista tiene ", pares, "elementos pares y", impares, "elementos impares")
print ("La listatiene", len(lista), "elementos")
