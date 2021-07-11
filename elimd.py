#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import threading

from conect import *


#query de la consulta de un paciente mediante rut 
PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("localhost",PORT))
server.send(bytes('00010sinitelimd','utf-8'))

#def recibir(sock, addr):
print("Start eliminar_dog")
while True:

    datos = server.recv(4096)
    if datos.decode('utf-8').find('elimd')!=-1:
        
        #decodificar el mensaje
        datos = datos[10:]
        target = datos.decode()
        data = target.split()
        
    #ELIMINAR EN MASCOTAS
    consulta = f"DELETE FROM mascota WHERE idmascota='{data[0]}';" 
    respuesta = modificar(consulta)

    #ELIMINAR EN USUARIOPERRO
    consulta1 = f"DELETE FROM usuariomascota WHERE idmascota='{data[0]}';"
    respuesta1 = modificar(consulta1)
    
    if respuesta == None:
        menj = "perro eliminado con exito"
    else:
        menj = "no se elimino perrito"
    
    

    menj='elimd'+str(menj)
    #print(menj)
    temp=llenado(len(menj))  
    #print('tmp: ', temp)
    #print('tmp + respuesta:',temp+menj)
    server.send(bytes(temp+menj,'utf-8'))


    #crear mensaje de respuesta
    print("envia3")

    
sock.close()
'''while True:
	sock, addr = server.accept()
	tarea = threading.Thread(target = recibir, args = (sock, addr))
	tarea.start()'''
