

# bucle while
print("---------------------------------------------")

print("Bucle while")

print("---------------------------------------------")

# Bucle while se repite hasta que una condicion se cumpla

# si se cumple la condicion se ejecuta el bloque de codigo

# se repite "mientras" que se cumpla la condicion

# Un ejemplo lo tenemos en los videojuegos.
#  Mientras tengas vidas sigues jugando

#sintaxis
#------------------------------------
# while condicion:
#     bloque de codigo
#------------------------------------

# podemos añadir un bloque else
#------------------------------------
# while condicion:
#     bloque de codigo
# else:
#     bloque de codigo
#------------------------------------

# hay que tener cuidado con los bucles infinitos
# si la condicion nunca se cumple el bucle se ejecutara de forma infinita

# en los bucles while podemos usar las palabras reservadas
#  break, continue y pass. Lo veremos mas adelante

print("Ejemplos")

print("---------------------------------------------")

monedas= 5

while monedas > 0:
    print(f"Te quedan {monedas} monedas")
    monedas -= 1

print("---------------------------------------------")

# podemos poner un else al final del bucle

monedas= 5

while monedas > 0:
    print(f"Te quedan {monedas} monedas")
    monedas -= 1
else:
    print("No tienes mas monedas")

# este ejmplo, aunque es parecido a un bucle for es distinto
# en un bucle for sabemos cuantas veces se va a repetir
# ene ste caso no sabemos cuantas veces se va a repetir
# Pero la dinámica es distinta
# En este caso se ejecuta el bloque de codigo mientras se cumpla la condicion

print("---------------------------------------------")

"""respuesta= "si"

while respuesta == "si":
    respuesta= input("Quieres seguir jugando? (si/no) ") #aqui pierdo el control del programa
else:
    print("Gracias por jugar")"""

# en este caso el bucle se ejecutara mientras la respuesta sea si
# si la respuesta es no, se ejecutara el bloque de codigo del else
# no sabemos cuantas veces se va a repetir el bucle ya que depende de la respuesta del usuario



print("---------------------------------------------")
print("pass, break y continue")
print("---------------------------------------------")

# podemos usar las palabras reservadas pass, break y continue en los bucles while

# pass: no hace nada, se usa para evitar errores de sintaxis

# break: se usa para salir del bucle. Lo interrumpe

# continue: se usa para saltar a la siguiente iteracion del bucle

# podemos usar estas palabras reservadas en los bucles for tambien

# ejemplo pass

"""respuesta= "si"

while respuesta == "si":
    pass # no se que hacer aqui de momento. Uso pass para evitar errores de sintaxis
print("hola")"""


print("---------------------------------------------")
#ejemplo break

nombre= input("Introduce tu nombre: ")

for letra in nombre:
    print(letra)
print("---------------------------------------------")  
#quiero que el bucle se detenga si encuentra una letra en concreto
# letra o por ejemplo

for letra in nombre:
    print(letra)
    if letra == "o":
        break

print("---------------------------------------------")
#ejemplo continue
# no va interrumpir el bucle, solo va a saltar a la siguiente iteracion

for letra in nombre:
    if letra == "o":
        continue # se interrumpe la iteracion actual y se salta a la siguiente
    print(letra)

print("---------------------------------------------")






































































