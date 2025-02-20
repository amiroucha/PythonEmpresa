# Sets

# se pueden definir de dos formas

# 1. con la función set()
s = set([1, 2, 3, 4, 5]) # de esta forma tienen que estar encerrados en corchetes
print(s)

# 2. con llaves
s = {1, 2, 3, 4, 5} # de esta forma no tienen que estar encerrados en corchetes
print(s)

# los sets no tienen orden

# solo admiten valores únicos. Si lo haces con valores repetidos, se eliminarán

# son inmutables, no se pueden modificar

print("---------------------------------------------")

mi_set = set([1, 2, 3, 4, 5]) # si no se encierra falla.
print(type(mi_set))
print(mi_set)

print("---------------------------------------------")


otro_set= {1, 2, 3, 4, 5}
print(type(otro_set))
print(otro_set)

print("---------------------------------------------")

# si quiero buscar un valor en un set, se hace con la palabra reservada in
print(1 in mi_set)  # True

print("---------------------------------------------")

# no se repiten los valores

mi_set = {1, 2, 3, 4, 5, 5, 5, 5, 5}
print(mi_set)

print("---------------------------------------------")

# pueden admitir tuplas pq son inmutables también, pero no listas

mi_set = {(1, 2, 3), (4, 5, 6)}
print(mi_set)

print("---------------------------------------------")

# podemos usar la función len() para saber cuántos elementos tiene un set

mi_set = {1, 2, 3, 4, 5}
print(len(mi_set))

print("---------------------------------------------")

# unión de sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7, 8}

# también se puede hacer con la función union()

print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8}

print("---------------------------------------------")

# podemos agregar elementos a un set con la función add()

mi_set = {1, 2, 3, 4, 5}
mi_set.add(6)
print(mi_set)

print("---------------------------------------------")

# podemos eliminar elementos de un set con la función remove()

mi_set = {1, 2, 3, 4, 5} # si descarto un elemento que no existe, falla
mi_set.remove(3)
print(mi_set)

#también se puede hacer con la función discard()

mi_set = {1, 2, 3, 4, 5} # si descarto un elemento que no existe, no falla
mi_set.discard(3)
print(mi_set)

print("---------------------------------------------")


# podemos usar el metodo pop() para eliminar un elemento aleatorio

mi_set = {1, 2, 3, 4, 5}
mi_set.pop()
print(mi_set)

print("---------------------------------------------")

# clear() para eliminar todos los elementos de un set

mi_set = {1, 2, 3, 4, 5}
mi_set.clear()
print(mi_set)

print("---------------------------------------------")

# mira la documentación para ver más métodos de los sets








































