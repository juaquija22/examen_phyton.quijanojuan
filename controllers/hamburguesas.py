from utils.screencontrollers import limpiar_pantalla
from utils.screencontrollers import pausar
import utils.corefile as cf
import utils.screencontrollers as sc
import utils.validedata as vd
from config import DB_PATH
import random
import os


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



    