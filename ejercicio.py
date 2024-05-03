import os
import re

# Función para agregar un usuario
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
        print("1. Regstrar Usuario")
        print("2. Ver Registro")
        print("3. Buscar Correo Electronico")
        print("4. Actualizar Registro")
        print("5. Eliminar Registro")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")    
        if opcion == '1':
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            correo = input("Ingrese correo electrónico: ")
            telefono = input("Ingrese teléfono: ")
            agregar_usuario(nombre, apellido, correo, telefono)
            ejecutar_opciones()

        elif opcion == '2': # Función para mostrar todos los usuarios
            mostrar_usuarios()
            ejecutar_opciones()
            
        elif opcion == '3':
            correo = input("Ingrese el correo a filtrar: ")
            print("\n--- FILTRADO POR CORREO ---")
            filtrar_por_correo(correo)
            ejecutar_opciones()
        elif opcion == '4': 
            correo = input("Ingrese el correo del usuario a actualizar: ")
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            telefono = input("Ingrese el nuevo teléfono: ")
            actualizar_usuario(correo, nombre, apellido, telefono)
            ejecutar_opciones()

        elif opcion == '5':
            correo = input("Ingrese el correo del usuario a borrar: ")
            borrar_usuario(correo)
            ejecutar_opciones()
        elif opcion == '6':
            print("Hasta pronto")
            break
        else:   
            print("Opción inválida. Por favor, elige una opción de la lista.")
def agregar_usuario(nombre, apellido, correo, telefono):
    if not validar_correo(correo):
        print("Correo electrónico inválido.")
        return False

    # Verificar si el correo ya existe en el archivo
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as file:
            for line in file:
                if correo in line:
                    print("El correo electrónico ya se encuentra registrado.")
                    return False
                    

    # Si el archivo no existe, crearlo
    else:
        with open("usuarios.txt", "w") as file:
            pass  # Crear archivo vacío si no existe

    # Agregar el usuario al archivo
    with open("usuarios.txt", "a") as file:
        file.write(f"{nombre},{apellido},{correo},{telefono}\n")
    print("Usuario agregado exitosamente.")
    return True

def mostrar_usuarios():
                with open("usuarios.txt", "r") as file:
                    for line in file:
                        print(line.strip())
def filtrar_por_correo(correo):
    with open("usuarios.txt", "r") as file:
        for line in file:
            if correo in line:
                print(line.strip())

# Función para actualizar un usuario por correo electrónico
def actualizar_usuario(correo, nombre, apellido, telefono):
    with open("usuarios.txt", "r") as file:
        lines = file.readlines()
        with open("usuarios.txt", "w") as file:
            for line in lines:
                if correo in line:
                    file.write(f"{nombre},{apellido},{correo},{telefono}\n")
                else:
                    file.write(line)
                    print("Usuario actualizado exitosamente.")

# Función para borrar un usuario por correo electrónico
def borrar_usuario(correo): 
    with open("usuarios.txt", "r") as file:
        lines = file.readlines()
        with open("usuarios.txt", "w") as file:
            for line in lines:
                if correo not in line:
                    file.write(line)
                    print("Usuario eliminado exitosamente.")


# Llamar a la función para iniciarla
ejecutar_opciones()