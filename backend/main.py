# MAIN 
from graph import Graph
from dijkstra import dijkstra
from pumabus import construir_grafo_pumabus
if __name__ == "__main__":
    grafo = construir_grafo_pumabus()   # nombre corregido

    print("Sistema de Rutas Pumabús")
    print("\nParadas disponibles:")
    for nodo in grafo.list_adj:
        print(" -", nodo)

    try:
        # Pedimos datos al usuario
        print("\nEscribe el nombre EXACTO de las paradas como aparecen en la lista.\n")
        inicio = input("Ingresa tu punto de partida: ").strip()
        destino = input("Ingresa tu destino: ").strip()

        if inicio.isdigit():
            raise ValueError("Debes escribir el NOMBRE de la parada de inicio, no un número, ¿que pensabas?")
        if destino.isdigit():
            raise ValueError("Debes escribir el NOMBRE de la parada de destino, no un número. ¿Otra vez? ¿Es en serio?")

        # Validar que existan en el grafo
        if inicio not in grafo.list_adj:
            raise ValueError(f"La parada '{inicio}' no está registrada en el sistema. GG")
        if destino not in grafo.list_adj:
            raise ValueError(f"La parada '{destino}' no está registrada en el sistema. GG")

        # Cálculo de rUta
        distancia, ruta = dijkstra(grafo, inicio, destino)

        if ruta:
            print(f"\nRuta más corta de {inicio} a {destino}:")
            print(" → ".join(ruta))
            print("Distancia total:", distancia)
        else:
            print(f"\nNo existe ruta entre {inicio} y {destino}.")

    except ValueError as e:
        print("\n[ERROR DE ENTRADA] Echale ganitas")
        print(e)

    except KeyError as e:
        print("\n[ERROR INTERNO]")
        print("Hay una parada mal escrita ", e)

    except Exception as e:
        print("\n[ERROR INESPERADO]")
        print("Ocurrió un problema no contemplado jiji : ", e)
