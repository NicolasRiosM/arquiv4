#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import threading

from conect import *


PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1',PORT))
#server.send(bytes('00010siniteditu','utf8'))
#recibido=s.recv(4096)
#print(recibido)
server.listen(1000)

def recibir(sock, addr):
    print("Start edit_user")
    while True:

        datos = sock.recv(4096)
        if datos.decode('utf-8').find('editu'):

            #decodificar el mensaje
            datos = datos[10:]
            target = datos.decode()
            data = target.split()
            print(data)


        consulta = f"UPDATE usuario SET nombre='{data[0]}', apellido='{data[1]}', rut='{data[2]}', pass='{data[3]}', contacto='{data[4]}', region='{data[5]}' WHERE email='{data[6]}';"


        #consulta = f"INSERT INTO perros (nombre, edad, raza, descripcion) VALUES ('{data[0]}','{data[1]}', '{data[2]}','{data[3]}');"


        respuesta = modificar(consulta)

        if respuesta == None:
            menj = "usuario actualizado con exito"
        else:
            menj = "no se actualizo el usuario"



        menj='editu'+str(menj)
        #print(menj)
        temp=llenado(len(menj))
        #print('tmp: ', temp)
        #print('tmp + respuesta:',temp+menj)
        sock.send(bytes(temp+menj,'utf-8'))


        #crear mensaje de respuesta
        print("envia3")
        a = consultar("SELECT * FROM usuario;")
        print(a)

    sock.close()
while True:
	sock, addr = server.accept()
	tarea = threading.Thread(target = recibir, args = (sock, addr))
	tarea.start()
