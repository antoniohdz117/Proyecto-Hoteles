# Proyecto-Hoteles

Objetivo

DESCRIPCION
El sistema esta diseñado principalmente para hacer reservaciones en un hotel y que el sistema sea usado por los supervisores(gerente, recepcionista) para realizar estas reservaciones y ofrecer un mejor servico al cliente y hacer auditorias.

# INSTALACION 
1. Para este sistema se tendra que usar MySQL para el almacenamiento de los datos
   En este link podras descargar MySQL para el uso de la base de datos en cualquier manejador, solamente tendras que escoger tu Sistema operativo de preferencia          https://dev.mysql.com/downloads/installer/
2. Deberas descargar un IDE en nuestro caso te recomendamos hacer el uso de VSCode, o de cualquier otro IDE para ejecutar el programa
3. Descargar python la peniultma version en este caso 3.13.2 en el siguiente link https://www.python.org/downloads/
4. Instalar bibliotecas para el uso de la base de datos en la terminal de python con npm install pip install mysql-connector-python o simplemente ejecuta el siguiente comando pip install -r requirements.txt para instalar todas las dependencias
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

NOTA: CABE RECALCAR QUE EL SISTEMA TENDRA VALIDACIONES PARA EL REGISTRO DE LOS DATOS SEAN DE ACUERDO PARA LA BASE DE DATOS

# PREGUNTAS 
Paso 1. Redacta un objetivo para tu proyecto, recuerda que tiene que
ser
1. Específico
2. Medible
3. Alcanzable
4. Relevante
5. Temporal
El punto de éstas preguntas es responder a la pregunta general: ¿Qué
vas a hacer?
Mi objetivo es realizar un sistema (CRUD) para gestionar las reservaciones de un Hotel


Paso 2. Es importante no sólo programar por programar, debe
existir siempre una razón detrás bien motivada1

1. En caso de haber escogido un juego, ¿por qué este juego y no
otro? ¿Qué habilidades te va a brindar este proyecto? ¿Por qué
programar un juego y no algo más útil como un visualizador de
datos?

Escogi un CRUD de gestion de reservaciones porque queria ver cual es mi limite con python sin el uso bibliotecas y tambien porquer queria aprender a usar ciertas funciones de python para el uso de una base de datos

3. En caso de haber escogido algo diferente a un juego, ¿en qué
contexto histórico surge el concepto que quieres modelar? ¿Para
qué quieres programarlo?
Ya he hecho varios CRUD con python sin embargo no queria hacer el mismo de siempre, queria hacer algo diferente como una base de datos y ademas queria enfretarme el problema de un sistema de negocio que afectan mucho como el cupo de las personas

En sí es responder a la pregunta general: ¿Por qué tu proyecto es
relevante?
Por que estos estoy enfretando el problema de una eficiencia operativa para la toma de decisiones en un hotel, si es rentable o no, rediccion de perdidas, y un mejor 
Paso 3. Habiendo redactado un objetivo, responde las siguientes
preguntas
1. ¿Qué quieres lograr con tu proyecto? ¿Qué problema o situación
estás respondiendo?
A la toma de decisiones de las reservaciones de un cliente para la toma de decisiones si un cliente, para el estudio de mercado posicionado el hotel si es para un uso de paso o para vacacionar
3. ¿Para quién estás programando? ¿Quién es el usuario final?
   El gerente o el recepcionista que ellos podran guardar las reservaciones incluso hacer el estudio de mercado
5. ¿Qué decisiones necesita tomar el programa para funcionar?
   Solament el uso de gestionar las reservaciones y los clientes
7. ¿De qué manera se puede romper el programa? ¿Cómo puedes
prevenir que el usuario hackeé tu programa? ¿Cómo puedes validar
los datos que te brinda el usuario?
He estado implementado valdiaciones para que no truene el programa con datos no validos, para hackear el programa solamente deberia tendra acceso al usario root para poder tronar el programa o alterarlo sin embargo hay bibliotecas de python que te ayudan a guardar datos de manera cifrada 

9. ¿Cómo puedes a prevenir los sesgos (racismo, sexismo, colonia-
lismo, discriminación a personas con discapacidades, etc.) en tu
proyecto?
Cualquier persona puede usarlo Segun bajo mi concepto tiene una interfaz grafica(terminal) amigable con el usuario
Estas son preguntas guías que tienen la intención de responder la
pregunta general: ¿Para quién estás trabajando?
Para mi desarrollo profesional

# CONTACTO
antonio117.berrios@gmail.com
# CREDITOS
Antonio Hernandez Berrios



