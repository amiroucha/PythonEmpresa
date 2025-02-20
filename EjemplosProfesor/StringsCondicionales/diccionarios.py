# Diccionarios
print("----------------------------------------------") 


# Se trata de una estructura de datos que permite almacenar pares clave-valor.
# Se escriben entre llaves {} y los pares clave-valor separados por comas.
# Las claves deben ser únicas. Los valores si pueden repetirse.
# Los valores pueden ser de cualquier tipo de dato.
# no tienen orden, es decir, no podemos acceder a un elemento por su indice.
# Son mutables, es decir, podemos cambiar su contenido.
print("----------------------------------------------")

diccionario={"c1":"valor1", "c2":"valor2", "c3":"valor3"}
print(type(diccionario)) #esto nos dice que es un diccionario
print(diccionario) #esto nos imprime el diccionario
print("----------------------------------------------")

# podemos consultar el valor de una clave

resultado=diccionario["c1"]
print(resultado) #esto nos devuelve "valor1"
print("----------------------------------------------")

cliente= {"nombre":"Juan",
          "apellido":"Fuentes",
          "edad":30, 
          "telefono":"123456789"}

consulta=cliente["apellido"]
print(consulta) #esto nos devuelve "Fuentes"
print("----------------------------------------------")

# Un diccionario puede tener diferentes tipos de datos

dic={"c1":55, "c2":[10,20,30], "c3":{"s1":100, "s2":200}}

print(dic["c2"]) #esto nos devuelve [10, 20, 30]

# si quiero consultar el indice 1 de la lista que esta en la clave "c2" del diccionario "dic", hago lo siguiente:

print(dic["c2"][1]) #esto nos devuelve 20
print("----------------------------------------------")

#podemos usar metodos de los diccionarios

dic={"c1":["a", "b", "c"], "c2":["d", "e", "f"]}
print(dic["c2"][1].upper()) #esto nos devuelve "E"
print("----------------------------------------------") 

#podemos agregar elementos a un diccionario

dic={1:"a", 2:"b"}
dic[3]="c"
print(dic) #esto nos devuelve {1: 'a', 2: 'b', 3: 'c'}
print("----------------------------------------------")

#podemos sobre-escribir un valor que ya existe en un diccionario

dic={1:"a", 2:"b"}
dic[2]="B"
print(dic) #esto nos devuelve {1: 'a', 2: 'B'}  
print("----------------------------------------------")

# podemos conocer todas las claves de un diccionario con el metodo keys()

print(dic.keys()) #esto nos devuelve dict_keys([1, 2])
print("----------------------------------------------")

# podemos conocer todos los valores de un diccionario con el metodo values()

print(dic.values()) #esto nos devuelve dict_values(['a', 'B'])
print("----------------------------------------------")

# podemos conocer todos los pares clave-valor de un diccionario con el metodo items()

print(dic.items()) #esto nos devuelve dict_items([(1, 'a'), (2, 'B')])
print("----------------------------------------------")



















