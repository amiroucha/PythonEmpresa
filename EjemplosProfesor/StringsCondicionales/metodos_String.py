#upper() - pasa a mayusculas
#lower() - pasa a minusculas
#split() - separa palabras en partes(lista)
#join() - une palabras usando un separador
#find() - busca una palabra en un texto(un substring)
#replace() - reemplaza una palabra por otra
#hay muchos mas métodos, mira la documentación

print("----------------------------------------")

texto="Este es el texto de Antonio"

resultado=texto
print(resultado)
print("----------------------------------------")

resultado=texto.upper() # pasa a mayusculas
print(resultado)
print("----------------------------------------")

resultado=texto[2].upper() # pasa a mayusculas la letra en la posición 2
print(resultado)
print("----------------------------------------")

resultado=texto.lower() # pasa a minus
print(resultado)    
print("----------------------------------------")

resultado=texto.split() # separa palabras en partes(lista)
print(resultado)
print("----------------------------------------")
#por defecto separa por espacios, pero se puede especificar otro separador
resultado=texto.split("t") # separa por la letra t
print(resultado)
print("----------------------------------------")
a="Aprender"
b="Python"
c="es"
d="genial"
e=" ".join([a,b,c,d]) # une palabras usando un separador. el separador es el espacio. Creamos una lista con las palabras y las unimos con un espacio
print(e)
print("----------------------------------------")

resultado=texto.find("Antonio") # busca una palabra en un texto(un substring)
print(resultado)#cuando no encuentra la palabra devuelve -1 a diferencia de index que devuelve un error
print("----------------------------------------")

resultado=texto.replace("Antonio","Juan") # reemplaza una palabra por otra. necesita dos argumentos, el que se busca y el que se reemplaza
print(resultado)
print("----------------------------------------")

resultado=texto.replace("e","i") # reemplaza una letra por otra
print(resultado)
print("----------------------------------------")























