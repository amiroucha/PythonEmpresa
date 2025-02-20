
print("----------------------------------")
print("Random")
print("----------------------------------")

# Con random vamos a usar números aleatorios y además vamos a ver como 
#importamos métodos a Python.

# usaremos un método llamado "randint()" que viene de random integer
# el cual nos devolverá un número entero aleatorio

# estos métodos hay que importarlos
# le decimos a Python que desde tal librería importa tal método.
#------------------------------------------------------
#ejemplo:
#   desde random importa randint (en inglés)
#   from random import randint
#------------------------------------------------------

# si quieres importarlo todo:
#   from random import *

#------------------------------------------------------

# vamos a conocer 5 métodos de random():
#
#   1.randint()
#   2.uniform()
#   3.random()
#   4.choice()
#   5.shuffle()
#

from random import * # de la librería random importa todo

aleatorio = randint(1,50)
print(aleatorio)

print("----------------------------------")

aleatorio = uniform(1,5) # nos devuelve un valor decimal
print(aleatorio)

print("----------------------------------")

# si quiero menos decimales lo encierro en un round

aleatorio=round(uniform(1,5),2)
print(aleatorio)

print("----------------------------------")

aleatorio = random()# no necesita ningún parámetro, va vacio
print(aleatorio) # es aleatorio entre 0 y 1


print("----------------------------------")

#choice nos permite trabajar con una seleción de elementos 
# aleatorios de una lista

colores= ["azul","rojo","verde","amarillo"]

aleatorio = choice(colores)
print(aleatorio)


print("----------------------------------")

# shuffle quiere decir mezclar. nos puede ser until en un juego de cartas

numeros = list(range(5,50,5)) # el último núemro no es inclusivo
print(numeros)

shuffle(numeros)
print(numeros)
# shuffle no podemos almacenarlo en una lista
# no podemos usarlos con strings ya que estos son inmutables
print("----------------------------------")