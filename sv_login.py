import socket
from conect import *
import bcrypt
import threading
import sqlite3
import hashlib

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 5000))
s.send(bytes('00010sinitlogi7','utf-8'))

#def recibir(sock, addr):
print("Ingresando a la cuenta de usuario")
recibido=s.recv(4096)

def limpiar(var):
    var = str(var)
    var = var.replace("[","")
    var = var.replace("(","")
    var = var.replace("]","")
    var = var.replace(")","")
    var = var.replace(",","")
    return var


while True:
    print("aqui")
    datos=s.recv(4096)
    print(datos)
    
    if datos.decode('utf-8').find('logi7')!=-1:
        datos = datos[10:]
        target = datos.decode()
        data = target.split()
        email = data[0]
        password = data[1]
        val = 0
        print(email)
        consulta = f"select pass from usuario where email='{email}'"
        respuesta = consultar(consulta)
        print("-----------")
        print(respuesta[2])
        enchash = hashlib.md5(password.encode())#aqui
        pass2=enchash.hexdigest()
        print("aca abajo contras")
        for i in respuesta:
            mail = i[0]
            passw = i[1] 
            print(passw)
            print(password)
            if mail == email and passw==password:
                val=1
                print("Ha ingresado con éxito a su cuenta")
                respuesta2='logi7'+mail+passw
                
                break
            else:
                respuesta2 = 'logi7' + "no_existe_usuario"
                break
        else:
            pass
    print(respuesta2)
    temp=llenado(len(respuesta2))  
    s.sendall(bytes(temp+respuesta2,'utf-8'))

    if (val!=1):
        print("Contraseña incorrecta")
