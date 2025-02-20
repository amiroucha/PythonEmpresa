#propiedades de los strings

# inmutabilidad. una vez que se crea un string, no se puede cambiar

# hemos trabajado con variables, pero no hemos cambiado el valor de la variable

#concatenacion

#pueden tener mas de una linea sin necesidad de usar el caracter de escape \n

# podemos calcular la longitud de un string con la funcion len()

print("----------------------------------------------")

nombre="Carina" #me doy cuenta que es Karina con K
#nombre[0]="K" #esto no se puede hacer, da error
nombre="Karina" #esto si se puede hacer ya qque cambio el contenido de la variable
print(nombre) #como hemos dicho, los strings son inmutables
print("----------------------------------------------")

#concatenacion

n1= "Hola"
n2= "Mundo"
n3= n1 + " " + n2
print(n3)
print("----------------------------------------------")

#multiplicacion de strings
n1= "Hola"
n2= n1*3 #esto es lo mismo que n1+n1+n1
print(n2)
print("----------------------------------------------")

#pueden tener mas de una linea sin necesidad de usar el caracter de escape \n
poema= """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print(poema)
print("----------------------------------------------")

# podemos ver si existe una palabra en un string
print("agua" in poema) #esto devuelve True
print("fuego" in poema) #esto devuelve False
print("----------------------------------------------")

#tambien podemos ver si no existe una palabra en un string
print("agua" not in poema) #esto devuelve False
print("fuego" not in poema) #esto devuelve True
print("----------------------------------------------")

#len() nos da la longitud de un string
print(len(poema)) #esto devuelve 61
print("----------------------------------------------")









