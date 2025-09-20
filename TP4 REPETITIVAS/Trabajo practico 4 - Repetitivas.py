#TRABAJO PRACTICO 4

#EJERCICIO 1

#Para la variable "numero" en el rango 101 porque cuenta desde 0 para que imprima desde el 0 al 100 linea por linea
for numero in range(101):
    print(numero)

#EJERCICIO 2

#Variables
#Cuenta la cantidad de digitos que ingreso el usuario usando len.
num = input("Ingrese un numero entero: ");
cantidad_digitos = len(num)

for num in range(cantidad_digitos):
    print(cantidad_digitos)
    break

#EJERCICIO 3

#Variables
num1 = int(input("Ingrese el primer numero: "));
num2 = int(input("Ingrese el segundo numero: "));

menor = min(num1, num2)
mayor = max(num1, num2)

suma = 0

for num3 in range(menor +1, mayor):
    suma += num3

print(f"La suma entre ambos numeros {menor} y {mayor} excluyendo los ingresados es {suma}")

#EJERCICIO 4

#Variable inicializada
suma1 = 0

print("Ingrese numeros enteros para ser sumados, ingrese cero para terminar: ")

while True:
    numeros_enteros = int(input("Numeros: "))

    if numeros_enteros == 0:
        break

    suma1 += numeros_enteros

print(f"La suma de los numeros ingresados es: {suma1}") 

#EJERCICIO 5

import random

numero_adivinar = random.randint(0, 9)
intentos = 0

print("Adivina el numero del 0 al 9.")

while True:
    adivinar = int(input("Ingrese su intento: "))
    intentos += 1
    if adivinar == numero_adivinar:
        print(f"Correcto has adivinado. El numero de intentos realizados fueron: {intentos}")
        break    
    else:
        print("Incorrecto, vuelva intentar.")

#EJERCICIO 6

for numero_rango in range(100, -2, -2):
    print(numero_rango)

#EJERCICIO 7 

numero_usuario = int(input("Ingrese un numero entero mayor que 0: "))

if numero_usuario <= 0:
    print("Debe ingresar un numero mayor a 0")
else:
    suma2 = sum(range(1, numero_usuario + 1))

print(f"La suma de los numeros entre 0 y {numero_usuario} es: {suma2}")

#EJERCICIO 8 

#Inicializar variables
pares = 0
impares = 0
positivos = 0
negativos = 0

#Cantidad de numeros a ingresar (puede remplazarse facilmente por 100)
cantidad = 5

#Intruccion para el usuario
print(f"Ingresa {cantidad} numeros enteros: ")

for i in range(cantidad):
    numero = int(input(f"Numero {i + 1}: "))
    #if para el par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    #if para positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

#Mostrar resultados
print("RESULTADOS:")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

#EJERCICIO 9

#Cantidad de numeros a ingresar (se puede cambiar facilmente por 100)
cantidad1 = 5

#Inicializar suma
suma3 = 0

#Intruccion para el usuario
print(f"Ingresa {cantidad1} numeros enteros para calcular la media.")

for a in range(cantidad1):
    num4 = int(input(f"Numero {a + 1}: "))
    suma3 += num4

#Calcula la media
media = suma3 / cantidad1

#Imprime resultado
print(f"La media de los {cantidad1} numeros ingresados es: {media}")

#EJERCICIO 10

#Pide al usuario ingrese el numero a invertir
invertir_numero = input("Ingresa un numero entero: ")

#Invierte el numero ingresado por el usuario sin especificar inicio, fin pero si -1 que indica de atras hacia delante.
invertido = invertir_numero[::-1]

#Imprimir numero invertido.
print(f"El numero {invertir_numero} ingresado por el usuario, invertido es: {invertido}")