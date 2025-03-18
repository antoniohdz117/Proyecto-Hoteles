import mysql.connector
from datetime import datetime
import creacionBaseDatos
from validacionesDatos import numerico
import funciones as fun
import os


def conexionBaseDatos():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root", #ingrese su usuario
        password="halo 117", #ingrese su password
        database="hotel"
        )
    return conexion


def limpiarTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
#funcion para mkostrar las reservaciones
def mostrarReservaciones():
    conexion = conexionBaseDatos()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM reservacion")
    reservaciones = cursor.fetchall()
    
    print("Reservaciones Hechas")
    for reservacion in reservaciones:
        print("\n---------------------------------------------------------------------------------")
        print("\n   ID")
        print ('|',reservacion, end='|')
    print("\n---------------------------------------------------------------------------------")
    cursor.close()
    conexion.close()  


        
#funcion para registrar un cliente    
def registrarCliente():
    nombre = input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el email del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    direccion = input("Ingrese la direccion del cliente: ")
    #guardo los datos en mi lista para mandarlos a la base de datos
    lista = [(nombre, email, telefono, direccion,)]
    creacionBaseDatos.insercionCliente(lista,)
    print("Cliente registrado con éxito")


#funcion para la busqueda de un cliente    
def buscarCliente():
    nombre = input("Ingrese el nombre del cliente: ")
    conexion = conexionBaseDatos()
    cur = conexion.cursor()
    cur.execute("SELECT * FROM cliente WHERE nombre REGEXP %s", (".*"+nombre+'*',))
    cliente = cur.fetchall()
    if cliente:
        for persona in cliente:
            print(persona)
            # print("ID: ",cliente[0])
            # print("Nombre:", cliente[1])
            # print("Teléfono:", cliente[2])
            # print("Email:", cliente[3])
            # print("Dirección:", cliente[4])
    else:
        print("Cliente no encontrado")

#funcion para hacer la reservacion del cliente
def reservarHabitacion():

    #input para los datos de reservacion
    fechaEntrada = datetime.today().date() #<- este dato se genera automaticamente
    while True:    
        fechaS = input("Ingresa la fecha SALIDA (YYYY-MM-DD): ")
        fechaSalida = datetime.strptime(fechaS, "%Y-%m-%d").date()
        if fechaSalida < fechaEntrada:
            print("Fecha incompatible, ingrese de nuevo la fecha ")
        else:
            break
    dias = (fechaSalida - fechaEntrada).days
    idHabitacion = int(input("Ingrese el id de la habitación: "))    
     
    #funcion para hacer la insersion del precio final de la habitacion
    pago = creacionBaseDatos.conseguirPrecio(idHabitacion,dias)
    estado = input("Ingrese el estado del pago P)Pagado D)Adeudo: ").upper()
    cliente = int(input("Ingrese el ID del cliente: "))
    #habitacion = int(input("Ingrese el ID  o numero de la habitación: "))
    Empleado = int(input("Ingrese el ID del empleado que atendio: "))
    
    #guardamos los datos en una lista para mandarlos a la base de datos
    lista = [(fechaEntrada, fechaSalida, estado, pago, cliente, idHabitacion, Empleado,)]
    print(lista)
    creacionBaseDatos.insercionReservacion(lista)


#Eliminacion de un registro de una reservacion
def eliminacionReservacion():
    print("Cual reservaciones sera eleminada?")
    mostrarReservaciones()
    print("Escribe el id de la reservacion que sera eliminada: ")
    registro = numerico()
    conexion = conexionBaseDatos()
    cursor = conexion.cursor()
    cursor.execute("""SELECT *
                        FROM reservacion
                        WHERE idReservacion = %s""", (registro,))
    resultado = cursor.fetchone()
    print("Desear eliminar el siguiente registro?   1)si    0)no")
    print(resultado)
    respuesta = numerico()
    if respuesta:
        cursor.execute("DELETE FROM reservacion WHERE idReservacion = %s", (registro,))
        #confirmacion de la eliminacion solamente para INSERT, UPDATE o DELETE
        conexion.commit()
        print("Registro eliminado con exito")
    else:
        print("Registro No eliminado")



def actualizarFechaSalida():
    try:
        # Conectar a MySQL
        conexion = conexionBaseDatos()
        cursor = conexion.cursor()
        
        mostrarReservaciones()
        # CONSULTA PARA HACER EL CALCULO DEL PAGO CUANDO CAMBIAMOS LA FECHA     
        # Valores a actualizar
        print("Ingresa el ID para cambiar la fecha de salida del registro")
        reservacion = numerico()
        cursor.execute("""SELECT fechaEntrada
                    FROM reservacion
                    WHERE idReservacion = %s
                """, (reservacion,))
        fechaEntrada = cursor.fetchone()[0]
        while True:
            
            fechaS = input("Ingresa la fecha  NUEVA (YYYY-MM-DD): ")
            fechaSalida = datetime.strptime(fechaS, "%Y-%m-%d").date()
            if fechaSalida < fechaEntrada:
                print("Fecha incompatible, ingrese de nuevo la fecha ")
            else:
                break
        dias = (fechaSalida - fechaEntrada).days

        #Query para conseguir el numero de habiacion
        
        cursor.execute("""SELECT idHabitacion
                    FROM reservacion
                    WHERE idReservacion = %s""",(reservacion,))
        idHabitacion = cursor.fetchone()[0]
        pago = creacionBaseDatos.conseguirPrecio(idHabitacion,dias)
        
    
        #CONSULTA 3 PARA HACER EL CAMBIO
        query = "UPDATE reservacion SET fechaSalida = %s, pago = %s WHERE idReservacion = %s"
        # Ejecutar la consulta
        cursor.execute(query, (fechaSalida, pago, reservacion))

        # Confirmar cambios en la base de datos
        conexion.commit()

        print("Registro actualizado correctamente.")

    except mysql.connector.Error as e:
        print("Error en la base de datos:", e)
        conexion.rollback() 

    
#FUNCION EXTRAIDA DE CHATGPT tenia dudas en en como hacer el cambio
def actualizarEstado():
    try:
        # Conectar a MySQL
        conexion = conexionBaseDatos()
        cursor = conexion.cursor()
        
        mostrarReservaciones()
        # Definir la consulta SQL
        query = "UPDATE reservacion SET estado = %s WHERE idReservacion = %s"

        # Valores a actualizar
        print("Ingresa el ID para cambiar el pago del registro")
        reservacion = numerico()
        nuevoValor = input("Ingresa su nuevo valor P)Pagado D)Debe pago: ")

        # Ejecutar la consulta
        cursor.execute(query, (nuevoValor, reservacion))

        # Confirmar cambios en la base de datos
        conexion.commit()

        print("Registro actualizado correctamente.")

    except mysql.connector.Error as e:
        print("Error en la base de datos:", e)
        conexion.rollback()  # Revertir cambios si hay error

    
    cursor.close()  # Cerrar el cursor
    conexion.close()  # Cerrar la conexión



def actualizarCliente():
    try:
        # Conectar a MySQL
        conexion = conexionBaseDatos()
        cursor = conexion.cursor()
        
        mostrarReservaciones()
        # Definir la consulta SQL
        query = "UPDATE reservacion SET idCliente = %s WHERE idReservacion = %s"

        # Valores a actualizar
        print("Ingresa el ID de la reservacion para cambiar el idCliente")
        reservacion = numerico()
        print("Ingrese el NUERVO idCliente: ")
        nuevoValor = numerico()

        # Ejecutar la consulta
        cursor.execute(query, (nuevoValor, reservacion))

        # Confirmar cambios en la base de datos
        conexion.commit()

        print("Registro actualizado correctamente.")

    except mysql.connector.Error as e:
        print("Error en la base de datos:", e)
        conexion.rollback()  # Revertir cambios si hay error

    
    cursor.close()  # Cerrar el cursor
    conexion.close()  # Cerrar la conexión
    
def actualizarHabitacion():
    try:
        mostrarReservaciones()
        conexion = conexionBaseDatos()
        cursor = conexion.cursor()
        print("Ingresa el ID de la reservacion que deseas cambiar: ")
        reservacion = numerico()
        cursor.execute("""SELECT fechaEntrada, FechaSalida
                       FROM reservacion
                       WHERE idReservacion = %s
                       """, (reservacion,))
        resultado = cursor.fetchone()
        if resultado:
            fechaEntrada, fechaSalida = resultado
            dias = (fechaSalida - fechaEntrada).days

            print("Ingrese la NUEVA habitacion")
            nuevaHabitacion = numerico()
            pago = creacionBaseDatos.conseguirPrecio(nuevaHabitacion,dias)
            query = """UPDATE reservacion 
                        SET idHabitacion = %s, pago = %s
                        WHERE idReservacion= %s"""
            cursor.execute(query,(nuevaHabitacion, pago, reservacion,))
            conexion.commit()
            print("Registro actualizado")
        else:
            print("Registro no encontrado")
            
        
    except mysql.connector.Error as e:
        print("Error en la base de datos:", e)
        conexion.rollback()
    cursor.close()  # Cerrar el cursor
    conexion.close()  # Cerrar la conexión 

def actualizarEmpleado():
    try:
        # Conectar a MySQL
        conexion = conexionBaseDatos()
        cursor = conexion.cursor()
        
        mostrarReservaciones()
        # Definir la consulta SQL
        query = "UPDATE reservacion SET idEmpleado = %s WHERE idReservacion = %s"

        # Valores a actualizar
        print("Ingresa el ID de la reservacion para cambiar el idEmpleado")
        reservacion = numerico()
        print("Ingrese el Empleado")
        nuevoValor = numerico()

        # Ejecutar la consulta
        cursor.execute(query, (nuevoValor, reservacion))

        # Confirmar cambios en la base de datos
        conexion.commit()

        print("Registro actualizado correctamente.")

    except mysql.connector.Error as e:
        print("Error en la base de datos:", e)
        conexion.rollback()  # Revertir cambios si hay error

    
    cursor.close()  # Cerrar el cursor
    conexion.close()  # Cerrar la conexió

def cambiarReservacion():
    print('Que deseas cambiar')
    print("1) Fecha Salida")
    print("2) Estado del pago:")
    print("3) Cliente de habitacion")
    print("4) Habitacion del cliente")
    print("5) Empleado que atendio")
    opcion = numerico()
    match opcion:
        case 1:
            print("Elegiste la opción 1")
            actualizarFechaSalida()
        case 2:
            print("Elegiste la opción 2")
            actualizarEstado()
        case 3:
            print("Elegiste la opción 3")
            actualizarHabitacion()
        case 4:
            print("Elegiste la opcion 4")
            actualizarCliente()
        case 5:
            print("Elegiste la opcion 5")
            actualizarEmpleado()
        case _:
            print("Opción no válida")
    

def menuPrincipal():
    print("Menú principal")
    print("Elige un numero para realizar una acción")
    print("1. Registrar un cliente")
    print("2. Buscar un cliente")
    print("3. Mostrar Reservaciones")
    print("4. Reservar una habitación")
    print("5. Cambiar una reservacion")
    print("6. Cancelar una reservación")
    print("7. Salir")
    while True:
        try:
            opcion = numerico()
            if 1 <= opcion <= 7:
                break
            else:
                print("Error: El número debe estar entre 1 y 7.")
        except ValueError:
            print("Error: Debe ingresar un número válido.")
    return opcion


def acciones():
    while True:
        opcion = menuPrincipal()
        if opcion == 1:
            print("Registrar un cliente")
            registrarCliente()
            limpiarTerminal()
        elif opcion == 2:
            print("Buscar un cliente")
            buscarCliente()
            espero = input("Enter para continuar: ")
            limpiarTerminal()
        elif opcion == 3:
            print("Mostrar Reservaciones")
            mostrarReservaciones()
            espera = input("presiona enter para continuar:")
            limpiarTerminal()
            #mostrarHabitaciones()
        elif opcion == 4:
            reservarHabitacion()
            limpiarTerminal()
        elif opcion == 5:
            cambiarReservacion()
            limpiarTerminal()
        elif opcion == 6:
            print("Eliminar una reservación")
            eliminacionReservacion()
            espera = input("Presiona enter para continuar")
            limpiarTerminal()
        elif opcion == 7:
            print("Salir")
            break
        
        