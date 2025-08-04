from utils.corefile import readJson

def reporte_1():
    ingredientes = readJson("ingredientes.json")

    print("Ingredientes con stock menor a 400:\n")

    encontrados = False
    for id_ing, info in ingredientes.items():
        stock = info.get("stock", 0)
        if stock < 400:
            print(f"- {info.get('nombre', 'Desconocido')} (ID: {id_ing}) - Stock: {stock}")
            encontrados = True

    if not encontrados:
        print("No hay ingredientes con stock menor a 400.")