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
direccion = input("Direccion en la que quieres contar(arriba/abajo): ")
if direccion == "arriba":
    numero = int(input("Introduzca un numero superior a 1: "))
    i = 1
    for _ in range(1, numero+1):
        print(0+i)
        i = i + 1
elif direccion == "abajo":
    numero = int(input("Introduzca un numero inferior a 20: "))
    if numero < 20:
        i = 0
        for _ in range(numero+1):
            print(20-i)
            i = i+1
    else:
        print("Debe ser un numero inferior a 20")
else:
    print("No entiendo")

Ejercicio 043--------------------------------------------
    COMPROBAR EL NUMERO 43  SJDFNDSNFDJFNJDNSJNFÑKDNFSÑKFÑ
numeroUsu = int(input("personas a invitar en la fiesta: "))

if numeroUsu < 10:
    for _ in range(10):
        nombre = input("Nombre del persona: ")
        print(nombre+" ha sido invitado")
else:
    for _ in range(3):
        print("Demasiadas personas")

Ejercicio 044--------------------------------------------
numeroUsu = int(input("personas a invitar en la fiesta: "))

if numeroUsu < 10:
    for _ in range(numeroUsu):
        nombre = input("Nombre del persona: ")
        print(nombre+" ha sido invitado")
else:
    for _ in range(3):
        print("Demasiadas personas")


BUCLE WHILE ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Ejercicio 045--------------------------------------------
total = 0
while total < 50:
    numero = int(input("Introduce un numero "))
    total = numero +total
    print("El total es "+ str(total))

Ejercicio 046--------------------------------------------
numero = 0
while numero < 6:
    numero = int(input("Introduce un numero "))

print("El último número que ha introducido fue un  "+ str(numero))

Ejercicio 047--------------------------------------------
print("Se sumaran los numeros : ")
numero = int(input("Introduce un numero 1 "))
numero2 = int(input("Introduce un numero 2 "))
total = numero + numero2

respuesta ="si"
while respuesta == "si":
    respuesta = input("Deseas añadir otro numero? si/no ").lower()
    if respuesta == "si":
        numero = int(input("Introduce un numero "))
        total = numero + total
    else:
        respuesta = "no"
print("Total "+ str(total))

Ejercicio 048--------------------------------------------
total = 0
respuesta ="si"
while respuesta == "si":
    nombre = input("A quien quieres invitar: ")
    print(nombre + " ha sido invitado ")
    total = 1 + total
    respuesta = input("Quieres añadir a alguien mas? si/no ").lower()
    if respuesta != "si":
        break
print("Total "+ str(total))
Ejercicio 049--------------------------------------------
compnum = 50
contador = 0
while compnum < 100:
    numero = int(input("Adivina el valor de compnum: "))
    if numero > compnum:
        print("Demasiado alto. Intentalo de nuevo")
        contador= contador +1
    elif numero < compnum:
        print("Demasiado bajo. Intentalo de nuevo")
        contador = contador + 1
    else:
        break
print("Bien hecho, lo has hecho en "+ str(contador+1)+" intentos.")
Ejercicio 050--------------------------------------------
numero = 0
while numero < 10 or numero>20:
    numero = int(input("introduce un numero entre el 10 y el 20: "))
    if numero <= 9:
        print("Demasiado bajo.")
    elif numero >=19:
        print("Demasiado alto .")
    else:
        print("Gracias")
Ejercicio 051--------------------------------------------


RANDOM´.....................................................................
............................................................................
............................................................................
Ejercicio 052--------------------------------------------
import random

listaFruta = ["manzana", "pera", "platano", "banana", "uva" ]
numero = random.randint(1,5)
print(listaFruta[numero])

Ejercicio 053--------------------------------------------

Ejercicio 054--------------------------------------------


"""
import random

listaFruta = ["manzana", "pera", "platano", "banana", "uva" ]
numero = random.randint(1,5)
print(listaFruta[numero])
