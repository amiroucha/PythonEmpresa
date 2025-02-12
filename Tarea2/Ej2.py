
"""
--------------CONDICIONALES------------------------------------------
Ejercicio 12---------------------------------------------
numero1= int(input("Introduce el numero 1: "))
numero2= int(input("Introduce el numero 2: "))
if numero1 > numero2:
    print(numero2)
    print(numero1)
elif numero1 < numero2:
    print(numero1)
    print(numero2)
else:
    print("Los dos numeros son iguales : "+str(numero1))
Ejercicio 13------------------------------------------------
numero1= int(input("Introduce el numero 1: "))
if numero1 < 20 :
    print("Gracias")
else:
    print("Demasiado alto")

Ejercicio 14------------------------------------------------

numero1= int(input("Introduce un numero entre 10 y 20: "))
if (numero1 >= 10) and (numero1 <= 20) :
    print("Gracias")
else:
    print("Respuesta incorrecta")

Ejercicio 16------------------------------------------------
lluvia = input("Esta lloviendo??: ")
if lluvia.lower() == "si":
    viento = input("Hace viento??: ")
    if viento.lower() == "si":
        print("Hace demasiado viento para llevar un paraguas")
    else:
        print("Lleve un paraguas")
else:
    print("Disfrute del día")
Ejercicio 17------------------------------------------------
edad = int(input("Dime tu edad: "))
if edad >= 18:
    print("Puede votar")
elif edad == 17:
    print("Puedes aprender a conducir")
elif edad == 16:
    print("Puedes comprar lotería")
elif edad <= 15:
    print("Truco o trato")

Ejercicio 19------------------------------------------------
opcion = input("Introduce 1 , 2 o 3 : ")
if opcion == str(1):
    print("Gracias")
elif opcion == str(2):
    print("Bien hecho")
elif opcion == str(3):
    print("Correcto")
else:
    print("Mensaje de error")
------------STRINGS--------------------------------------------------------------
Ejercicio 20------------------------------------------------
nombre = input("Introduce el nombre: ")
print("Longitud del nombre : "+str(len(nombre)))
Ejercicio 21------------------------------------------------
nombre = input("Introduce el nombre: ")
apellidos = input("Introduce tus apellidos: ")
nombrecompleto = nombre + " " + apellidos
print("Nombre completo: "+nombrecompleto +"\nLongitud del nombre completo : "+str(len(nombrecompleto)))


Ejercicio 22------------------------------------------------
nombre = input("Introduce el nombre en minusculas: ")
apellidos = input("Introduce tus apellidos en minusculas: ")
nombreCompl = nombre.capitalize() + " " + apellidos.capitalize()
print(nombreCompl)
Ejercicio 23------------------------------------------------


Ejercicio 24------------------------------------------------
palabra = input("Introduce el palabra: ")
print(palabra.upper())
Ejercicio 25------------------------------------------------
nombre = input("Introduce tu nombre de pila: ")
if len(nombre) < 5:
    apellido = input("Introduce tu apellidos: ")
    juntos = nombre + apellido
    print(juntos.upper())
else:
    print(nombre.lower())

Ejercicio 26------------------------------------------------
palabra = input("Introduce el palabra: ")
if palabra[0] == 'a' or palabra[0] == 'e' or palabra[0] == 'i' or palabra[0] == 'o' or palabra[0] == 'u':
    palabra = palabra+"way"
else:
    palabra = palabra[1:]+palabra[0]+"ay"

print(palabra.lower())
---------------------------------------------------------------

frase = input("Introduce una linea de tu cancion favorita: ")
print("Longitud de la frase: "+str(len(frase)))
num1 = int(input("Introduce un numero incial: "))
num2 = int(input("Introduce un numero final: "))

frase = frase[num1:num2]
print(frase)

"""

numero1= int(input("Introduce un numero entre 10 y 20: "))
if (numero1 >= 10) and (numero1 <= 20) :
    print("Gracias")
else:
    print("Respuesta incorrecta")








