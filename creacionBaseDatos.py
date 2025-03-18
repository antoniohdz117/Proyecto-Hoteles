import mysql.connector

def creacionBaseDatos():
    try:
        # Conexión al servidor de MySQL (cambia usuario y contraseña)
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='halo 117'
        )
        cursor = conexion.cursor()

        # Validar si la base de datos existe
        cursor.execute("CREATE DATABASE IF NOT EXISTS hotel;")
        cursor.execute("USE hotel;")

        # Codigo sql en orden para ejecutarse
        tablas = [
            """CREATE TABLE tipoEmpleado(
                idTipoEmpleado INT AUTO_INCREMENT NOT NULL,
                puesto VARCHAR(255) NOT NULL,
                CONSTRAINT pkTipoEmpleado PRIMARY KEY (idTipoEmpleado)
            );""",

            """CREATE TABLE tipoHabitacion(
                idTipoHabitacion INT AUTO_INCREMENT NOT NULL,
                habitacion VARCHAR(255) NOT NULL,
                precio DECIMAL(6,1) NOT NULL,
                descripcion VARCHAR(255) NOT NULL,
                capacidad INT NOT NULL,
                CONSTRAINT pkTipoHabitacion PRIMARY KEY (idTipoHabitacion)
            );""",

            """CREATE TABLE cliente(
                idCliente INT AUTO_INCREMENT NOT NULL,
                nombre VARCHAR(255) NOT NULL,
                correoElectronico VARCHAR(255) NOT NULL,
                telefono CHAR(10) NOT NULL,
                direccion VARCHAR(255) NOT NULL,
                CONSTRAINT pkCliente PRIMARY KEY (idCliente)
            );""",

            """CREATE TABLE habitacion(
                idHabitacion INT AUTO_INCREMENT NOT NULL,
                numeroHabitacion INT NOT NULL,
                estado CHAR(1) NOT NULL,
                idTipoHabitacion INT NULL,
                CONSTRAINT pkHabitacion PRIMARY KEY (idHabitacion),
                CONSTRAINT fkHabitacionTipoHabitacion FOREIGN KEY (idTipoHabitacion)
                    REFERENCES tipoHabitacion(idTipoHabitacion)
                    ON DELETE CASCADE 
                    ON UPDATE CASCADE
            );""",

            """CREATE TABLE empleado(
                idEmpleado INT AUTO_INCREMENT NOT NULL,
                nombre VARCHAR(40) NOT NULL,
                turno CHAR(1) NOT NULL,
                salario INT NOT NULL,
                idTipoEmpleado INT NOT NULL,
                CONSTRAINT pkEmpleado PRIMARY KEY (idEmpleado),
                CONSTRAINT fkEmpleadoTipoEmpleado FOREIGN KEY (idTipoEmpleado)
                    REFERENCES tipoEmpleado(idTipoEmpleado)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            );""",

            """CREATE TABLE reservacion(
                idReservacion INT AUTO_INCREMENT NOT NULL,
                fechaEntrada DATE NOT NULL,
                fechaSalida DATE NOT NULL,
                estado CHAR(1) NOT NULL,
                pago INT NOT NULL,
                idCliente INT NOT NULL,
                idHabitacion INT NOT NULL,
                idEmpleado INT NOT NULL,
                CONSTRAINT pkReservacion PRIMARY KEY (idReservacion),
                CONSTRAINT fkReservacionCliente FOREIGN KEY (idCliente)
                    REFERENCES cliente(idCliente)
                    ON DELETE RESTRICT
                    ON UPDATE CASCADE,
                CONSTRAINT fkReservacionHabitacion FOREIGN KEY (idHabitacion)
                    REFERENCES habitacion(idHabitacion)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE,
                CONSTRAINT fkReservacionEmpleado FOREIGN KEY (idEmpleado)
                    REFERENCES empleado(idEmpleado)
                    ON DELETE RESTRICT
                    ON UPDATE CASCADE
            );"""
            ]

        #iteracion para la creacion de mis tablas empezando con las padres, padres e hijos y por ultimo los hijos
        for tabla in tablas:
            cursor.execute(tabla)


        print("Carga de base de datos exitosa.")
        insercionTipoEmpleado(tipoEmpleado)
        insercionEmpleado(empleado)
        insercionTipoHabitacion(tipoHabitacion)
        insercionHabitacion(habitacion)
        insercionCliente(cliente)
        insercionReservacion(reservacion)

    except mysql.connector.Error as error:
        print(f" Error al conectar con MySQL: {error}")

def conexionBaseDatos():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root", #ingrese su usuario
        password="halo 117", #ingrese su password
        database="hotel"
        )
    return conexion
    
#funcion para validar la existencia de la base de datos, Cree otra funcion para las pruebas unitarias del usario
def validarExistencia(baseDatos="hotel"):
    #try para la validacion de la base de datos existente
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',        #Cambiar usuario si es necesario
            password='halo 117' #cambia tu contraseña
        )
        #cursor para la conexion
        cursor = conexion.cursor()

        #usamos una consulta del SCHEMA_NAME para validar la existencia de la base de datos
        cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{baseDatos}';")
        resultado = cursor.fetchone()

        #CONDICION PARA REGRESAR UN TRUE O FALSE
        if resultado:
            print(f"La base de datos '{baseDatos}' ya esta creada.")
            return True
        else:
            print(f"La base de datos '{baseDatos}' no ha sido creada.")
            creacionBaseDatos()
            return False

    #excepcion si no se logro una conexion con la base de datos correctamente y dar un mensaje de error
    except mysql.connector.Error as error:
        print(f"Error al conectar con MySQL: Verifique su usario, contraseña o el error: {error}")
        exit()
        return False

def insercionTipoEmpleado(lista):

	#ESTO ME LO PUEDO AHORRAR PERO NO TUVE TIEMPO
    conexion = conexionBaseDatos()
    cursor = conexion.cursor()
    # Insert INTO
    query = """INSERT INTO tipoEmpleado (puesto) 
               VALUES (%s)"""
    # Insertar los datos
    cursor.executemany(query, lista)
    conexion.commit()
    print(cursor.rowcount, "Filas insertadas correctamente")	
 

def insercionTipoHabitacion(lista):

	#ESTO ME LO PUEDO AHORRAR PERO NO TUVE TIEMPO
    conexion = conexionBaseDatos()
    cursor = conexion.cursor()
    # Insert INTO
    query = """INSERT INTO tipoHabitacion (habitacion, precio, descripcion, capacidad) 
               VALUES (%s, %s, %s, %s)"""
               
    # Insertar los datos y confirmar la insercion
    cursor.executemany(query, lista)
    conexion.commit()

def insercionEmpleado(lista):
	#ESTO ME LO PUEDO AHORRAR PERO NO TUVE TIEMPO
    conexion = conexionBaseDatos()

    cursor = conexion.cursor()
    # Insert INTO
    query = """INSERT INTO empleado(nombre, turno, salario, idTipoEmpleado) 
               VALUES (%s,%s,%s,%s)"""
               
               
    # Insertar los datos y confirmar la insercion
    cursor.executemany(query, lista)
    conexion.commit()
    
def insercionHabitacion(lista):
	#ESTO ME LO PUEDO AHORRAR PERO NO TUVE TIEMPO
    conexion = conexionBaseDatos()
    cursor = conexion.cursor()
    # Insert INTO
    query = """INSERT INTO Habitacion(numeroHabitacion, estado, idTipoHabitacion) 
               VALUES (%s, %s, %s)"""
               
               
    # Insertar los datos y confirmar la insercion
    cursor.executemany(query, lista)
    conexion.commit()

def insercionCliente(lista):

	#ESTO ME LO PUEDO AHORRAR PERO NO TUVE TIEMPO
    conexion = conexionBaseDatos()
    cursor = conexion.cursor()
    # Insert INTO
    query = """INSERT INTO cliente(nombre, correoElectronico, telefono, direccion) 
               VALUES (%s, %s,%s,%s)"""  
    cursor.executemany(query, lista)
    conexion.commit()  
             
           
def insercionReservacion(lista):

	#ESTO ME LO PUEDO AHORRAR PERO NO TUVE TIEMPO
    conexion = conexionBaseDatos()
    cursor = conexion.cursor()
    # Insert INTO
    query = """INSERT INTO Reservacion(fechaEntrada, fechaSalida, estado, pago, idCliente, idHabitacion, idEmpleado) 
               VALUES (%s,%s,%s,%s,%s,%s,%s)"""
               
               
    # Insertar los datos y confirmar la insercion
    cursor.executemany(query, lista)
    conexion.commit()

#funcion para conseguir el precio de la habitacion tomando en cuenta el tipo de habitacion y los dias de estancia
def conseguirPrecio(idHabitacion,dias):
    #conexion a la base
    conexion = conexionBaseDatos()
    #cursor para ejecutar la consulta
    cursor = conexion.cursor()
    #consulta sql con parametro
    query = """
        SELECT tp.precio
        FROM tipoHabitacion AS tp
        INNER JOIN habitacion AS H ON tp.idTipoHabitacion = H.idHabitacion
        WHERE H.idHabitacion = %s
        """
    #ejecutar la consulta con el id ingresado por el usuario
    cursor.execute(query,(idHabitacion,))
    resultado = cursor.fetchone()
    #extraer el precio en una variable (si hay resultados)
    precio = resultado[0] if resultado else None
    
    precio = precio * dias 
    print(f"El precio de la habitacion seria: {precio}")
    return precio



#datos para la inertar en las tablas
#tioEmpleado
tipoEmpleado = [
	("Recepcionista",),
	("Limpieza",),
	("Mantenimiento",),
	("Gerente",),
	("Cocinero",)
]
#tipoHabitacion
tipoHabitacion = [
	("Sencilla", 500.0, "Habitación sencilla con una cama", 1,),
	("Doble", 800.0, "Habitación doble con dos camas", 2,),
	("Suite", 1200.0, "Habitación suite con cama king size", 2,),
	("Presidencial", 2000.0, "Habitación presidencial con cama king size y jacuzzi", 2,)
]
#empleado
empleado =[
	("David Ceballos Loli ", "M", 10000, 1,),
	("Ernesto Hernandez Gonzalez", "V", 8000, 2,),
	("Oscar Alberto Perez", "M", 9000, 3,),
	("Diego Soriano Gonzalez", "V", 15000, 4,),
	("Jose Luis Perez", "N", 12000, 5,)
]
#habitacion
habitacion = [
	(101, "D", 1,),
	(102, "O", 2,),
	(103, "O", 2,),
	(104, "O", 2,),
	(105, "D", 2,)
]

#cliente
cliente = [
	("Antonio Hernandez Berrios", "antonio117.berrios@gmail.com", "5544658682", "Calle 1 #123"),
]
#reservacion
reservacion =[
	("2021-07-01", "2021-07-05", "P", 5000, 1, 1, 1,),
	("2021-07-01", "2021-07-05", "P", 8000, 1, 2, 4,),
	("2021-07-01", "2021-07-05", "P", 12000, 1, 3, 1,),
	("2021-07-01", "2021-07-05", "P", 20000, 1, 4, 4,)
]
    
if not validarExistencia():
    print("Ejecucion terminada")
else:
    print("La base de datos ya está creada en el sistema.")
    print("Iniciando conexion a la base")
    conexion = conexionBaseDatos()
    cursor = conexion.cursor()
    cursor.execute("USE hotel;")
    cursor.close()
    conexion.close()
    print("Conexion establecida")
    



