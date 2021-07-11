#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import threading

from conect import *


PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("localhost",PORT))
server.send(bytes('00010sinitviewd','utf-8'))
recibido=server.recv(4096)
#def recibir(sock, addr):
print("Start view_dogs")
while True:

    datos = server.recv(4096)
    if datos.decode('utf-8').find('viewd')!=-1:

        #decodificar el mensaje
        datos = datos[10:]
        target = datos.decode()
        data = target.split()
    # verifica si hay mascotas
    consulta = f"SELECT nombre, edad, raza, descripcion, idmascota FROM mascota;"

    respuesta = consultar(consulta)

    if respuesta == None:
        menj = "consulta fallida"
    else:
        menj = "consulta exitosa"



    menj='viewd'+str(menj)
    #print(respuesta)
    temp=llenado(len(menj))
    print('temp: ',temp)
    #print('temp + respuesta: ',temp+respuesta)
    server.send(bytes(temp+menj,'utf-8'))

    #crear mensaje de respuesta
    print("envia3")
sock.close()
'''while True:
	sock, addr = server.accept()
	tarea = threading.Thread(target = recibir, args = (sock, addr))
	tarea.start()'''
