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