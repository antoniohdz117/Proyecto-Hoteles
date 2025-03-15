# Proyecto-Hoteles

Objetivo

DESCRIPCION
El sistema esta diseñado principalmente para hacer reservaciones en un hotel y que el sistema sea usado por los supervisores(gerente, recepcionista) para realizar estas reservaciones y ofrecer un mejor servico al cliente y hacer auditorias.

# INSTALACION 
1. Para este sistema se tendra que usar MySQL para el almacenamiento de los datos
   En este link podras descargar MySQL para el uso de la base de datos en cualquier manejador, solamente tendras que escoger tu Sistema operativo de preferencia          https://dev.mysql.com/downloads/installer/
2. Deberas descargar un IDE en nuestro caso te recomendamos hacer el uso de VSCode, o de cualquier otro IDE para ejecutar el programa
3. Descargar python la peniultma version en este caso 3.13.2 en el siguiente link https://www.python.org/downloads/
4. Instalar bibliotecas para el uso de la base de datos en la terminal de python con npm install pip install mysql-connector-python
5. Usar el codigo de gitHub para hacer uso del programa y ejecutarlo, el link del repositorio es el siguiente https://github.com/antoniohdz117/Proyecto-Hoteles

# USO
EL sistema contara con varias opciones para poder registrar reservaciones o a los clientes
1. Registrar un cliente
   El sistema te pedira datos para poder registrar un cliente con lo siguientes datos: nombre, correoElectronico, telefono y su direccion
2. Cambiar datos de un cliente: El sistema te permitira poder cambiar los datos de algun cliente como su telefono,, correo o su direccion
3. Buscar un cliente: El sistema puede hacerte una busqueda de algun cliente en caso de que el cliente no recuerde si esta registrado 
4. Mostrar habitaciones Disponibles: El sistema tiene un limite de 20 habitaciones y te dira si estan disponibles ESTA FUNCION ESTARA PROXIMANTE 
5. Mostrar habitaciones ocupadas: El sistema podra mostrarte las habitaciones que estan en uso 
6. Reservar una habitación: El sistema registrara la reservacion de un cliente para hospedarse, los datos que te pediran son los siguientes, fecha entrada, fecha salida, si sigue en curso o se cancelo antes, costo de la habitacion, el cliente, habitacion, Empleado que registro esa reservacion
7. cambiar una reservación. La reservacion puede cambiar como la fecha entrada, fecha salida, claramente tendria que cambiar el pago, el estado del pago, el cliente o la habitacion sin embargo tambien puede cambiar
8. Cancelar una reservación: Se peude cancelar la reservacion en estado de la reservacion como "C" en curso, "T" terminada, o se puede borar para no registrarla
9. Salir: funcion para salir del sistema sin embargo el sistema guardara los datos en la base de datos

