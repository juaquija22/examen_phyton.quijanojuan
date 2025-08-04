from utils.screencontrollers import limpiar_pantalla
from utils.screencontrollers import pausar
import utils.corefile as cf
import utils.screencontrollers as sc
import utils.validedata as vd
from config import DB_PATH
import random
import os



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

