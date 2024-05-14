from client import db_client
#01 product/ XX
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

#02 product/id XX
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
#03 product/ post XX
def insertaProduct(prod):
	conexion = db_client()
	cursor = conexion.cursor()
	query = "INSERT into botiga.product (name,description,company,price,units,subcategory_id,created_at,updated_at) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
	cursor.execute(query,(prod.name,prod.description,prod.company,prod.price,prod.units,prod.subcategory_id,prod.created_at,prod.updated_at))
	
	queryD = "select * from botiga.product where product_id = %s;"
	ultimaId = cursor.lastrowid
	conexion.commit()

	cursor.execute(queryD,(ultimaId,))
	producto_insertado = cursor.fetchone()
	conexion.close()
	cursor.close()
	print(ultimaId)

	if producto_insertado:
		return productoDict(producto_insertado)
	else:
		return "error producto no se ha podido insertar:"
#Modifica por id XX
def modificaWithId(id,preu):
	conexion = db_client()
	cursor = conexion.cursor()
	query = "UPDATE product SET price = %s WHERE product_id = %s;"
	cursor.execute(query,(preu,id))

	query ="select * from product WHERE product_id= %s;"
	cursor.execute(query,(id,))
	resultado = cursor.fetchone()
	return productoDict(resultado)

#Muestra todo seccionado join
def productosSeccionados():
	conexion = db_client()
	cursor = conexion.cursor()
	query = """
		SELECT 
            p.id AS product_id,
            p.name AS product_name,
            s.name AS subcategory_name,
            c.name AS category_name,
            p.brand,
            p.price
        FROM 
            product p
        JOIN 
            subcategory s ON p.subcategory_id = s.id
        JOIN 
            category c ON s.category_id = c.id;
	"""
	cursor.execute(query)
	resultado = cursor.fetchall()
	listProductos =[]
	
	for a in resultado:
		aDict = productoDict(a)
		listProductos.append(aDict)
	conexion.close()
	return listProductos

#Delete XX
def eliminaProducto(id):
	conexion = db_client()
	cursor = conexion.cursor()
	query= "select * from product WHERE product_id= %s;"
	cursor.execute(query,(id,))
	resultado = cursor.fetchone()


	query= "delete from product where product_id=%s;"
	cursor.execute(query,(id,))
	conexion.close()
	return productoDict(resultado)

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
	
#Actividad02
def cargaMasivaTodo():
	pass