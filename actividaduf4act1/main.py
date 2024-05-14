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



# @app.get("/contenido/categorias")
# def muestraCategorias():
# 	contenido = general_db.showTablaWithName("category")
# 	return contenido

# @app.get("/contenido/subcategorias")
# def muestraSubCategorias():
# 	contenido = general_db.showTablaWithName("subcategory")
# 	return contenido

@app.get("/product/")
def muestraProductos(): #retorna una lista json de toda la lista productos
	contenido = product_db.showTablaWithName("product")
	return contenido

@app.get("/product/{id}")
def muestraUnProducto(id: int): #retorna una lista json de toda la lista productos
	contenido = product_db.contenidoProductoID(id)
	return contenido

@app.post("/product/")
def insertaUnProducto(producto: product):
	contenido = product_db.insertaProduct(producto)
	return contenido