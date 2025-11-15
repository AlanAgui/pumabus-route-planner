from graph import Graph
import heapq

def dijkstra(graph, inicio, destino):
    # Acumular distancias
    distancia = {nodo : float("inf") for nodo in graph.list_adj}
    # infinito positivo 

    distancia[inicio] = 0

    # Reconstruir la ruta 
    padre = {nodo : None for nodo in graph.list_adj}

    # priority queue
    priority_queuee = [(0, inicio)]

    while priority_queuee:
        actual_distance, nodo = heapq.heappop(priority_queuee)

        if actual_distance > distancia[nodo]:
            continue 

        if nodo == destino:
            # se reconstruye la ruta
            ruta = []
            temp = nodo
            while temp is not None:
                ruta.append(temp)
                temp = padre[temp]
                
            reversa = list(reversed(ruta))
            return distancia[destino], reversa
        
        for vecino, weight in graph.list_adj[nodo]:
            nueva_distancia = actual_distance + weight

            if nueva_distancia < distancia[vecino]:
                distancia[vecino] = nueva_distancia
                padre[vecino] = nodo
                heapq.heappush(priority_queuee, (nueva_distancia,vecino))

        
    return float("inf"), []