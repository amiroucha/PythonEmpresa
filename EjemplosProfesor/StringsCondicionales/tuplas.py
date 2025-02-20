"""Los tuples o tuplas, son estructuras de datos que almacenan
múltiples elementos en una única variable. Se caracterizan por
ser ordenadas e inmutables. Esta característica las hace más
eficientes en memoria y a prueba de daños."""
print("----------------------------------------------------")
#Usan paréntesis
tupla = (1, 2, 3, 4, 5)

# ocupa menos espacio en memoria

# No se pueden modificar y por tanto son a prueba de daños

# podemos usarlos sin paréntesis

print("----------------------------------------------------")

mi_tupla=(1,2,3,4,5)
print(type(mi_tupla))
print(mi_tupla)

print("----------------------------------------------------")

# pueden tener elementos de diferentes tipos

mi_tupla=(1,2,3,"hola",True)
print(mi_tupla)

print("----------------------------------------------------")

# podemos consultar elementos por índice

mi_tupla=(1,2,3,"hola",True)
print(mi_tupla[3])

print("----------------------------------------------------")

#podemos anidar tuplas

mi_tupla=(1,2,3,"hola",True,(1,2,3))
print(mi_tupla)
print(mi_tupla[5])
# si quiero acceder a un elemento de la tupla anidada
print(mi_tupla[5][2])

print("----------------------------------------------------")

#podemos hacer casting de tuplas a listas

mi_tupla=(1,2,3,"hola",True)
mi_lista=list(mi_tupla)
print(type(mi_lista))
print(mi_lista)

print("----------------------------------------------------")


# podemos asignar el contenido de una tupla a varias variables
# podemos hacerlo también con listas y diccionarios
# tienen que tener la misma cantidad de elementos

mi_tupla=(1,2,3)
a,b,c=mi_tupla
print(a)
print(b)
print(c)

print("----------------------------------------------------")

t=(1,2,3,1)
print(len(t))

#podemos contar cuantas veces aparece un elemento en una tupla
print(t.count(1)) # el 1 aparece dos veces

print("----------------------------------------------------")

# puedo saber en que índice se encuentra un elemento

print(t.index(1)) # el 1 está en el índice 0
print(t.index(2)) # el 2 está en el índice 1
print(t.index(3)) # el 3 está en el índice 2

print("----------------------------------------------------")

# mira la documentación oficial para ver más métodos de las tuplas




















