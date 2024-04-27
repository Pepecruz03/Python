#Esto es un comentario de una linea
'''
Esto es un comentario de
varias lineas
'''
#Variables
hola = "Hola Mundo"
print(hola)

#Tipos de datos
#String
nombre = "Juan"
print(nombre)
#Entero
numero = 10
print(numero)
#Decimal
numero_decimal = 10.5
print(numero_decimal)
#Boolean
verdadero = True
falso = False
print(verdadero)
print(falso)
#Listas
lista = [10, 20, 30, 40]
print(lista)
#Tuplas
tupla = (10, 20, 30, 40)
print(tupla)
#Diccionarios
diccionario = {
  "nombre": "Juan",
  "edad": 30
}
print(diccionario)
#None
nada = None
print(nada)

#Operadores de asignacion
edad = 55
print(edad)
edad += 5
print(edad)
edad -= 5
print(edad)
edad *= 5
print(edad)
edad /= 5
print(edad)

#Operadores aritmeticos
numero1 = 77
numero2 = 44
print(numero1 + numero2)
print(numero1 - numero2)
print(numero1 * numero2)
print(numero1 / numero2)
print(numero1 % numero2)

#Operadores logicos
print(numero1 == numero2)
print(numero1 != numero2)
print(numero1 > numero2)
print(numero1 < numero2)
print(numero1 >= numero2)
print(numero1 <= numero2)
#And
print(numero1 > numero2 and numero1 < numero2)
#Or
print(numero1 > numero2 or numero1 < numero2)
#Not
print(not(numero1 > numero2))

#input
nombre = input("Cual es tu nombre? ")
print(nombre)

#Concatenacion y F-strings
nombre = "Juan"
edad = 30
print("Hola me llamo " + nombre + " y tengo " + str(edad) + " años")