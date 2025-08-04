import controllers.ingredientes as ing 
import config
import utils.corefile


def uno() -> list[dict]:
    sc.limpiar_pantalla()
    archivos = ["reportes.json"]
    resultados = []

    for archivo in archivos:
        data = readJson(archivo)
        tipo = archivo.replace(".json", "")

        for stock, elementos in data.items():
            if isinstance(elementos, dict):
                for id_elemento, item in elementos.items():
                    if isinstance(item, dict) and "nombre" in item:
                        if valor.lower() in str(item["nombre"]).lower():
                            resultados.append({
                                "stock": item
                            })