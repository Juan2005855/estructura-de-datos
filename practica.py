def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

# Solicitar datos al usuario
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

print("Suma:", suma(a, b))
print("Resta:", resta(a, b))
print("Multiplicación:", multiplicacion(a, b))
print("División:", division(a, b))
