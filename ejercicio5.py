# Dada una listade números, utiliza un método para eliminar todos los elementos que sean iguales a un valor dado
lista= [2, 7, 8, 10, 14, 3, 4, 20,2]
for i in lista:
    if i == 2:
        lista.remove(2)
print(lista)
