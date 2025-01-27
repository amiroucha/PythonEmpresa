
"""
Ejercicio 1---------------------------------------------
nombre= input("¿Cómo te llamas?: ")
print("Hola", nombre)
Ejercicio 2------------------------------------------------
nombre= input("¿Cómo te llamas?: ")
apellido= input("Y tu apellidos: ")
print("Hola", nombre +" "+ apellido)
Ejercicio 3------------------------------------------------
print("¿Cómo llamas a un oso sin dientes?\n¡Un oso de goma! ")
Ejercicio 4------------------------------------------------
numero1 = int(input("Introduce un número: "))
numero2 = int(input("Introduce otro número: "))
print("El total es "+str(numero1+numero2))
Ejercicio 5------------------------------------------------
numero1 = int(input("Introduce el numero 1: " ))
numero2 = int(input("Introduce el numero 2: " ))
numero3 = int(input("Introduce el numero 3: " ))
print("La respuesta es : "+ str((numero1+numero2)*numero3))
Ejercicio 6------------------------------------------------
tenia = int(input("Cuantas porciones de pizza tenias: "))
comido = int(input("Cuantas porciones de pizza te has comido: " ))
print("La respuesta es "+ str(tenia-comido))
Ejercicio 7------------------------------------------------
nombre = input("Como te llamas?: " )
edad = int(input("Cuanto años tienes?: " ))
print(nombre +" el próximo cumpleaños usted tendrá "+str(edad+1))
Ejercicio 8------------------------------------------------
total = int(input("Precio total de la cuenta: "))
comensales = int(input("Numero de comensales: "))
print("Precio a pagar cada comensal: "+ str(total/comensales))
Ejercicio 9------------------------------------------------
dias = int(input("Dame un numero de dias: "))
if dias < 0:
    print("Por favor, introduce un número positivo.")
else:
    horas = dias * 24
    minutos = horas * 60
    segundos = minutos * 60
    print("En "+str(dias)+" dias hay "+str(horas)+" horas, "+str(minutos)+" minutos y "+str(segundos)+" segundos.")
Ejercicio 10------------------------------------------------
kilos = int(input("Cuantos kilos quieres convertir: "))
print(str(kilos)+" kilos son :"+str(round((kilos*2.204),3))+ " libras")
Ejercicio 11------------------------------------------------
mayor100 = int(input("Introduce un numero mayor de 100 "))

if mayor100 <= 100:
    print("El numero debe de ser mayor de 100")
else:
    menor10 = int(input("Introduce un numero menor de 10 "))
    if menor10 >=10:
        print("El numero debe de ser menor de 10")
    else:
        print("El numero "+str(menor10)+" cabe "+str(mayor100//menor10)+" veces en el numero "+str(mayor100))

Ejercicio 12-Proyecto------------------------------------------------



nombre = input("Identificacion (nombre): " )
totalVentas = float(input("Precio total de ventas de este mes: "))
if totalVentas < 0:
    print("Ventas negativas, no recibe nada. Contacte con nosotros.")
else:
    print("Hola "+nombre+", tu comisión por ventas es de "+str(round((totalVentas*0.13),2))+"€")
"""


numero1= int(input("Introduce un numero entre 10 y 20: "))
if (numero1 >= 10) and (numero1 <= 20) :
    print("Gracias")
else:
    print("Respuesta incorrecta")












