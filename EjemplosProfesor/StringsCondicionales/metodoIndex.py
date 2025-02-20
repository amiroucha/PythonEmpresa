
# el metodo index

# los indices en python empiezan en 0

# el metodo index nos permite buscar un elemento en una lista y nos devuelve el indice de la primera ocurrencia de ese elemento

#los espacios en blanco tambien cuentan como caracteres

# el indice reverso empieza en -1 siendo el ultimo elemento de la lista

# ejemplo de conocer el indice de un caracter
mi_texto = "Hola mundo"
print(mi_texto.index("o")) # 1

# ejemplo de conocer el caracter en un indice
mi_texto = "Hola mundo"
print(mi_texto[1]) # o ojo! va entre corchetes

print("------------------------------------------------------------")
print("INDEX")
print("------------------------------------------------------------")

mi_texto = "Esta es una cadena de texto"
resultado= mi_texto[0]
print(resultado)

resultado= mi_texto[9]
print(resultado)

#podemos usar números negativos
resultado= mi_texto[-1]
print(resultado)

#vamos a ver el caracter que tenemos en la posición ?
resultado= mi_texto.index("a") # usamos el metodo index para buscar la letra a
print(resultado)

# si probamos con una letra que no existe en la cadena nos dará un error

#podemos buscar cadenas de texto
resultado= mi_texto.index("cadena")
print(resultado) #nos indica la posición en la que empieza la palabra cadena

# el indice es sensible a mayusculas y minusculas
#resultado= mi_texto.index("Cadena")
#print(resultado) # nos dará un error porque la C de Cadena no es igual a la c de cadena

# si la palabra esta repetida nos devolverá la primera ocurrencia

#puedo buscar desde una posición concreta
resultado= mi_texto.index("a", 5) #busca la letra a a partir de la posición 5
print(resultado)

#tambié le puedo decir hasta donde quiero buscar
resultado= mi_texto.index("a", 5, 11) #busca la letra a a partir de la posición 5 y hasta la 10. no es inclusivo
print(resultado)


# tenemos el metodo rindex que nos devuelve la última ocurrencia de un caracter
resultado= mi_texto.rindex("o")
print(resultado) #nos devuelve la posición de la última o























