"""
Ejercicio 035---------------------------------------------
nombre= input("¿Cómo te llamas?: ")
for i in range(3):
    print(nombre)
Ejercicio 036---------------------------------------------
nombre= input("¿Cómo te llamas?: ")
numero=int(input("Introduzca un numero: "))
for i in range(numero):
    print(nombre)
Ejercicio 037---------------------------------------------
nombre = input("¿Cómo te llamas?: ")
for i in nombre:
    print(i)
Ejercicio 038---------------------------------------------
nombre = input("¿Cómo te llamas?: ")
numero=int(input("Introduzca un numero: "))
for _ in range(numero):
    for i in nombre:
        print(i)
Ejercicio 039---------------------------------------------
numeroUsu = int(input("Introduzca un numero del 1 al 12: "))
if numeroUsu >0 and numeroUsu <12:
    print("Tabla de multiplicar del " + str(numeroUsu))
    for numero in range(1, 11):
        print(str(numero) + "*" + str(numeroUsu) + " = " + str(numeroUsu * numero))
else:
    print("Debe ser un numero entre en 1 y 12")
Ejercicio 040---------------------------------------------
numeroUsu = int(input("Introduzca un numero menor que 50: "))
if numeroUsu < 50:
    for numero in range(numeroUsu, 51):
        print(numero)
else:
    print("Debe ser un numero menor de 50")
Ejercicio 041---------------------------------------------
nombre = input("¿Cómo te llamas?: ")
numeroUsu=int(input("Introduzca un numero: "))
if numeroUsu < 10:
    for _ in range(numeroUsu):
        print(nombre)
else:
    for _ in range(3):
        print("Demasiado alto")
Ejercicio 042---------------------------------------------
total = 0
print("Tienes que introducir 5 numeros: ")
for _ in range(5):
    numeroUsu = int(input("Introduzca un numero: "))
    si = input("Quieres añadirlo al total?(si / no): ")
    if si == "si" or si == "Si" or si == "SI":
        total += numeroUsu
print("Total: "+str(total))
Ejercicio 043--------------------------------------------

"""
total = 0
print("Tienes que introducir 5 numeros: ")
for _ in range(5):
    numeroUsu = int(input("Introduzca un numero: "))
    si = input("Quieres añadirlo al total?(si / no): ")
    if si == "si" or si == "Si" or si == "SI":
        total += numeroUsu
print("Total: "+str(total))