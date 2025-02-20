#----------------------------------------------
# Min y Max
#----------------------------------------------

# min() y max() son funciones que nos permiten obtener
# el valor minimo y maximo de un objeto iterable

# funcionan con valores numéricos y alfabéticos



print("------------------------------------------------------")
# vamos a buscar el valor mínimo

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
valor_minimo = min(numeros)
print("El valor mínimo es:", valor_minimo)

# También funciona con cadenas de texto
# son ordenables alfabéticamente
cadenas = ["manzana", "naranja", "plátano", "pera"]
valor_minimo_cadena = min(cadenas)
print("El valor mínimo en cadenas es:", valor_minimo_cadena)

print("----------------------------------------------")

# si usamos un solo nombre nos va a buscar el caracter más bajo

nombre= "Carlos"
print(min(nombre)) # busca primero en la letras myúsculas y luego en las minúsculas

print("------------------------------------------------------")

# vamos a buscar el valor máximo
print("------------------------------------------------------")
valor_maximo = max(numeros)
print("El valor máximo es:", valor_maximo)

# También funciona con cadenas de texto
# son ordenables alfabéticamente

valor_maximo_cadena = max(cadenas)
print("El valor máximo en cadenas es:", valor_maximo_cadena)
print("------------------------------------------------------")

print("------------------------------------------------------")

# podemos usarlos en los diccionarios

dic= {"c1":45,"c2":11}
print(min(dic)) # te devuelve la clave que tiene el valor inferior

# si quiero que me devuelva el valor menor:

print(min(dic.values()))
print("------------------------------------------------------")





