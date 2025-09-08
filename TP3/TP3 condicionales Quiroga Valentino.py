#EJERCICIO_1
edad = int(input("Ingrese su edad:"))
if edad >= 18:
    print("Eres mayor de edad")
#EJERCICIO_2
nota = int(input("Ingrese su nota:"))
if nota >= 6:
 print("APROBADO")
else:
 print("DESAPROBADO")
#EJERCICIO_3
num = int(input("Ingrese un número par:"))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
#EJERCICIO_4
edad = int(input("Ingrese su edad:"))
if edad < 12:
    print("Perteneces a la categoría NIÑO/A.")
elif edad >= 12 and edad < 18:
    print("Perteneces a la categoría adolescente.")
elif edad >= 18 and edad < 30:
    print("Perteneces a la categoría adulto/a jóven,")
elif edad >= 30:
    print("Perteneces a la categoría adulto.")
#EJERCICIO_5
contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
#EJERCICIO_6
import statistics 
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)
if media > mediana and mediana > moda:
   print(f"El sesgo es positivo.")
elif media < mediana and mediana < moda:
   print(f"El sesgo es negativo")
elif media == mediana and mediana == moda and moda == media:
   print(f"No hay sesgo")
#EJERCICIO_7
palabra = input("Ingrese una palabra")
if palabra and palabra[-1].lower() in 'aeiou':
   print(f"{palabra}!")
else: print("{palabra}")
#EJERCICIO_8
nombre = input("Ingresa tu nombre: ")
print("Elige una opción:")
print("1. Mostrar el nombre en MAYÚSCULAS")
print("2. Mostrar el nombre en minúsculas")
print("3. Mostrar el nombre con la Primera letra en mayúscula")
opcion = input("Ingresa el número de la opción (1, 2 o 3): ")
if opcion == "1":
    print("Nombre en mayúsculas:",nombre.upper())
elif opcion == "2":
   print("Nombre en minúsculas:",nombre.lower())
elif opcion == "3":
   print("Nombre con la primera letra en mayúscula:",nombre.title())
#EJERCICIO_9
magnitud = float(input("Ingrese la magnitud del terremoto"))
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")  
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala).")
#EJERCICIO_10
hemisferio = input("¿En qué hemisferio te encuentras?(N/S)")
mes = int(input ("Ingrese el mes:"))
dia = int(input("Ingrese el día"))
if hemisferio == "N" or "n":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("De acuerdo la fecha ingresada, estás en Invierno.")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("De acuerdo la fecha ingresada, estás en Primavera.")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print("De acuerdo la fecha ingresada, estás en Verano.")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print("De acuerdo la fecha ingresada, estás en Otoño.")
    else:
        print("Fecha no válida.")
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("De acuerdo la fecha ingresada, estás en Verano.")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("De acuerdo la fecha ingresada, estás en Otoño.")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print("De acuerdo la fecha ingresada, estás en Invierno.")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print("De acuerdo la fecha ingresada, estás en Primavera.")
    else:
        print("Fecha no válida.")
else:
    print("Hemisferio no válido.")