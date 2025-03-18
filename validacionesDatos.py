def numerico():
    while True:
        try:
            numero = int(input("Ingresa el dato NUMERICO:"))
            return numero
        except ValueError or mysql.connector.errors.DatabaseError:
            print("Error: Ingresa un dato valido porfavor")
            

# lista = [(1,"fdsd","sdfsd",1,)]
# creacionBaseDatos.insercionTipoHabitacion(lista)