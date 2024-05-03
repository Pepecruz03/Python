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
diccionario= {
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

#Condicionales
#If
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")
#Elif
dia = 1
if dia == 1:
  print("Lunes")
elif dia == 2:
  print("Martes")
elif dia == 3:
  print("Miercoles")
else:
  print("Otro dia")

#Scope y variables

def hola_mundo():
  texto = "Hola Mundo"
  print(texto)

hola_mundo()
#print(texto) #Error

#variables globales
texto = "Hola Mundo"

def hola_mundo2():
  print(texto)

hola_mundo2()

#Funciones con parametros
def saludar(nombre = "Mundo"):
  return f"Hola {nombre}"

print(saludar("Juan"))

#Funciones con parametros opcionales
def saludar2(nombre = None):
  if nombre is None:
    return "Hola Mundo"
  else:
    return f"Hola {nombre}"
  
print(saludar2())

#Metodos de string
nombre = "Juan"
print(nombre.upper())
print(nombre.lower())
print(nombre.capitalize())
print(nombre.count("a"))
print(nombre.replace("a", "e"))
print(nombre.split("a"))
print(nombre.find("a"))
print(nombre.isdigit())
print(nombre.isalpha())
print(nombre.isalnum())
print(nombre.isupper())
print(nombre.islower())
print(nombre.istitle())
#Funcion
print(len(nombre))

#Metodos de listas
lista = [10, 20, 30, 40]
print(lista)
#agregar un elemento al final de la lista
lista.append(50)
print(lista)
#agregar un elemento en una posicion especifica
lista.insert(2, 25)
print(lista)
#eliminar un elemento de la lista (por indice)
lista.pop()
print(lista)
#Elimina el primer elemento que coincida con el valor
lista.remove(20)
print(lista)
#Revertir la lista
lista.reverse()
print(lista)
#Vacia la lista
lista.clear()
print(lista)
#Ordenar la lista
lista.sort()
print(lista)
#Devolver el indice de un elemento
print(lista.index(30))
#Contar cuantas veces aparece un elemento
print(lista.count(30))

#Metodos de diccionarios
diccionario = {
  "nombre": "Juan",
  "edad": 30
}
print(diccionario)
#Devuelve las claves
print(diccionario.keys())
#Devuelve los valores
print(diccionario.values())
#Devuelve los elementos
print(diccionario.items())
#Devuelve el valor de una clave
print(diccionario.get("nombre"))
#diccionario["nombre"]
#Agregar un elemento
diccionario["pais"] = "Mexico"
print(diccionario)
#Eliminar un elemento
diccionario.pop("pais")
print(diccionario)
#Eliminar el ultimo elemento
diccionario.popitem()
print(diccionario)
#Copiar un diccionario
diccionario2 = diccionario.copy()
print(diccionario2)
#Limpiar un diccionario
diccionario.clear()

#Metodos de tuples
tupla = (10, 20, 30, 40)
print(tupla)
#Devuelve el numero de veces que aparece un elemento
print(tupla.count(30))
#Devuelve el indice de un elemento
print(tupla.index(30))

#Bucles
lista = [10, 20, 30, 40]
for elemento in lista:
  print(elemento)

for i in range(0, 10):
  print(i)

i = 0
while i < 10:
  print(i)
  i += 1

