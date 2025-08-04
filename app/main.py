"""
Autor: Juan Pablo Quijano y valentina mancilla
Fecha: 28/07/2025
Descripción: Administrador de Colección de Libros/Películas/Música
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.screencontrollers as sc
import controllers.añadir as add
import controllers.buscar as ls
import controllers.reportes as rp


def main_menu():
    while True:
        sc.limpiar_pantalla()
        print('========================================')
        print('Reportes')
        print('========================================')
        print('1. Encontrar todos los ingredientes con stock menor a 400.')
        print('2. Encontrar todas las hamburguesas de la categoría “Vegetariana.')
        print('3. Encontrar todos los chefs que se especializan en “Carnes.')
        print('4. Aumentar en 1.5 el precio de todos los ingredientes.')
        print('5. Encontrar todas las hamburguesas preparadas por “ChefB.')
        print('6. Encontrar el nombre y la descripción de todas las categorías.')
        print('7. Eliminar todos los ingredientes que tengan un stock de 0.')
        print('8. Agregar un nuevo ingrediente a la hamburguesa “Clásica”.')
        print('9. Encontrar todas las hamburguesas que contienen “Pan integral” como ingrediente.')
        print('10.Cambiar la especialidad del “ChefC” a “Cocina Internacional.')
        print('11.Encontrar todas las hamburguesas preparadas por “ChefB.')
        print('12. Encontrar el ingrediente más caro.')
        print('13. Encontrar las hamburguesas que no contienen “Queso cheddar” como ingrediente.')
        print('14. Incrementar el stock de “Pan” en 100 unidades.')
        print('15. Eliminar las hamburguesas que contienen menos de 5 ingredientes')
        print('16. Listar las hamburguesas en orden ascendente según su precio.')
        print('17. Encontrar todos los ingredientes cuyo precio sea entre $2 y $5.')
        print('18. Actualizar la descripción del “Pan” a “Pan fresco y crujiente”.')
        print('19. Encontrar la hamburguesa más cara que fue preparada por un chef especializado en “Gourmet”.')
        print('20. Listar todos los ingredientes junto con el número de hamburguesas que los contienen..')
        print('21. Salir')
        print('========================================')

        try:
            op = int(input("\nElige una opción (1-21): "))
            if 1 <= op <= 21:
                return op
        except ValueError:
            pass  

        print("\nOpción no válida. Intenta nuevamente.")
        sc.pausar()


if __name__ == "__main__":
    while True:
        opcion = ()

        if opcion == 1:
            rp.uno()
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            pass
        elif opcion == 8:
            pass
        elif opcion == 9:
            pass
        elif opcion == 10:
            pass
        elif opcion == 11:
            pass
        elif opcion == 12:
            pass
        elif opcion == 13:
            pass
        elif opcion == 14:
            pass
        elif opcion == 15:
            pass
        elif opcion == 16:
            pass
        elif opcion == 17:
            pass
        elif opcion == 18:
            pass
        elif opcion == 19:
            pass
        elif opcion == 20:
            pass
        elif opcion == 21:
            break