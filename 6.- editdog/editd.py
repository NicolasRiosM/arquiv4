#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import threading

from conect import *


#query de la consulta de un paciente mediante rut 
PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1',PORT))
server.listen(1000)
 
def recibir(sock, addr):
    print("Start Edit_dog")
    while True:

        datos = sock.recv(4096)
        if datos.decode('utf-8').find('editd'):
            
            #decodificar el mensaje
            datos = datos[10:]
            target = datos.decode()
            data = target.split()
        
        consulta = f"UPDATE mascota SET nombre='{data[0]}', edad='{data[1]}', raza='{data[2]}', descripcion='{data[3]}' WHERE idmascota='{data[4]}';"
	        
        respuesta = modificar(consulta)
        
        if respuesta == None:
            menj = "perro actualizado con exito"
        else:
            menj = "no se actualizo perrito"
        
        
    
        menj='supfu'+str(menj)
        #print(menj)
        temp=llenado(len(menj))  
        #print('tmp: ', temp)
        #print('tmp + respuesta:',temp+menj)
        sock.send(bytes(temp+menj,'utf-8'))
        
        print("envia3")
        
    sock.close()
while True:
	sock, addr = server.accept()
	tarea = threading.Thread(target = recibir, args = (sock, addr))
	tarea.start()
