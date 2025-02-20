# Description: Listas en Python
print("----------------------------------------------")

# las listas son un tipo de dato que nos permite almacenar varios valores

# pueden ser de cualquier tipo de dato

# se escriben entre corchetes [] y los elementos separados por comas

# podemos tener listas de listas

# no son inmutables, es decir, podemos cambiar su contenido

print("----------------------------------------------")

mi_lista=["a", "b", "c", "d", "e"]
print(type(mi_lista)) #esto nos dice que es una lista
print(mi_lista) #esto nos imprime la lista
print("----------------------------------------------")

#podemos crear listas con diferentes tipos de datos
mi_lista2=["a", 1, 2.0, True]
print(mi_lista2)
print("----------------------------------------------")

#podemos saber cuantos elementos tiene una lista con la funcion len()
print(len(mi_lista)) #esto nos devuelve 5
print("----------------------------------------------")

#podemos acceder a un elemento de la lista con el indice. todo lo que hemos visto en los indices de los strings se aplica a las listas
print(mi_lista[0]) #esto nos devuelve "a"
print(mi_lista[1]) #esto nos devuelve "b"
print(mi_lista[2]) #esto nos devuelve "c"
print(mi_lista[3]) #esto nos devuelve "d"
print(mi_lista[4]) #esto nos devuelve "e"
print("----------------------------------------------")
print(mi_lista[0:3]) #esto nos devuelve ['a', 'b', 'c']
print("----------------------------------------------")

#concatenacion de listas

mi_lista3=["f", "g", "h"]
mi_lista4=mi_lista+mi_lista3
print(mi_lista4) #esto nos devuelve ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("----------------------------------------------")

#hay cosas que los strings no pueden hacer, pero las listas si

mi_lista4[0]="alfa"
print(mi_lista4) #esto nos devuelve ['alfa', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("----------------------------------------------")

#podemos agregar elementos a una lista con el metodo append()
mi_lista4.append("i")
print(mi_lista4) #esto nos devuelve ['alfa', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print("----------------------------------------------")

#podemos eliminar elementos de una lista con el metodo pop()
mi_lista4.pop()#si dejo el parentesis vacio, elimina el ultimo elemento
print(mi_lista4) #esto nos devuelve ['alfa', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print("----------------------------------------------")
mi_lista4.pop(0)#si pongo un indice, elimina el elemento de ese indice
print(mi_lista4) #esto nos devuelve ['b', 'c', 'd', 'e', 'f', 'g', 'h']
print("----------------------------------------------")

#puedo guarar el elemento eliminado en una variable
eliminado=mi_lista4.pop(0)
print(eliminado) #esto nos devuelve "b"
print("----------------------------------------------")

#podemos ordenar una lista con el metodo sort()

mi_lista5=[3, 1, 5, 2, 4]
mi_lista5.sort() #no devuelve nada, pero ordena la lista
print(mi_lista5) #esto nos devuelve [1, 2, 3, 4, 5]
print("----------------------------------------------")

#podemos invertir una lista con el metodo reverse()
mi_lista5.reverse() #no devuelve nada, pero invierte la lista
print(mi_lista5) #esto nos devuelve [5, 4, 3, 2, 1]
print("----------------------------------------------")

#mira la documentacion de python para ver mas metodos de las listas
print("----------------------------------------------")
# CONTAR

mi_lista5 = [3, 1, 5, 2, 4, 3, 3, 1]

# Contar cuántas veces aparece el número 3 en la lista
cantidad_tres = mi_lista5.count(3)

print(f"El número 3 aparece {cantidad_tres} veces en la lista.")

print("----------------------------------------------")

#DIVIDIR

texto = "Hola mundo, cómo estás"
palabras = texto.split()  # Divide el texto en palabras separadas por espacios

print(palabras)

print("----------------------------------------------")

# UNIR ELEMENTOS EN PYTHON

palabras = ["Hola", "mundo", "Python", "es", "genial"]
frase = " ".join(palabras)
print(frase)
#--------------------------------------------------------------

frase = ", ".join(palabras)
print(frase)

print("----------------------------------------------")






























