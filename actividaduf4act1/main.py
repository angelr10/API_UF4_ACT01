from fastapi import FastAPI
from pydantic import BaseModel

from typing import List
import product_db

app = FastAPI()

class product(BaseModel):
	name:str
	description: str
	company: str
	price: float
	units: int
	subcategory_id:int
	created_at: str
	updated_at: str

@app.get("/")
def read_root():
	return{"Esta pagina funciona"}

@app.get("/product/")
def muestraProductos():
	contenido = product_db.showTablaWithName("product")
	return contenido

@app.get("/product/{id}")
def muestraUnProducto(id: int): 
	contenido = product_db.contenidoProductoID(id)
	return contenido

@app.post("/product/")
def insertaUnProducto(producto: product):
	contenido = product_db.insertaProduct(producto)
	return contenido

@app.put("/product/producte/{id}/{precio}")
def editaProductoConId(id: int,precio: int):
	contenido = product_db.modificaWithId(id,precio)
	return contenido

@app.delete("/product/{id}")
def deleteProducto(id: int):
	contenido = product_db.eliminaProducto(id)
	return contenido

@app.get("/productAll")
def muestraTodoFormateado():
	contenido = product_db.productosSeccionados()
	return contenido


#ACT 02
@app.post("/loadProducts")
def cargaMasiva():
	contenido = product_db.cargaMasivaTodo()
	return contenido