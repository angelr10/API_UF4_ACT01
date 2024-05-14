from client import db_client

def showTablaWithName(tablaLectura):
	conexion = db_client()
	cursor = conexion.cursor()
	cursor.execute("select * from "+tablaLectura+";")
	resultado = cursor.fetchall()
	listProductos =[]
	for a in resultado:
		#Transformacion a diccionario
		listProductos.append()#Restante

	conexion = db_client()
	conexion.close()
	return resultado