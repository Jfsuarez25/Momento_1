import os 

#En este paso crearemos las dos bases de datos que almacenaran los usuarios y los prestamos
usuarios = {}
prestamos = []

# Limpiar consola
def limpiar_consola():  
    os.system('cls' if os.name == 'nt' else 'clear')  

# En esta funcion vamos a tener el registro de ususarios
def registrar_usuario():
    limpiar_consola ()
    numero_tarjeta = input("Ingrese el número de tarjeta del usuario: ")
    nombre = input("Ingrese el nombre del usuario: ")
    usuarios[numero_tarjeta] = {'nombre': nombre, 'contrasena': input("Ingrese la contraseña del usuario: ")}
    print(f"Usuario registrado: {nombre} (Tarjeta: {numero_tarjeta})")

# En esta funcion iniciamos sesion con los datos anteriormente registrados
def iniciar_sesion():
    limpiar_consola()
    numero_tarjeta = input("Ingrese el número de tarjeta del usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    if numero_tarjeta in usuarios and usuarios[numero_tarjeta]['contrasena'] == contrasena:
        print(f"Sesión iniciada para el usuario: {usuarios[numero_tarjeta]['nombre']}")
        return numero_tarjeta
    else:
        print("\nInicio de sesión fallido. Verifique el número de tarjeta y la contraseña.")

# Función para que un usuario tome una bicicleta
def tomar_bicicleta(numero_tarjeta):
    origen = input("Ingrese el origen del viaje: ")
    destino = input("Ingrese el destino del viaje: ")
    prestamos.append({
        'usuario': usuarios[numero_tarjeta]['nombre'],
        'origen': origen,
        'destino': destino
    })
    print(f"{usuarios[numero_tarjeta]['nombre']} ha tomado una bicicleta desde {origen} hasta {destino}")

# Función para consultar el listado de usuarios
def consultar_listado_usuarios():
    print("Listado de Usuarios:")
    for numero_tarjeta, datos in usuarios.items():
        print(f"Tarjeta: {numero_tarjeta}, Nombre: {datos['nombre']}")

# Función para consultar el listado de préstamos
def consultar_listado_prestamos():
    print("Listado de Préstamos:")
    for prestamo in prestamos:
        print(f"\nUsuario: {prestamo['usuario']}, Origen: {prestamo['origen']}, Destino: {prestamo['destino']}")

# Loop principal de la aplicación
while True:
    print("\n" + " --¡SOMOS GW RENTA TU BICI!--")
    print("1. Registrar Usuario")
    print("2. Iniciar Sesión")
    print("3. Salir")
    print(" ------------- 🚲 --------------- \n")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':

        
        numero_tarjeta = iniciar_sesion()
        
        if numero_tarjeta:
            while True:
                #Este es el menu de 
                print("\n🔥--MENU DE RENTA--🔥")
                print("1. Tomar Bicicleta")
                print("2. Consultar Listado de Usuarios")
                print("3. Consultar Listado de Préstamos")
                print("4. Cerrar Sesión")
                print(" ------------- 🚲 --------------- \n")
                
                
                opcion_usuario = input("Seleccione una opción: ")
                
                if opcion_usuario == '1':
                    limpiar_consola()
                    tomar_bicicleta(numero_tarjeta)
                    
                elif opcion_usuario == '2':
                    limpiar_consola()
                    consultar_listado_usuarios()
                    
                elif opcion_usuario == '3':
                    limpiar_consola()
                    consultar_listado_prestamos()
                    
                elif opcion_usuario == '4':
                    limpiar_consola()
                    print(f"Sesión cerrada para el usuario: {usuarios[numero_tarjeta]['nombre']}")
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción válida. ")
    elif opcion == '3':
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")