"""
Ejercicio 118---------------------------------------------
def suma(a, b):
    return a + b

print(suma(3, 10))
Ejercicio 119---------------------------------------------
def es_par(n):
    return n % 2 == 0

print(es_par(8))
Ejercicio 120---------------------------------------------
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(factorial(6))
Ejercicio 121---------------------------------------------
def area_rectangulo(base, altura):
    return base * altura

print(area_rectangulo(4, 6))
Ejercicio 122---------------------------------------------
def mayusculas(cadena):
    return cadena.upper()

print(mayusculas("pepe"))
Ejercicio 123---------------------------------------------
def concatenar(cadena1, cadena2):
    return cadena1 + cadena2
print(concatenar("Soy ", "pepe!"))

Ejercicio 124---------------------------------------------
def longitud(cadena):
    contador = 0
    for _ in cadena:
        contador += 1
    return contador

print(longitud("pepe happy"))
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
Lectura y Escritura de archivos en Python
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
Ejercicio 125---------------------------------------------

"""

botellas = 10
while botellas > 0:
    print("Hay "+str(botellas)+" botellas verdes colgadas en la pared, ")
    print(str(botellas)+" botellas verdes colgadas en la pared, ")
    print("y si 1 botella verde se cae accidentalmente...")

    while True:
        respuesta = input("¿Cuántas botellas verdes habrá colgadas en la pared? ")

        if respuesta.isdigit() and int(respuesta) == botellas - 1:
            botellas -= 1
            print("Habrá "+str(botellas)+" botellas verdes colgadas en la pared.\n")
            break
        else:
            print("No, inténtalo de nuevo.")

print("Ya no hay botellas verdes colgadas en la pared.")

