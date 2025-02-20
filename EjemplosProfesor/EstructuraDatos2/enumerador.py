

print("--------------------------------------------")   
print("Enumerador")
print("--------------------------------------------")

# enumerdador en python se llama enumerate
# su funcion es hacernos la vidad mas facil al momento de recorrer los índices de una colección 

#lista= ["a","b","c","d","e","f","g","h","i","j"]

# for letra in lista:
#     print(letra)
#     print(indice??)

# si estoy escribiendo un loop for y necesito el indice de la lista, puedo usar enumerate

# una forma de hacerlo sería asi:

lista= ["a","b","c"]
indice=0 #nos cargamos el indice para hacerlo con enumerate

for letra in lista:
    print(indice,letra)
    indice+=1 # incremento el indice de uno en uno

print("---------------------------------------------------")

# pero esta no es la mejor manera de hacerlo, por eso existe enumerate

for item in enumerate(lista):
    print(item)

# contiene una tupla con el indice y el valor

print("---------------------------------------------------")

# podemos hacer lo como lo hemos visto en ocasiones anteriores

for indice,letra in enumerate(lista):
    print(indice,letra)

print("---------------------------------------------------")

# podemos trabajar con strings, listas, tuplas, diccionarios,integers, floats, etc

for indice,letra in enumerate(range(50,55)):
    print(indice,letra)

print("---------------------------------------------------")

# podemos usarlos fuera de un loop

mis_tuplas=list(enumerate("abcde")) # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
print(mis_tuplas)

print("---------------------------------------------------")

# podemos desempaquetar la tupla

mis_tuplas=list(enumerate("abcde")) 
print(mis_tuplas[1][0]) # 1

#accedemos al indice 1 de la tupla y luego al primer elemento de la tupla
# de esta manera podemos acceder a los indices de una lista
print("---------------------------------------------------")

# CUANDO QUIERAS TENER ACCESO A LOS INDICES DE UN OBJETO ITERABLE,
# UTILIZA ENUMERATE

# EN RESUMEN, ENUMERATE NOS DEVUELVE UNA TUPLA CON EL INDICE Y EL VALOR

print("---------------------------------------------------")
















