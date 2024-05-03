import re
def validar_nombre(nombre):
    return bool(re.match(r'^[a-zA-Z]{3,}$', nombre))
# Solo letras y mínimo 3 caracteres
def validar_correo(correo):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo))
# Patrón básico de validación de correo electrónico
def validar_numero_telefono(telefono):
    return bool(re.match(r'^\+?[0-9]+$', telefono))
# Números y el signo más al principio opcional

def ejecutar_opciones():
    while True:
        # Aquí va la lógica de tu función que ejecuta opciones
        print("1. Regstrar Usuario")
        print("2. Ver Registro")
        print("Presiona 'q' para salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            archivo=open("Usuarios.txt","a")
            print("Bienvenido ingrese su nombre por favor")
            nombre=input(str())
            if validar_nombre(nombre):
                    print("Nombre válido")
            else:
                print("Nombre inválido")
                nombre=input()
            print("Ingrese su apellido por favor")
            apellido=input(str())
            if validar_nombre(apellido):
                    print("apellido válido")
            else:
                print("apellido inválido")
                apellido=input()
            print("Ingrese su correo por favor")
            correo=input()
            if validar_correo(correo):
                    print("Correo válido")
            else:
                print("Correo inválido")
                correo=input()
            print("Ingrese su codigo de area mas su numero por favor (ejemplo +584141234567)")
            numero=input()
            if validar_numero_telefono(numero):
                    print("Numero válido")
            else:
                print("Numero inválido")
                numero=input()
            archivo.write(nombre+", "+apellido+", " +correo+", "+numero+"\n")
            archivo.close()
            print("Registro exitoso")
            print("Desea regresar al menu principal?")
            print("1. Si")
            print("2. No")
            if input() == '1':
                continue
            else:
                print("Hasta pronto")
                break

                
        elif opcion == '2':
            print("Ejecutando opción 2")
            archivo=open("Usuarios.txt","r")
            print(archivo.read())
            archivo.close()
            print("Desea regresar al menu principal?")
            print("1. Si")
            print("2. No")
            if input() == '1':
                continue
            else:
                print("Hasta pronto")
                break
        elif opcion.lower() == 'q':
            print("Saliendo...")
            break  # Salir del bucle si el usuario elige 'q'
        else:
            print("Opción no válida")
            
# Llamar a la función para iniciarla
ejecutar_opciones()









