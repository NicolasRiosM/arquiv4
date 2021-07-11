import socket
from conect import *
import bcrypt
import threading
import sqlite3
import hashlib

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 5000))
s.send(bytes('00010sinitlogin','utf-8'))

#def recibir(sock, addr):
print("Ingresando a la cuenta de usuario")
while s.recv(4096):
    datos = s.recv(4096)
    if datos.decode('utf-8').find('login'):
        datos = datos[10:]
        target = datos.decode()
        data = target.split()
        email = data[0]
        password = data[1]
    val = 0
    consulta = "select email, pass from usuario"
    respuesta = consultar(consulta)
    enchash = hashlib.md5(password.encode())
    pass2=enchash.hexdigest()
    print("hola")
    for i in respuesta:
        mail = i[0]
        passw = i[1] 
        print(passw)
        print(pass2)
        if mail == email and passw==pass2:
            val=1
            print("Ha ingresado con éxito a su cuenta")
            respuesta2='login'+mail+passw
            
            break
        else:
            respuesta2 = 'login' + "no_existe_usuario"
            break
print(respuesta2)
temp=llenado(len(respuesta2))  
s.sendall(bytes(temp+respuesta2,'utf-8'))

if (val!=1):
    print("Contraseña incorrecta")
