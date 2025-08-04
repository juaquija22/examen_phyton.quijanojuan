from utils.screencontrollers import limpiar_pantalla
from utils.screencontrollers import pausar
import utils.corefile as cf
import utils.screencontrollers as sc
import utils.validedata as vd
from config import DB_PATH
import random
import os

            



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



