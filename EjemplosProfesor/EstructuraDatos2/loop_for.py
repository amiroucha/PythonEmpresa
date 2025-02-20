
# Introduccion a los bucles en Python

# Loop es un bloque de codigo que se repite varias veces.
# Se trata de bucles

# iterar es recorrer una lista de elementos
# una lista es iterable porque se puede recorrer una serie de elementos

# ejemplo de iteracion
# for i in range(5):
#     print(i)

#Existen dos tipos de bucles en Python
# 1. for, el cual se repite un numero determinado de veces
# 2. while, el cual se repite mientras una condicion sea verdadera
print("---------------------------------------------")
print("Bucle for")
print("---------------------------------------------")

# Bucle for se repite un numero determinado de veces

nombre= ["Juan", "Pedro", "Maria", "Luis", "Ana"]
for i in nombre:
    print("Hola",i)

# Lo que vamos a hacer es que por cada elemento en la lista nombre,
# se va a imprimir el nombre de la persona

# la i es una variable que se va a ir cambiando por cada elemento de la lista
# puedo poner cualquier nombre a la variable, no necesariamente i

print("---------------------------------------------")

lista= ["a", "b", "c"]
for letra in lista:
    print(letra)   

print("---------------------------------------------")

lista= ["a", "b", "c"]
for letra in lista:
    print("letras " + letra) 

print("---------------------------------------------")  
lista= ["a", "b", "c"]
# podemos usar indices en el bucle for
for letra in lista:
    numero_de_letra= lista.index(letra) + 1
    print("letra", numero_de_letra, letra)

print("---------------------------------------------")

lista=["Pablo", "Juan", "Pedro", "Maria", "Luis", "Ana"]

# quiero hacer un loop que por cada nombre de la lista haga una verificacion

for nombre in lista:
    if nombre.startswith("P"):
        print(nombre)
    else:
        print("No empieza con P")   
 
# solo va a imprimir los nombres que empiecen con la letra P, es decir,
# los que cumplan con la condiciones del if

print("---------------------------------------------")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   

mi_valor= 0

for numero in numeros:
    mi_valor= mi_valor + numero
    print(mi_valor)

# hay que prestar atención si el print esta dentro del bucle o fuera de el
# si esta dentro del bucle, se va a imprimir por cada iteracion
# si esta fuera del bucle, se va a imprimir una sola vez. Se ejecuta cuando el bucle termina.


print("---------------------------------------------")


palabra = "Python"

for letra in palabra:
    print(letra)        

#los strings al igual que las listas son iterables, se pueden recorrer

print("---------------------------------------------")

# también se puede hacer de esta forma:

for letra in "Python":
    print(letra)

print("---------------------------------------------")  

# podemos iterar en una lista que contenga listas

lista_de_listas= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  

for lista in lista_de_listas:
    print(lista)

# si queremos acceder a los elementos de las listas internas

for lista in lista_de_listas:
    for numero in lista:
        print(numero)

print("---------------------------------------------")

# como podemos iterar en un diccionario

diccionario= {"a": 1, "b": 2, "c": 3}

for clave in diccionario:
    print(clave) # solo se imprimen las claves

print("---------------------------------------------")

# si lo quiero ver todo

for item in diccionario.items():
    print(item)# se imprimen las claves y los valores
print("---------------------------------------------")
# si quiero ver solo los valores

for valor in diccionario.values():
    print(valor)

print("---------------------------------------------")

#puedo crear dos variables para que me muestre las claves y los valores

for clave, valor in diccionario.items():
    print(clave, valor)

print("---------------------------------------------")









