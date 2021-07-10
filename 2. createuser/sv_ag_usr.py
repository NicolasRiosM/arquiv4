import socket
import threading
from conect import *
 
PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1',PORT))
server.listen(1000)

def recibir(sock, addr):
    print("Creando un nuevo usuario")
    while True:
        datos = sock.recv(4096)
        if datos.decode('utf-8').find('agusr'):
            #decodificar el mensaje
            datos = datos[10:]
            target = datos.decode()
            data = target.split()
            
        consulta = f"INSERT INTO usuario (nombre, apellido, rut, pass, contacto, region, email) VALUES ('{data[0]}','{data[1]}','{data[2]}','{data[3]}','{data[4]}','{data[5]}','{data[6]}');"
        respuesta = modificar(consulta)
        
        if respuesta == None:
            menj = "ok"
        else:
            menj = "No fue posible añadir el usuario"
        
        menj='supfu'+str(menj)
        temp=llenado(len(menj))  
        sock.send(bytes(temp+menj,'utf-8'))
        print("Usuario registrado")
        
    sock.close()
while True:
	sock, addr = server.accept()
	tarea = threading.Thread(target = recibir, args = (sock, addr))
	tarea.start()
