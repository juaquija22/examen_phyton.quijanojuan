def buscar_por_titulo() -> List[Dict]:
    sc.limpiar_pantalla()
    valor = input("Ingresa el título: ")
    archivos = ["libros.json", "musica.json", "peliculas.json"]
    resultados = []

    for archivo in archivos:
        data = readJson(archivo)
        tipo = archivo.replace(".json", "")

        for categoria, elementos in data.items():
            if isinstance(elementos, dict):
                for id_elemento, item in elementos.items():
                    if isinstance(item, dict) and "nombre" in item:
                        if valor.lower() in str(item["nombre"]).lower():
                            resultados.append({
                                "tipo": tipo,
                                "categoria": categoria,
                                "id": id_elemento,
                                "elemento": item
                            })

    if resultados:
        mostrar_resultados(resultados)
    else:
        print("No se encontraron resultados.")
        sc.pausar()

    return resultados
