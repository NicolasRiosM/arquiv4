import psycopg2
import sqlite3
conec = None
cur = None

def conexion():
    try:
        global conec
        global cur
        conec = sqlite3.connect('arqui.db')
        print("Conexión con base de datos establecida")
        cur = conec.cursor()
    except:
        print("Error de conexión con base de datos")
    
def consultar(sqlquery):
    cur.execute(sqlquery)
    return cur.fetchall()

def modificar(sqlquery):
    cur.execute(sqlquery) 
    conec.commit()  

def cerrar():
    try:
        cur.close()
        conec.close()
        print("Conexión con base de datos cerrada")
    except:
        print("Error al cerrar conexión")    

def llenado(largo):
    aux = str(largo)
    while len(aux) < 5:
        aux = '0' + aux
    print(aux)
    return aux

conexion()
