import mysql.connector

conexion = mysql.connector.connect(
    user="root", 
    password="halo 117", 
    host="localhost", 
    database="hotel")

if conexion.is_connected():
    print("Conexión exitosa")
    

user = ["antonio"]
password = ["12345"]


#Función para el inicio de sesión
def login():
    print("Inicio de sesión")

    validar = 1
    while validar < 3:
        usuario = input("Ingrese su usuario: ")
        contrasenia = input("Ingrese su contraseña: ")
        print(usuario in user)
        print(contrasenia in password)
                
        if (usuario in user  and contrasenia in password):
            print("Bienvenido al sistema")
            break
        else:
            print("Usuario o contraseña incorrecta")
            validar +=1
            if validar == 3:
                print("Número de intentos excedidos")
                exit()
                

#funcion para registrar un cliente
def registrarCliente():
    nombre = input("Ingrese el nombre del cliente: ")
    paterno = input("Ingrese el apellido  paterno del cliente: ")
    materno = input("Ingrese el apellido materno del cliente: ")
    edad = input("Ingrese la edad del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    email = input("Ingrese el email del cliente: ")
    direccion = input("Ingrese el correo del cliente: ")
    cur = conexion.cursor()
    cur.execute("INSERT INTO cliente (nombre, paterno, materno, edad, telefono, email, direccion) VALUES (%s, %s, %s, %s, %s, %s, %s)", (nombre, paterno, materno, edad, telefono, email, direccion))
    conexion.commit()
    print("Cliente registrado con éxito")



def buscarCliente():
    nombre = input("Ingrese el nombre del cliente: ")
    cur = conexion.cursor()
    cur.execute("SELECT * FROM cliente WHERE nombre = %s", (nombre,))
    cliente = cur.fetchone()
    if cliente:
        print("Nombre:", cliente[1])
        print("Apellido paterno:", cliente[2])
        print("Apellido materno:", cliente[3])
        print("Edad:", cliente[4])
        print("Teléfono:", cliente[5])
        print("Email:", cliente[6])
        print("Dirección:", cliente[7])
    else:
        print("Cliente no encontrado")

#funcion para mostrar las habitaciones disponibles    
def mostrarHabitaciones():
    
    
    
    
    
#funcion para mostrar las habitaciones disponibles    
def ReservarHabitacion():
    print("Habitaciones")
    print("1. Habitación sencilla")
    print("2. Habitación doble")
    print("3. Habitación triple")
    print("4. Suite")
    print("5. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Habitación sencilla")
    elif opcion == "2":
        print("Habitación doble")
    elif opcion == "3":
        print("Habitación triple")
    elif opcion == "4":
        print("Suite")
    elif opcion == "5":
        menuPrincipal()
    else:
        print("Opción no válida")
        mostrarHabitaciones()

def reservarHabitacion():
    nombre = input("Ingrese el nombre del cliente: ")
    paterno = input("Ingrese el apellido  paterno del cliente: ")
    materno = input("Ingrese el apellido materno del cliente: ")
    habitacion = input("Ingrese el tipo de habitación: ")
    #fecha = input("Ingrese la fecha de ingreso: ") <- este dato se genera automaticamente
    fechaSalida = input("Ingrese la fecha de salida:  en formato dd/mm/aaaa") 
    
    
    
 
    
def menuPrincipal():
    print("Menú principal")
    print("Elige un numero para realizar una acción")
    print("1. Registrar un cliente")
    print("2. Buscar un cliente")
    print("3. Mostrar habitaciones Disponibles")
    print("4. Reservar una habitación")
    print("5. Cancelar una reservación")
    print("6. Salir")
    while True:
        try:
            opcion = int(input("Seleccione un número (1-5): "))
            if 1 <= opcion <= 6:
                break
            else:
                print("Error: El número debe estar entre 1 y 5.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")
        
    return opcion
  

while True:
    opcion = menuPrincipal()
    if opcion == 1:
        print("Registrar un cliente")
    elif opcion == 2:
        print("Buscar un cliente")
    elif opcion == 3:
        mostrarHabitaciones()
    elif opcion == 4:
        reservarHabitacion()
    elif opcion == 5:
        print("Cancelar una reservación")
    elif opcion == 6:
        print("Salir")
        break
    