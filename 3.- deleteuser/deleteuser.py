#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import threading

from conect import *


PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1',PORT))
server.listen(1000)

def limpiar(var):
        var = str(var)
        var = var.replace("[","")
        var = var.replace("(","")
        var = var.replace("]","")
        var = var.replace(")","")
        var = var.replace(",","")
        return var

def recibir(sock, addr):
    print("Start delete_user")
    while True:

        datos = sock.recv(4096)
        if datos.decode('utf-8').find('deltu'):

            #decodificar el mensaje
            datos = datos[10:]
            target = datos.decode()
            data = target.split()
            print(data)
        # necesito [email, idusuario]
        # seleccionar tipo de usuario del usuario loggeado
        consulta0 = f"SELECT tipodeusuario FROM usuario where email='{data[0]}';"
        tipousuario = consultar(consulta0)
        tipousuario = limpiar(tipousuario)
        #print(tipousuario)
        #print(type(tipousuario))
        if tipousuario != "True" and data[1]=="-":
            menj = "no tiene permiso para borrar usuarios"
            menj='deltu'+str(menj)
            temp=llenado(len(menj))
            sock.send(bytes(temp+menj,'utf-8'))
            print("envia3")

        if tipousuario == "True":
            # seleccionar ID del usuario
            consulta1= f"SELECT idusuario FROM usuario where email='{data[1]}';"
            idusuario1 = consultar(consulta1)
            idusuario1 = limpiar(idusuario1)
            print(idusuario1)
            if idusuario1=="":
                print("No existe un usuario con ese email")
                menj = "no se elimino el usuario porque no existe"
            else:
                # borrar usuario y relaciones
                consulta2 = f"DELETE FROM usuario WHERE email='{data[1]}';"
                respuesta = modificar(consulta2)
                # obtener ids de las mascotas del dueño
                consulta3 = f"SELECT mascota.idmascota FROM mascota, usuariomascota WHERE usuariomascota.idusuario='{idusuario1}' AND usuariomascota.idmascota=mascota.idmascota;"
                idmascota1 = consultar(consulta3)
                idmascota1 = limpiar(idmascota1)
                print("ids mascotas:")
                print(idmascota1)
                listaids = idmascota1.split()
                if len(listaids) > 0:
                    for id in listaids:
                        con = f"DELETE FROM mascota WHERE idmascota='{id}';"
                        modificar(con)
                        con2 = f"DELETE FROM usuariomascota WHERE idmascota={id};"
                        modificar(con2)
                #respuesta2 = modificar(consulta2)
                if respuesta == None:
                    menj = "usuario eliminado con exito"
                else:
                    menj = "no se elimino el usuario"
            menj='deltu'+str(menj)
            temp=llenado(len(menj))
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
