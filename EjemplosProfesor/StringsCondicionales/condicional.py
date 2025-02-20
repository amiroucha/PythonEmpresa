# condicional if

# if

# if condicion:
#     bloque de codigo
# else:
#     bloque de codigo

# Ejemplo

a = 10
b = 5

if a > b:
    print("a es mayor que b")
else:
    print("a no es mayor que b")    

if a < b:
    print("a es menor que b")
else:
    print("a no es menor que b")    

if a == b:
    print("a es igual a b") 
else:
    print("a no es igual a b")

if a != b:
    print("a es diferente de b")
else:
    print("a no es diferente de b") 

print("-----------------------------------------------")
num = 10

if num > 10:
    print("El numero es mayor que 10")
elif num == 10:
    print("El numero es igual a 10")
else:
    print("El numero es menor que 10")

print("-----------------------------------------------")


# if anidado

# if condicion:
#     bloque de codigo
#     if condicion:
#         bloque de codigo
#     else:
#         bloque de codigo
# else:
#     bloque de codigo

# Ejemplo

num = 10

if num > 10:
    print("El numero es mayor que 10")
    if num == 15:
        print("El numero es igual a 15")
    else:
        print("El numero no es igual a 15")
else:
    print("El numero es menor que 10")

print("-----------------------------------------------")

# podemos usar operandos logicos y operadores de comparacion

# and
# or
# not

# Ejemplo

num = 10

if num > 5 and num < 15:
    print("El numero esta entre 5 y 15")

if num < 5 or num > 15:
    print("El numero no esta entre 5 y 15") 

if not num > 15:
    print("El numero no es mayor que 15")

if not num < 5:
    print("El numero no es menor que 5")

print("-----------------------------------------------")

# mira la documentación sobre condicionales en python

# https://docs.python.org/3/tutorial/controlflow.html#if-statements


f=input("nombre en minusculas: ")
s=input(" apellido en minusculas: ")

f=f.title()
s=s.title()

name=f+" "+s
print(name)










