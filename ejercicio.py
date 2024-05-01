import re

print("Registro de usuarios:\nOpcion1 -Nuevo registro\nOpcion2-Mostrar usuarios")
opcion=int(input("selecione una opcion: "))
while not(opcion==1 or opcion==2):  
    print("Opcion no valida")
    opcion=(input("selecione una opcion: "))

if(opcion==1):
    archivo=open("Usuarios.txt","a")
    print("Bienvenido ingrese su nombre por favor")
    nombre=input(str())
    while not(len(nombre)>1):
        print("Ingrese un nombre valido")
        nombre=input()
    print("Ingrese su apellido por favor")
    apellido=input(str())
    while not(len(apellido)>1):
        print("Ingrese un apellido valido")
        apellido=input()
    print("Ingrese su correo por favor")
    correo=input()
    print("Ingrese su codigo de area mas su numero por favor (ejemplo +584141234567)")
    numero=input()
    while not(re.match(r"^\+?1?\d{9,15}$", numero)):
        print("Ingrese un numero valido")
        numero=input()
    archivo.write(nombre+", "+apellido+", " +correo+", "+numero+"\n")
    archivo.close()
else:
    (opcion==2)
    archivo=open("Usuarios.txt","r")
    print(archivo.read())
    archivo.close()