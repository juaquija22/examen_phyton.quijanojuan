from utils.screencontrollers import limpiar_pantalla
from utils.screencontrollers import pausar
import utils.corefile as cf
import utils.screencontrollers as sc
import utils.validedata as vd
from config import DB_PATH
import random
import os

            



def add_ingredientes():
    sc.limpiar_pantalla()
    idig = random.randint(1023, 9876)
    
    nameingrediente = vd.validatetext('Nombre Del ingrediente :')
    description = vd.validatetext('descripcion del ingrediente :')
    price = vd.validateflot('precio del ingrediente :')
    stock = vd.validateflot('stock del ingrediente :')
    ingrediente_data = {
        idig: {
            "nombre": nameingrediente,
            "descripcion": description,
            "precio": price,
            "stock": stock,
        }
    }

    if cf.updateJson(ingrediente_data, ["ingredientes"], filename="ingrediente.json"):
        print("ingrediente agregado exitosamente.")
    else:
        print("No se pudo agregar el ingrediente.")
    sc.pausar()
            



def add_categoria():
    sc.limpiar_pantalla()
    idct = random.randint(1023, 9876)
    
    categorianame = vd.validatetext('Nombre De la Categoria :')
    descriptioncg = vd.validatetext('Descripcion :')
    
    
    categoria_data = {
        idct: {
            "nombre": categorianame,
            "descripcion": descriptioncg
        }
    }
    

    if cf.updateJson(categoria_data, ["categorias"], filename="categoria.json"):
        print("categoria agregado exitosamente.")
    else:
        print("No se pudo agregar la categoria.")
    
    sc.pausar()


def add_chefs():
    sc.limpiar_pantalla()
    idch = random.randint(1023, 9876)
    
    nombrechef = vd.validatetext('Nombre Del chef :')
    especialidad = vd.validatetext('especialidad del chef :')
    
    
    chef_data = {
        idch: {
            "nombre": nombrechef,
            "descripcion": especialidad
        }
    }
    

    if cf.updateJson(chef_data, ["chefs"], filename="chef.json"):
        print("chef agregado exitosamente.")
    else:
        print("No se pudo agregar el chef.")
    
    sc.pausar()




def add_hamburguesas():
    sc.limpiar_pantalla()
    idhm = random.randint(1023, 9876)
    
    nameburguer = vd.validatetext('Nombre De la hamburguesa :')
    categoria = vd.validatetext('categoria :')
    ingredientes = vd.validatetext('ingredientes :')
    precio = vd.validateflot('precio :')
    chef = vd.validatetext('chef:')
    hamburguesas_data = {
        idhm: {
            "nombre": nameburguer,
            "categoria": categoria,
            "ingredientes": ingredientes,
            "precio": precio,
            "chef": chef
        }
    }

    if cf.updateJson(hamburguesas_data, ["hamburguesas"], filename="hamburguesa.json"):
        print("hamburguesa agregada exitosamente.")
    else:
        print("No se pudo agregar la hamburguesa.")
    sc.pausar()

