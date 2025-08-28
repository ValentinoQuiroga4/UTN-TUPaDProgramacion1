#TP_SECUENCIALES_QUIROGA_VALENTINO
#EJERCICIO_1
print("hola mundo")
#EJERCICIO_2
nombre=input("¿Cuál es tu nombre? ")
print(f"Hola", nombre)
#EJERCICIO_3
nombre=input("¿Cuál es tu nombre? ")
apellido=input("¿Cuál es tu apellido? ")
edad=input("¿Cuál es tu edad? ")
residencia=input("¿Dónde resides?")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
#EJERCICIO_4
import math
# Solicitar al usuario el radio del círculo
radio = float(input("Introduce el radio del círculo: "))
# Calcular el área y el perímetro
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Área del círculo: {area}")
print(f"Perímetro del círculo: {perimetro:}")
#EJERCICIO_5
segundos=int(input("Ingrese la cant. de segundos:"))
horas = segundos // 3600
print(f"la cantidad de horas es: {horas}")
#EJERCICIO_6
num=(int(input("Ingrese un número:")))
print(f"{num} * 1 = {num*1}")
print(f"{num} * 2 = {num*2}")
print(f"{num} * 3 = {num*3}")
print(f"{num} * 4 = {num*4}")
print(f"{num} * 5 = {num*5}")
print(f"{num} * 6 = {num*6}")
print(f"{num} * 7 = {num*7}")
print(f"{num} * 8 = {num*8}")
print(f"{num} * 9 = {num*9}")
print(f"{num} * 10 = {num*10}")
#EJERCICIO_7
num1=(int(input("Ingrese el primer número:")))
num2=(int(input("Ingrese el segundo número:")))
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} / {num2} = {num1/num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} - {num2} = {num1-num2}")
#EJERCICIO_8
peso=float(input("Ingrese el peso (en kg):"))
altura=float(input("Ingrese la altura (m)"))
imc= peso / (altura ** 2)
print(f("El índice de masa corporal es de: {imc}"))
#EJERCICIO_9
celsius=float(input("Ingrese los grados Celsius:"))
fahrenheit=(celsius * 1.8) + 32
print("El equivalente en grados Fahrenheit es:",fahrenheit)
#EJERCICIO_10
num1=(int(input("Ingrese el primer número:")))
num2=(int(input("Ingrese el segundo número:")))
num3=(int(input("Ingrese el tercer número:")))
promedio=(num1+num2+num3)/3
print("El promedio de los tres números es:",promedio)