textoUsuario = input("Introduce un texto: ").lower()
print("Introduce 3 letras: ")

letra1 = input("Letra 1 : ").lower()
letra2 = input("Letra 2 : ").lower()
letra3 = input("Letra 3 : ").lower()

# 1: las veces que aparece cadad lettra
contador1 = textoUsuario.count(letra1)
contador2 = textoUsuario.count(letra2)
contador3 = textoUsuario.count(letra3)

print(f"La letra {letra1} se encuentra {contador1} veces en el texto")
print(f"La letra {letra2} se encuentra {contador2} veces en el texto")
print(f"La letra {letra3} se encuentra {contador3} veces en el texto")

#2.texto pasarlo a una lista
palabrasLista = textoUsuario.split()
print(f"El texto tiene " + str(len(palabrasLista)) + " palabras")
print(palabrasLista)

#3.sacar la 1 y ultima letra de la frase
letra1 = textoUsuario[0]
letraFinal = textoUsuario[len(textoUsuario) - 1]
print("Letra inicial: "+letra1)
print("Letra final: "+letraFinal)

#3. otra forma si no es lista
print("LETRAS DE INICIOI Y FIN ")
fragmento1=textoUsuario[:1]
fragmento2=textoUsuario[-1]
print("Letra incial: "+fragmento1 +" - letra final: "+fragmento2)


#4. poner la frase en order inverso
textoInvertido = " ".join(palabrasLista[::-1])
print(textoInvertido)



#5. Si la palabra "Python" se encuentra dentro del texto
if "Python".lower() in textoUsuario:
    print("La palabra Python se encuentra dentro del texto.")
else:
    print("La palabra Python no se encuentra dentro del texto.")

#5 otra formaa
print("Buscando palabra python ")
resultadoP =textoUsuario.find("Python".lower())
if resultadoP == -1:
    print("Palabra python no existe")
else:
    print("Palabra python existe en el texto ")