import socket
import threading
from conect import *
 
PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)
print('connecting to {} port {}'.format(*server_address))
server.connect(server_address)
server.send(bytes('00010sinitregi7','utf-8'))
recibido=server.recv(4096)
#def recibir(sock, addr):
print("Creando un nuevo usuario")
while True:
    datos = server.recv(4096)
    print("hola")
    if datos.decode('utf-8').find('regi7')!=-1:
        #decodificar el mensaje
        datos = datos[10:]
        target = datos.decode()
        data = target.split()
        
    consulta = f"INSERT INTO usuario (nombre, apellido, rut, pass, contacto, region, email) VALUES ('{data[0]}','{data[1]}','{data[2]}','{data[3]}','{data[4]}','{data[5]}','{data[6]}');"
    respuesta = modificar(consulta)
    print(respuesta)
    if respuesta == None:
        menj = "ok"
    else:
        menj = "No fue posible añadir el usuario"
    
    menj='regi7'+str(menj)
    temp=llenado(len(menj))  
    server.send(bytes(temp+menj,'utf-8'))
    print("Usuario registrado")
    
server.close()
'''while True:
	sock, addr = server.accept()
	tarea = threading.Thread(target = recibir, args = (sock, addr))
	tarea.start()'''
