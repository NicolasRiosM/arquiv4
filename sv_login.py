import socket  
from conect import *
import bcrypt
import threading
import sqlite3


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
server_address = ('localhost', 5000)
print('connecting to {} port {}'.format(*server_address))
s.connect(server_address)
s.sendall(bytes('00010sinitlogin','utf-8'))


#def recibir(sock, addr):
print("Ingresando a la cuenta de usuario")

while s.recv(4096):
    datos = s.recv(4096)
    if datos.decode('utf-8').find('login'):
        datos = datos[10:]
        target = datos.decode()
        data = target.split()          
    consulta = f"select email, pass from usuario"
    respuesta = consultar(consulta)
    print(data)
    i=0
    print(respuesta)
    while (i<len(respuesta)):
        comp = respuesta [i][0]
        i=i+1
        mail =[]
        psw = []
        j=0
        k=0
        while (j<len(comp) and comp[j] != ","):
            mail.append(comp[j])
            k = j
            j=j+1
        mail.pop(0)
        email=''.join(mail)
        while (k<len(comp)):
            print(comp[k])
            psw.append(comp[k])
            k=k+1
        print(psw)
        psw.pop(0)
        psw.pop(0)
        psw.pop()
        password=''.join(psw)

        enchash = password.encode()
        encpass = data[1].encode()
        val=0
        if data[0] == email and bcrypt.checkpw(encpass, enchash):
            val=1
            print("Ha ingresado con éxito a su cuenta")
            break

if (val!=1):
    print("Contraseña incorrecta")
    
s.close()
'''while True:
	sock, addr = s.accept()
	tarea = threading.Thread(target = recibir, args = (sock, addr))
	tarea.start()'''
