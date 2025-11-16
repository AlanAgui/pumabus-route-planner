
from graph import Graph
from dijkstra import dijkstra


def construir_grafo_pumabus():
    g = Graph()

    # PARADAS PRINCIPALEs
    paradas = [
        "Metro CU", 
        "Estadio Olímpico", 
        "Facultad de Derecho", 
        "Rectoría", 
        "Biblioteca Central",
        "Ingeniería", 
        "Arquitectura",
        "Ciencias", 
        "Química"
    ]

    for p in paradas:
        g.agregarNodo(p)

    # RUTA 1 – CIRCUITO INTERIOR 
    g.agregarArista("Metro CU", "Estadio Olímpico", 2)
    g.agregarArista("Estadio Olímpico", "Facultad de Derecho", 3)
    g.agregarArista("Facultad de Derecho", "Rectoría", 2)
    g.agregarArista("Rectoría", "Biblioteca Central", 2)
    g.agregarArista("Biblioteca Central", "Ingeniería", 3)
    g.agregarArista("Ingeniería", "Arquitectura", 2)
    g.agregarArista("Arquitectura", "Ciencias", 3)
    g.agregarArista("Ciencias", "Química", 4)
    g.agregarArista("Química", "Metro CU", 5)


    # RUTA 3 – EXTERIOR (Ruta más rápida)
    g.agregarArista("Metro CU", "Ciencias", 5)
    g.agregarArista("Ciencias", "Estadio Olímpico", 4)
    g.agregarArista("Estadio Olímpico", "Metro CU", 3)

    return g



# MAIN 
if __name__ == "__main__":
    grafo = construir_grafo()

    print("Sistema de Rutas Pumabús")
    print("Paradas disponibles:")
    for nodo in grafo.list_adj:
        print(" -", nodo)

    print("\nEjemplo de consulta:")
    inicio = "Metro CU"
    destino = "Ingeniería"

    distancia, ruta = dijkstra(grafo, inicio, destino)

    if ruta:
        print(f"\nRuta más corta de {inicio} a {destino}:")
        print(" → ".join(ruta))
        print("Distancia total:", distancia)
    else:
        print(f"\nNo existe ruta entre {inicio} y {destino}.")
