import socket 
import bcrypt
import time
import datetime

from conect import *
import threading
global email
socket = socket.socket()
PORT = 5000
socket.connect(("127.0.0.1",PORT))
socket.send(bytes('00005getsv','utf-8'))
def limpiar(var):
    var = str(var)
    var = var.replace("[","")
    var = var.replace("(","")
    var = var.replace("]","")
    var = var.replace(")","")
    var = var.replace(",","")
    return var

        
       
        
       
#-------------------------interfaz--------------------------------------#

while True:


    opcion = input("""Que servicio desea: 
	1.- Login
	2.- Register

        0.- salir



        En caso de algun inconveniente contactarse al mail admin@mail.udp.cl\n""")
    if opcion == "0":
        socket.send(bytes('quit','utf-8'))
        time.sleep(5)
        break
    
    if(opcion == '1'):
        print("Ha seleccionado la opcion de inicio de sesión\n")
        #mandar a codigo maca
        socket.send(bytes('00010getsvlogin','utf-8'))
        #ingreso de dato

        email = input("Ingrese su email \n")
        password = input("Ingrese su contraseña\n")


        #enviar mensaje
        datos = email + " " + password 
        aux = llenado(len(datos+'login'))
        mensaje = aux + 'login' + datos
        
        socket.send(bytes(mensaje,'utf-8'))
        

        
    if(opcion == '2'):
        socket.send(bytes('00010getsvagusr','utf-8'))
        print("Para crear su cuenta de usuario, ingrese sus datos a continuación.")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        rut = input("RUT: ")
        psw = input("Contraseña: ")
        contacto = input("Numero de contacto: ")
        region = input("Región de residencia: ")
        email = input("E-mail: ")
        #--------------HASH----------------
        salt = bcrypt.gensalt()
        psw2 = psw.encode()
        pswAux = bcrypt.hashpw(psw2, salt)
        pswAux2 = pswAux.decode()
        #----------------------------------
        #envio de datos
        datos = nombre + " " + apellido + " " + rut + " " + pswAux2 + " " + contacto + " " + region + " " + email
        temp = llenado(len(datos+'agusr'))
        mensaje = temp + 'agusr' + datos
        socket.send(bytes(mensaje,'utf-8'))
        
        recibido = socket.recv(4096)
        print(recibido[10:])
        
        
while True:
    opcion = input("""Que servicio desea: 
	    1.- Agregar mascota
	    2.- Editar mascota
            3.- Eliminar mascota
            4.- Ver mascotas
            5.- Editar usuario 
            6.- Eliminar usuario
            0.- salir



            En caso de algun inconveniente contactarse al mail admin@mail.udp.cl\n""")

    if opcion=="1":
        socket.send(bytes('00010getsvcread','utf-8'))
        email1 = email
        email2 = email1 + " "
        temp2= llenado(len(email2+'cread'))
        mesj= temp2+ 'cread' + email2
        socket.send(bytes(mesj, 'utf-8'))

                # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1
                #socket.send(bytes('00010getsvadddi','utf-8'))

                #ID USUARIO:
        consulta0= f"SELECT idusuario FROM usuario WHERE email='{email1}';"
        idusuario1 = consultar(consulta0)
        idusuario1 = limpiar(idusuario1)
                

                #RELACION USUARIO PERRO
        consulta1= f"SELECT idmascota FROM usuariomascota where idusuario = '{idusuario1}';"
        idmascota1 = consultar(consulta1)
                
                
                #PERROS DISPONIBLES
        print("Sus perros ingresados: ")
        for gg in idmascota1:
            gg = limpiar(gg)
                        
            a = consultar(f"SELECT nombre, edad, raza, descripcion, idmascota FROM mascota where idmascota = '{gg}';")
            print(a)

                #ingreso de datos
        print("ingrese los siguientes datos del perrito")
        nombre = input("Escribir nombre: ")
        edad = input("Escribir edad en meses: ")
        raza = input("Escribir raza o callejero: ")
        descripcion = input("Escribir descripción corta: ")

                #envio de datos
        datos = nombre + " " + edad + " " + raza + " " + descripcion
        temp = llenado(len(datos+'cread'))
        mensaje = temp + 'cread' + datos
        socket.send(bytes(mensaje,'utf-8'))
                #print(mensaje)

        
        recibido = socket.recv(4096)
        print(recibido[10:])
        print("fin cliente")
        
    
    if opcion=="2":
        socket.send(bytes('00010getsveditd','utf-8'))
        email1 = email

                # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1
                #socket.send(bytes('00010getsvadddi','utf-8'))

                #ID USUARIO:
        consulta0= f"SELECT idusuario FROM usuario WHERE email='{email1}';"
        idusuario1 = consultar(consulta0)
        idusuario1 = limpiar(idusuario1)

                #RELACION USUARIO PERRO
        consulta1= f"SELECT idmascota FROM usuariomascota where idusuario = '{idusuario1}';"
        idmascota1 = consultar(consulta1)

                #PERROS DISPONIBLES
        print("Sus perros ingresados: ")
        for gg in idmascota1:
            
            gg = limpiar(gg)
                        
            a = consultar(f"SELECT nombre, edad, raza, descripcion, idmascota FROM mascota where idmascota = '{gg}';")
            print(a)

                #ingreso de ide
        print("AVISO: En el arreglo del perro el ULTIMO NUMERO es el ID del animal")
        ide = input("Ingrese id de animal a editar: ")

                #ingreso nuevo de datos
        nombre = input("Escribir nombre: ")
        edad = input("Escribir edad: ")
        raza = input("Escribir raza: ")
        descripcion = input("Escribir descripcion: ")

                #envio de datos nuevos
        datos = nombre + " " + edad + " " + raza + " " + descripcion + " " + ide
        temp = llenado(len(datos+'editd'))
        mensaje = temp + 'editd' + datos
        socket.send(bytes(mensaje,'utf-8'))
        
        recibido = socket.recv(4096)
        print(recibido[10:])
        print("fin cliente")
           


        
    if opcion=="3":
        socket.send(bytes('00010getsvelimd','utf-8'))
        email1 = email

                # se debe estar con sesión iniciada de entes , luego mover esto al if de op 1
                #socket.send(bytes('00010getsvadddi','utf-8'))

                #ID USUARIO:
        consulta0= f"SELECT idusuario FROM usuario WHERE email='{email1}';"
        idusuario1 = consultar(consulta0)
        idusuario1 = limpiar(idusuario1)

                #RELACION USUARIO PERRO
        consulta1= f"SELECT idmascota FROM usuariomascota where idusuario = '{idusuario1}';"
        idmascota1 = consultar(consulta1)

                #PERROS DISPONIBLES
        print("Sus perros ingresados: ")
        for gg in idmascota1:
                gg = limpiar(gg)
                        
                a = consultar(f"SELECT nombre, edad, raza, descripcion, idmascota FROM mascota where idmascota = '{gg}';")
                print(a)

                #ingreso de ide
        print("AVISO: En el arreglo del perro el ULTIMO NUMERO es el ID del animal")
        ide = input("Ingrese id de animal a eliminar: ")

                #envio de datos viejos
        datos = ide + " " + "jaja"
        temp = llenado(len(datos+'elimd'))
        mensaje = temp + 'elimd' + datos
        socket.send(bytes(mensaje,'utf-8'))
        
        recibido = socket.recv(4096)
        print(recibido[10:])

            
        
    if opcion== "4":
        socket.send(bytes('00010getsvviewd','utf-8'))
        consulta = f"SELECT mascota.nombre, mascota.edad, mascota.raza, mascota.descripcion, usuario.nombre, usuario.apellido, usuario.contacto, usuario.email, usuario.region FROM mascota, usuario, usuariomascota WHERE mascota.idmascota = usuariomascota.idmascota AND usuario.idusuario = usuariomascota.idusuario;"
        respuesta = consultar(consulta)
                #print(respuesta)
        for i in respuesta:
            nombreM = i[0]
            edad = i[1]
            raza = i[2]
            desc = i[3]
            nombreU = i[4]
            apellido = i[5]
            contacto = i[6]
            email = i[7]
            region = i[8]
            print("Nombre mascota: ",nombreM,"\nEdad (meses): ",edad,"\nRaza: ",raza,"\nDescripcion: ",desc,"\nNombre dueñx: ",nombreU," ",apellido,"\nContacto: ",contacto,"\nEmail: ",email,"\nRegion: ",region)
            print("-----------------------------")
        temp = llenado(len('viewd'))
        mensaje = temp + 'viewd'
        socket.send(bytes(mensaje,'utf-8'))
        recibido = socket.recv(4096)
        print(recibido[10:])
      


            
    if opcion== "5":
        socket.send(bytes('00010getsveditu','utf-8'))
        email1 = email # aqui pasas el atributo de mail
        print("Sus datos de usuario: ")
        consulta = f"SELECT nombre, apellido, rut, email, pass, contacto, region, tipodeusuario, idusuario FROM usuario WHERE email='{email1}';"
        datosU = consultar(consulta)
        n = datosU[0][0]
        a = datosU[0][1]
        r = datosU[0][2]
        e = datosU[0][3]
        p = datosU[0][4]
        c = datosU[0][5]
        re = datosU[0][6]
        t = datosU[0][7]
        id = datosU[0][8]
        if t == True:
            t = "Administrador"
        if t == False:
            t = "Usuario normal"
        print("Nombre completo: ",n,a,"\nRut: ",r,"\nEmail: ",e,"\nContraseña: ",p,"\nContacto: ",c,"\nRegion: ",re,"\nTipo de cuenta: ",t,"\nID usuario: ",id)
        print("-----------------------------")
        print("Editar datos: ")
        nombre = input("Escribir nombre: ")
        apellido = input("Escribir apellido: ")
        rut = input("Escribir rut: ")
        contraseña = input("Escribir contraseña: ")
        contacto = input("Escribir numero telefonico:")
        region = input("Escribir region:")

        salt = bcrypt.gensalt()
        psw2 = contraseña.encode()
        pswAux = bcrypt.hashpw(psw2, salt)
        pswAux2 = pswAux.decode()



                #envio de datos
        datos = nombre + " " + apellido + " " + rut +  " " + pswAux2 + " " + contacto + " " + region + " " + email
        temp = llenado(len(datos+'editu'))
        mensaje = temp + 'editu' + datos
        socket.send(bytes(mensaje,'utf-8'))
                #print(mensaje)

        recibido = socket.recv(4096)
        recibido = socket.recv(4096)
        print(recibido[10:])
    if opcion=="6":
        socket.send(bytes('00010getsvdeltu','utf-8'))
        email = email
                # seleccionar tipo de usuario del usuario loggeado
        consulta0 = f"SELECT tipodeusuario FROM usuario where email='{email}';"
        tipousuario = consultar(consulta0)
        tipousuario = limpiar(tipousuario)
        if tipousuario != "True":
            print("No tiene permiso para realizar esta accion")
            email_borrar = "-"
        if tipousuario == "True":
            email_borrar = input("Escribir email para borrar su usuario: ")
                #envio de datos
        datos = email + " " + email_borrar
        temp = llenado(len(datos+'deltu'))
        mensaje = temp + 'deltu' + datos
        socket.send(bytes(mensaje,'utf-8'))


        recibido = socket.recv(4096)
        print(recibido[10:])


        
    if(opcion == "0"):
        socket.send(bytes('quit','utf-8'))
        time.sleep(5)
        break

print("ha cerrado terminal")
