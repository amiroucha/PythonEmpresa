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

"""
#Ejercicio 105---------------------------------------------
def crear_numeros():
    with open("Números.txt", "w") as num:
        num.write("1,2,3,4,5")

#crear_numeros()
#Ejercicio 106---------------------------------------------
def crear_nombres():
    with open("Nombres.txt", "w") as nombres:
        nombres.write("Pepe\nCoco\nFernando\nCoquito\nLole")

#crear_nombres()
#Ejercicio 107---------------------------------------------

def leer_nombres():
    with open("Nombres.txt", "r") as f:
        print(f.read())
#leer_nombres()
#Ejercicio 108---------------------------------------------
def agregar_nombre():
    with open("Nombres.txt", "a") as f:
        nuevo_nombre = input("Ingrese un nuevo nombre: ")
        f.write(f"\n{nuevo_nombre}")
    leer_nombres()
#agregar_nombre()

#Ejercicio 109---------------------------------------------
def subject_txt():
    while True:
        print("1- Crear un nuevo archivo")
        print("2- Mostrar el archivo")
        print("3- Añadir un nuevo tema")
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            tema = input("Ingresa un tema escolar: ")
            with open("Subject.txt", "w") as sub:
                sub.write(tema)
        elif opcion == "2":
            with open("Subject.txt", "r") as sub:
                print(sub.read())
        elif opcion == "3":
            tema = input("Ingrese un nuevo tema escolar: ")
            with open("Subject.txt", "a") as sub:
                sub.write("\n"+tema)
        else:
            print("Opción inválida.")
        break

#subject_txt()
#Ejercicio 110---------------------------------------------
#guardar todos los nombres excepto el que ha metido el usuario
def escribir_menos_seleccionado():
    with open("Nombres.txt", "r") as file:
        names = file.readlines()
    # lista los nombres de Nombres.txt
    names = [name.strip() for name in names]  # quitar espacios en blanco y saltos de línea
    print("Lista de nombres de Nombres.txt:")
    for name in names:
        print(name)

    borrar = input("Escribe un nombre para eliminar: ").strip()

    # guardo tdos excepto el que sea  =  a borrar
    nombres_si = [name for name in names if name.lower() != borrar.lower()]
    # los escribo el Nombres2
    with open("Nombres2.txt", "w") as file:
        for name in nombres_si:
            file.write(name + "\n")

    print("El nombre "+borrar +" ha sido eliminado. Los demás nombres se guardaron en Nombres2.txt.")
escribir_menos_seleccionado()

