from os.path import split

textoUsuario = input("Ingresa un texto a eleccion: ")
letra1 = input("Ingresa la primera letra: ")
letra2 = input("Ingresa la segunda letra: ")
letra3 = input("Ingresa la tercera letra: ")
print("\n")

print("CANTIDAD DE LETRAS")
resultado1= textoUsuario.index(letra1, 1)
resultado2= textoUsuario.index(letra2, 1)
resultado3= textoUsuario.index(letra3, 1)
print("Hemos encontrado la letra "+letra1+" repetida : "+str(resultado1)+" veces")
print("Hemos encontrado la letra "+letra2+" repetida : "+str(resultado2)+" veces")
print("Hemos encontrado la letra "+letra3+" repetida : "+str(resultado3)+" veces")
print("\n")

print("LETRAS DE INICIOI Y FIN ")
fragmento1=textoUsuario[:1]
fragmento2=textoUsuario[-1]
print("Letra incial: "+fragmento1 +" - letra final: "+fragmento2)

print("\n")
print("texto invertido ")
fragmentoReves=textoUsuario[-1:0] # desde la posición 0 hasta el final de 2 en 2
print("orden del reves: "+str(fragmentoReves))

print("\n")
print("buscando palabra python ")
resultadoP=textoUsuario.find("Python")
if resultadoP == -1:
    print("Palabra python no existe")
else:
    print("Palabra python existe en el texto ")

