#operadores logicos

#and, or, not

#and: si todas las condiciones son verdaderas
#or: si alguna de las condiciones es verdadera
#not: niega la condicion

#Ejemplo de operador and
print("Ejemplo de operador and")
print("Ejemplo 1")
print("Comparacion 1: ", 2>1)
print("Comparacion 2: ", 3>2)
print("Comparacion 3: ", 4>3)
print("Comparacion 4: ", 5>4)
print("Comparacion 5: ", 6>5)

print("Resultado de la comparacion: ", 2>1 and 3>2 and 4>3 and 5>4 and 6>5)
print("--------------------------------------------------") 
print("Ejemplo 2")
print("--------------------------------------------------") 
print("Comparacion 1: ", 2>1)
print("Comparacion 2: ", 3>2)
print("Comparacion 3: ", 4>3)

print("Resultado de la comparacion: ", 2>1 and 3>2 and 4>3 and 5>4 and 6>5)

#Ejemplo de operador or

print("Ejemplo de operador or")
print("--------------------------------------------------") 
print("Ejemplo 1")
print("--------------------------------------------------") 
print("Comparacion 1: ", 2>1)
print("Comparacion 2: ", 3>2)
print("Comparacion 3: ", 4>3)

print("Resultado de la comparacion: ", 2>1 or 3>2 or 4>3 or 5>4 or 6>5)
print("--------------------------------------------------") 
print("Ejemplo 2")
print("--------------------------------------------------") 
print("Comparacion 1: ", 2>1)
print("Comparacion 2: ", 3>2)
print("Comparacion 3: ", 4>3)

print("Resultado de la comparacion: ", 2>1 or 3>2 or 4>3 or 5>4 or 6>5)

#Ejemplo de operador not
print("Ejemplo de operador not")
print("--------------------------------------------------") 
print("Ejemplo 1")
print("--------------------------------------------------") 
print("Comparacion 1: ", 2>1)
print("Comparacion 2: ", 3>2)
print("Comparacion 3: ", 4>3)

print("Resultado de la comparacion: ", not 2>1)
print("Resultado de la comparacion: ", not 3>2)
print("Resultado de la comparacion: ", not 4>3)
print("--------------------------------------------------") 
print("Ejemplo 2")
print("--------------------------------------------------") 
print("Comparacion 1: ", 2>1)
print("Comparacion 2: ", 3>2)
print("Comparacion 3: ", 4>3)

print("Resultado de la comparacion: ", not 2>1)

print("--------------------------------------------------") 
#OPERADOR DE COMPARACION
print("--------------------------------------------------") 
#mayor que >
print("Operador mayor que >")
print("Comparacion 1: ", 2>1)

#menor que <
print("Operador menor que <")
print("Comparacion 1: ", 2<1)

#mayor o igual que >=
print("Operador mayor o igual que >=")
print("Comparacion 1: ", 2>=1)

#menor o igual que <=
print("Operador menor o igual que <=")
print("Comparacion 1: ", 2<=1)

#igual que ==
print("Operador igual que ==")
print("Comparacion 1: ", 2==1)

#diferente que !=
print("Operador diferente que !=")
print("Comparacion 1: ", 2!=1)

print("--------------------------------------------------")

mi_bool= 10==25
print(mi_bool)
print("--------------------------------------------------")
mi_bool= 10!=25
print(mi_bool)
print("--------------------------------------------------")

# podemos comparar operaciones

mi_bool= 10==5+5
print(mi_bool)
print("--------------------------------------------------")

# podemos comparar cadenas
# los strings a la hora de comparar son case sensitive
mi_bool= "hola"=="hola"
print(mi_bool)

mi_bool= "hola"=="Hola"
print(mi_bool)

mi_bool= "hola"=="Hola".lower()
print(mi_bool)

mi_bool= "hola"!="Hola"
print(mi_bool)

print("--------------------------------------------------")

# podemos comparar valores de distintos tipos

mi_bool= 10==10.0 #int y float si son iguales en valor son iguales.
print(mi_bool)

mi_bool= 10=="10"
print(mi_bool)

mi_bool= 10==int("10")
print(mi_bool)

mi_bool= 10==float("10")
print(mi_bool)

mi_bool= 10==float("10.0")
print(mi_bool)

print("--------------------------------------------------")














