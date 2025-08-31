# Suma los elementos en la lista[2, 4, 7, 10, 11, 31, 14, 17, 45, 100]
lista= [2, 4, 7, 10, 11, 31, 14, 17, 45, 100]
suma = 0 
for i in lista:
    suma = suma + i
print(suma)

suma2 = 0 
for i in range(10):
    suma2 += lista[i]
print(suma2)