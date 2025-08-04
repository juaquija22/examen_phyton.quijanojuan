

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import controllers.reportes as rp

def main_menu():
    while True:
       
        print("=================================")
        print('             Reportes            ')
        print("=================================")
        print("1. Encontrar ingredientes con stock menor a 400.")
        print("2. Hamburguesas de la categoría 'vegetariana'.")
        print("3. Chefs especializados en 'Carnes'.")
        print("4. Aumentar 1.5 el precio de ingredientes.")
        print("5. Hamburguesas preparadas por 'chefB'.")
        print("6. Nombre y descripción de categorías.")
        print("7. Eliminar ingredientes con stock 0.")
        print("8. Agregar ingrediente a hamburguesa 'clásica'.")
        print("9. Hamburguesas con 'Pan integral'.")
        print("10. Ingredientes que no se usan en hamburguesas.")
        print("11. Chefs que no preparan ninguna hamburguesa.")
        print("12. Cantidad de hamburguesas por categoría.")
        print("13. Ingredientes usados por cada chef.")
        print("14. Cantidad de ingredientes por hamburguesa.")
        print("15. Stock total de ingredientes por categoría.")
        print("16. Precio promedio de hamburguesas.")
        print("17. Chefs que usan ingredientes sin gluten.")
        print("18. Categoría con más hamburguesas.")
        print("19. Ingrediente más usado.")
        print("20. Reporte general del sistema.")
        print("0. Salir")
        print("=================================")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                rp.reporte_1()
            case "2":
                rp.reporte_2()
            case "3":
                rp.reporte_3()
            case "4":
                rp.reporte_4()
            case "5":
                rp.reporte_5()
            case "6":
                rp.reporte_6()
            case "7":
                rp.reporte_7()
            case "8":
                rp.reporte_8()
            case "9":
                rp.reporte_9()
            case "10":
                rp.reporte_10()
            case "11":
                rp.reporte_11()
            case "12":
                rp.reporte_12()
            case "13":
                rp.reporte_13()
            case "14":
                rp.reporte_14()
            case "15":
                rp.reporte_15()
            case "16":
                rp.reporte_16()
            case "17":
                rp.reporte_17()
            case "18":
                rp.reporte_18()
            case "19":
                rp.reporte_19()
            case "20":
                rp.reporte_20()
            case "0":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida.")

        input("Presione Enter para continuar...")

if __name__ == "__main__":
    main_menu()
