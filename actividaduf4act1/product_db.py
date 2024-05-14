from client import db_client
#01 product/
def showTablaWithName(tablaLectura):
	conexion = db_client()
	cursor = conexion.cursor()
	cursor.execute("select * from "+tablaLectura+";")
	resultado = cursor.fetchall()
	listProductos =[]
	for a in resultado:
		aDict = productoDict(a)
		listProductos.append(aDict)

	conexion.close()
	return listProductos
#02 product/id
def contenidoProductoID(id):
	conexion = db_client()
	cursor = conexion.cursor()
	query = "select * from product WHERE product_id= %s;"
	cursor.execute(query,(id,))
	resultado = cursor.fetchall()
	listProductos =[]
	for a in resultado:
		aDict = productoDict(a)
		listProductos.append(aDict)

	conexion.close()
	return listProductos
#03 product/ post
def insertaProduct(prod):
	conexion = db_client()
	cursor = conexion.cursor()
	query = "insert into botiga.product (name,description,company,price,units,subcategory_id,created_at,updated_at) VALUES (%s,%s,%s,%s,%s,%s,NOW(),NOW())"
	cursor.execute(query,(prod.name,prod.description,prod.company,prod.price,prod.units,prod.subcategory_id))
	conexion.commit()
	
	ultimaId = cursor.lastrowid
	cursor.execute("select * from botiga.product where product_id = %s;",(ultimaId,))
	producto_insertado = cursor.fetchone()
	conexion.close()
	conexion.close()

	if producto_insertado:
		return productoDict(producto_insertado)
	else:
		return "error producto no se ha podido insertar"

def productoDict(a):
	return {"product_id":a[0],
		 "name":a[1],
		 "description":a[2],
		 "company":a[3],
		 "price":a[4],
		 "units":a[5],
		 "subcategory_id":a[6],
		 "created_at":a[7],
         "updated_at":a[8]
    }
	
