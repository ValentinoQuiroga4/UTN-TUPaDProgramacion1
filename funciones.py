#TP_FUNCIONES

#QUIROGA_VALENTINO_NICOLÁS

#EJERCICIO_1
def imprimir_hola_mundo ():
    return "Hola mundo"
saludo = imprimir_hola_mundo ()
print(saludo)

#EJERCICIO_2
def saludar_usuario(nombre):
    return "Hola " + nombre + "!"
nombre = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)

#EJERCICIO_3

def informacion_personal(nombre,apellido,edad,residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."
nombre = input("Ingrese su nombre")
apellido = input("Ingrese su apellido")
edad = input("Ingrese su edad")
residencia = input("Ingrese su residencia")
info = informacion_personal(nombre,apellido,edad,residencia)
print(info)

#EJERCICIO_4

import math 
def calcular_area_circulo(radio): 
    return math.pi * radio ** 2 

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio"))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo es: {area}")
print(f"El perimetro del círculo es: {perimetro}")

#EJERCICIO_5

def segundos_a_horas(segundos):
    return segundos // 3600

segundos = float(input("Ingrese la cantidad de segundos: "))

horas = segundos_a_horas(segundos)

print(f"Equivale a {horas} horas.")

#EJERCICIO_6

def tabla_multiplicar(num):
    for i in range(1,11):
     print(f"{num} * {i} = {num * i} ")

num = int(input("Ingrese un número"))

tabla = tabla_multiplicar(num)
print(tabla)

#EJERCICIO_7
def operaciones_basicas(num1, num2):
    print(F"Suma: {num1} + {num2} = {num1 + num2}")
    print(F"Resta: {num1} - {num2} = {num1 - num2}")
    print(F"Multiplicación: {num1} * {num2} = {num1 * num2}")
    print(F"División: {num1} / {num2} = {num1 / num2}")

num1 = int(input("Ingrese el primer número:"))
num2 = int(input("Ingrese el segundo número:"))

operaciones = operaciones_basicas(num1,num2)

#EJERCICIO_8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

resultado = calcular_imc(peso, altura)
print(f"Su IMC es: {resultado:.2f}")

#EJERCICIO_9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

resultado = celsius_a_fahrenheit(celsius)

print(f"{celsius}°C equivalen a {resultado:.2f}°F")

#EJERCICIO_10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
 
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

resultado = calcular_promedio(a, b, c)

print(f"El promedio de los tres números es: {resultado:.2f}")









