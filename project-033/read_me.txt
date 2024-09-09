Proyecto 34
En este proyecto seguí trabajando con sockets, pero ahora utilizando headers. Definí un header de 64 bytes, y posteriormente ajusto el tamaño del mensaje a recibir de acuerdo al tamaño que me envió el cliente. Esto me permite recibir por parte del cliente mensajes de tamaño variable. 

El cliente por su parte, primero me envía el tamaño de del mensaje que desea enviar y luego el mensaje en sí. Enviar el tamaño del mensaje primero le permite al servidor modificar el tamaño del mensaje que espera recibir y de esta manera trabajar más eficientemente. 


Project 34
In this project, I continued working with sockets, but now utilizing headers. I defined a 64-byte header and subsequently adjusted the size of the message to be received according to the size sent by the client. This allows me to receive variable-sized messages from the client.

On the client's side, it first sends the size of the message it wants to send, and then the message itself. Sending the message size first allows the server to modify the expected message size and work more efficiently.