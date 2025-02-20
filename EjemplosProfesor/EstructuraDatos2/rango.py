#-------------------------------------------
#rango(range)
#-------------------------------------------

# para establecer iteraciones en un loop hemos tenido que
# usar listas antes, pero con la funcion range() podemos
# hacerlo de manera mas sencilla

# un rango es una funcion que genera una secuencia de numeros

print("------------------------------------------------")
print("rango")
print("------------------------------------------------")

lista = [1,2,3,4]

for i in lista:
    print(i)    

print("------------------------------------------------")
# de manera mas sencilla usamos range

for i in range(5): #comienza en 0 y termina en 4
    print(i)

print("------------------------------------------------")
# podemos especificar el inicio y el fin

for i in range(1,5): #comienza en 1 y termina en 4
    print(i)

print("------------------------------------------------")

# podemos especificar el inicio, el fin y el paso

for i in range(1,10,2): #comienza en 1 y termina en 9, con paso de 2
    print(i)

print("------------------------------------------------")

# En algunos casos podemos usarlos fuera de un loop
# imagina que queremos una lista con los numeros del 1 al 100
# seria tedioso escribirlos uno por uno, pero con range() es facil

lista=list(range(1,101))
print(lista)

print("------------------------------------------------")








