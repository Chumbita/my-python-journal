Proyecto 32
En este simple programa intercambiamos información, en este caso un "Hola Mundo" entre un cliente y un servidor. Para lograr esto se utilizó la librería sockets. Como primer paso creé el servidor definiendo la IP y puerto del mismo. Luego creé un socket con la familia IPv4 y con el protocolo TCP, asociamos el socke a la IP y el puerto del servidor. Por último manejamos la conexión de un solo cliente, en donde el servidor espera a que el cliente envíe algo, en este caso un mensaje de tamaño de 1 Kb y se lo devuelve.

En el programa del cliente el código es más simple, como primer paso creé el socket del cliente con la misma familia y protocolo que definimos para el servidor y luego nos conectamos al servidor especificando su dirección IP y puerto, y por último enviamos el mensaje, recibimos la respuesta del servidor e imprimimos el mensaje.


Project 32
In this simple program, we exchange information, in this case a "Hello World," between a client and a server. To achieve this, the sockets library was used. As a first step, I created the server by defining its IP and port. Then, I created a socket using the IPv4 family and the TCP protocol, and associated the socket with the server's IP and port. Lastly, we handled the connection of a single client, where the server waits for the client to send something, in this case a 1 KB message, and then sends it back.

In the client program, the code is simpler. As a first step, I created the client socket with the same family and protocol as we defined for the server, then we connected to the server by specifying its IP address and port. Finally, we sent the message, received the server's response, and printed the message.