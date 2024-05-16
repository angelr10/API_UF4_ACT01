from client import db_client
import csv
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
            product.product_id AS product_id,
            product.name AS product_name,
            subcategory.name AS subcategory_name,
            category.name AS category_name,
            product.company AS company,
            product.price AS price
        FROM 
            product
        JOIN 
            subcategory ON product.subcategory_id = subcategory.subcategory_id
        JOIN 
            category ON subcategory.category_id = category.category_id;
	"""
	cursor.execute(query)
	resultado = cursor.fetchall()
	listProductos =[]

	for a in resultado:
		aDict = productoDictDos(a)
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


def productoDictDos(a):
	return {"product_id":a[0],
		"product_name":a[1],
		"subcategory_name":a[2],
		"category_name":a[3],
		"company":a[4],
		"price":a[5]
	}
	
#Actividad02
def cargaMasivaTodo():
	file = "llista_productes.csv"
	categoriaId = []
	categoriaName = []
	subcategoriaId = []
	subcategoriaName = []
	productoId = []
	productoName = []
	productoDescripcion = []
	productoCompa = []
	productoPrecio = []
	productounidades = []

	
	#Basureros
	categoriaIdB = []
	subcategoriaIdB = []
	productoIdB = []
	# Abrir el archivo CSV
	with open(file, mode='r', encoding='utf-8') as file:
		# Crear un lector CSV
		reader = csv.reader(file)
		
		# Leer cada fila en el archivo CSV
		vuelta = 0

		

		for row in reader:#Lector de tabla y almacenamiento individual
			categoriaId.append(row[0])
			
			subcategoriaId.append(row[2])
			
			productoId.append(row[4])
			
			
			if vuelta != 0:#Si encuentro contenido y NO LOS TITULOS
				#ParaCATEGORIAS
				if categoriaId[-1] in categoriaIdB:
					pass
				else:
					categoriaIdB.append(categoriaId[-1])
					categoriaName.append(row[1])

				#ParaSUBCATEGORIAS
				if subcategoriaId[-1] in subcategoriaIdB:
					pass
				else:
					subcategoriaIdB.append(subcategoriaId[-1])
					subcategoriaName.append(row[3])
				#ParaPRODUCTO
				if productoId[-1] in productoIdB:
					pass
				else:
					productoIdB.append(productoId[-1])
					productoName.append(row[5])
					productoDescripcion.append(row[6])
					productoCompa.append(row[7])
					productoPrecio.append(row[8])
					productounidades.append(row[9])

			vuelta+=1
		print("SUBCATEGORIA-------------")
		for a in subcategoriaName:
			print(a)
		print("CATEGORIAS---------------")
		for b in categoriaName:
			print(b)
		print("PRODUCTOS------------------")
		for c in productoName:
			print(c)
		return productoName

