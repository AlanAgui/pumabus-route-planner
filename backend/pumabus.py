
from graph import Graph
from dijkstra import dijkstra


def construir_grafo_pumabus():
    g = Graph()

    # PARADAS PRINCIPALEs
    paradas = [
        "Metro CU", 
        "ENALLT",
        "Facultad de Ingeniería", 
        "Facultad de Arquitectura",
        "Facultad de Química",
        "Rectoría", 
        "Biblioteca Central",
        "Psicología",
        "Facultad de Filosofía",
        "Facultad de Derecho",
        "Facultad de Econimía",
        "Facultad de Odontología",
        "Facultad de Medicina",
        "Facultad de Veterinaria",
        "Estadio Olímpico", 
        "Facultad de Ciencias",
        "Facultad de Contaduria y Administración",
        "Escuela de Trabajo Social",
        "Metrobús CU",
        "Facultad de CIencias Politicas y Sociales",
        "Biblioteca Nacional",
        "Zona Cultural",
        "Avenida del IMAN",
        "UNIVERSUM",
        "MUAC",
        "Espacio escultorico",
        "Tienda UNAM",
        "Estadio de Prácticas",
        "Jardín Botánico",
        "Medicina",
        "Odontología",
        "Economía",
        "Derecho",
        "Filosofía",
        "Psicología",
        "Ingeniería",
        "Química", 
        "Anexo de Ingenieria",
        "MUCA",
        "Estacionamiento 8",
        "Estacionamiento 7",
        "Estacionamiento 6",
        "Estacionamiento 5",
        "Estacionamiento 4",
        "Estacionamiento 3",
        "Estacionamiento 2",
        "Estacionamiento 1",
        "Centro Médico", 
        "Alberca",
        "IIMAS",
        "Anexo de Filosofía",
    ]

    for p in paradas:
        g.agregarNodo(p)

    # RUTA 1 – CIRCUITO INTERIR
    g.agregarArista("Metro CU", "Facultad de Química", 2)
    g.agregarArista("Facultad de Química", "ENALLT", 3)
    g.agregarArista("ENALLT", "Facultad de Ingenieria", 2)
    g.agregarArista("Facultad de Ingenieria", "Facultad de Arquitectura", 2)
    g.agregarArista("Facultad de Arquitectura", "Rectoria", 3)
    g.agregarArista("Rectoria", "Psicología", 2)
    g.agregarArista("Facultad de Psicología", "Facultad de Derecho", 3)
    g.agregarArista("Facultad de Derecho", "Facultad de Economía", 4)
    g.agregarArista("Facultad de Economía", "Facultad de Odontología", 5)
    g.agregarArista("Facultad de Odontología", "Facultad de Medicina", 3)
    g.agregarArista("Facultad de Medicina", "Facultad de Veterinaria", 4)
    g.agregarArista("Facultad de Veterinaria", "Metro CU", 5)

    

    # RUTA 3 – EXTERIOR (Ruta más rápida) conexión con ruta 1, ruta 5, ruta 10, 13
    g.agregarArista("Metro CU", "Facultad de Ciencias Polítias y Sociales", 5)
    g.agregarArista("Facultad de Ciencias Políticas y Sociales", "Biblioteca Nacional", 4)
    g.agregarArista("Biblioteca Nacional", "Zona Cultural", 3)
    g.agregarArista("Zona Cultural", "Avenida del IMAN", 5)
    g.agregarArista("Avenida del IMAN", "UNIVERSUM", 4)
    g.agregarArista("UNIVERSUM", "MUAC", 3)
    g.agregarArista("MUAC", "Tienda UNAM", 5)
    g.agregarArista("TIenda UNAM", "Metro CU", 4)

    #RUTA 4
    g.agregarArista("Metro CU", "Facultad de Ciencias", 2)
    g.agregarArista("Facultad de Ciencias", "Facultad de Contaduria y Administración", 3)
    g.agregarArista("Facultad de Contaduria y Administración", "Escuela de Trabajo Social", 2)
    g.agregarArista("Escuela de Trabajo Social", "Metrobús CU", 2)
    g.agregarArista("Metrobús CU", "Estadio de Prácticas", 3)
    g.agregarArista("Estadio de Prácticas", "Jardín Botánico", 2)
    g.agregarArista("Jardíb Botánico", "Facultad de Ciencias", 2)
    g.agregarArista("Facultad de Ciencias", "Metro CU", 2)

    #RUTA 5 #Circuito exterior
    g.agregarArista("Metro CU", "Medicina", 2) 2.3
    g.agregarArista("Medicina", "Odontología", 3) 1.2
    g.agregarArista("Odontología", "Economía ", 2) 1.1 
    g.agregarArista("Economía  ", "Derecho", 2) 1
    g.agregarArista("Derecho", "Filosofía", 3) 1
    g.agregarArista("Filosofía", "Facultad de Psicología", 2) 0.8
    g.agregarArista("Facultad de Psicología", "Facultad de Derecho", 3) 0.8 
    g.agregarArista("Facultad de Derecho", "Facultad de Economía", 4) 1
    g.agregarArista("Facultad de Economía", "Facultad de Odontología", 5)1.1
    g.agregarArista("Facultad de Odontología", "Facultad de Medicina", 3) 1.2
    g.agregarArista("Facultad de Medicina", "Facultad de Veterinaria", 4) 1
    g.agregarArista("Facultad de Veterinaria", "Metro CU", 5) 2

    #Base Estadio Olímpico
    #RUTA 6
    g.agregarArista("Estadio Olímpico", "Jardín Botánico", 2)
    g.agregarArista("Jardín Botánico", "Metrobús CU", 3)
    g.agregarArista("Metrobús CU", "Facultad de Ciencias ", 2)
    g.agregarArista("Facultad de Ciencias", "Anexo de Ingenieria", 2)
    g.agregarArista("Anexo de Ingeniería", "Facultad de Contaduría y Administración", 3)
    g.agregarArista("Facultad de Contaduría y Administración", "Escuela de Trabajo Social", 2)
    g.agregarArista("Escuela de Trabajo Social", "Metrobús CU", 3)
    g.agregarArista("Metrobús CU", "Estadio de Prácticas", 4)
    g.agregarArista("Estadio de Prácticas", "MUCA", 5)
    g.agregarArista("MUCA", "Estacionamiento 8", 3)
    g.agregarArista("Estacionamiento 8", "Estacionamiento 7", 4)
    g.agregarArista("Estacionamiento 7", "Estacionamiento 6", 5)
    g.agregarArista("Estacionamiento 6", "Estacionamiento 4", 5)
    g.agregarArista("Estacionamiento 4", "Estacionamiento 3", 5)
    g.agregarArista("Estacionamiento 3", "Estacionamiento 2", 5)
    g.agregarArista("Estacionamiento 2", "Estadio Olímpico", 5)

    #RUTA 7
    g.agregarArista("Estadio Olímpico", "Facultad de Psicología", 2)
    g.agregarArista("Facultad de Psicología", "Facultad de Filosofía", 3)
    g.agregarArista("Facultad de Flosofía", "Facultad de Derecho", 2)
    g.agregarArista("Facultad de Derecho", "Facultad de Economía", 2)
    g.agregarArista("Facultad de Economía", "Facultad de Odontología", 3)
    g.agregarArista("Facultad de Odontología", "Facultad de Medicina", 2)
    g.agregarArista("Facultad de Medicina", "Facultad de Química", 3)
    g.agregarArista("Facultad de Química", "ENALLT", 4)
    g.agregarArista("Estadio de Prácticas", "MUCA", 5)
    g.agregarArista("ENALLT", "Facultad de Ingeniería", 3)
    g.agregarArista("Facultad de Ingeniería", "Facultad de Arquitectura", 3)
    g.agregarArista("Facultad de Arquitectura", "Estacionamiento 8", 3)
    g.agregarArista("Estacionamiento 8", "Estacionamiento 7", 4)
    g.agregarArista("Estacionamiento 7", "Estacionamiento 6", 5)
    g.agregarArista("Estacionamiento 6", "Estacionamiento 4", 5)
    g.agregarArista("Estacionamiento 4", "Estacionamiento 3", 5)
    g.agregarArista("Estacionamiento 3", "Estacionamiento 2", 5)
    g.agregarArista("Estacionamiento 2", "Estadio Olímpico", 5)

    #RUTA 8
    g.agregarArista("Estadio Olímpico", "Metrobús CU", 2) 3.1
    g.agregarArista("Metrobús CU", "Estadiode de Prácticas", 3) 1
    g.agregarArista("Estadio de Prácticas", "Centro Médico", 2) 1.5
    g.agregarArista("Centro Médico", "Alberca", 2) 0.1
    g.agregarArista("Alberca", "Ingeniería", 3) 0.3
    g.agregarArista("Igeniería", "IIMAS", 2) 0.9
    g.agregarArista("IIMAS", "Anexo de Ingeniería", 3) 0.5
    g.agregarArista("Anexo de Ingeniería", "FAcultad de COntaduría y Administración", 4) 0.15
    g.agregarArista("Facultad de Contaduria y Administración", "Escuela de Trabajo Social", 5) 0.6
    g.agregarArista("Escuela de Trabajo Social", "Metrobús CU", 3) 2.9
    g.agregarArista("Metrobús CU", "Estadio de Prácticas", 3) 0.5
    g.agregarArista("Estadio de Prácticas", "MUCA", 3) 0.7
    g.agregarArista("MUCA", "Estacionamiento 8", 4) 0.7
    g.agregarArista("Estacionamiento 8", "Estacionamiento 7", 4) 0.3 
    g.agregarArista("Estacionamiento 7", "Estacionamiento 6", 5) 0.15
    g.agregarArista("Estacionamiento 6", "Estacionamiento 4", 5) 0.4
    g.agregarArista("Estacionamiento 4", "Estacionamiento 3", 5) 0.4
    g.agregarArista("Estacionamiento 3", "Estacionamiento 2", 5) 0.5
    g.agregarArista("Estacionamiento 2", "Estadio Olímpico", 5) 0.4

    #Base metrobús CU
    #RUTA 9
    g.agregarArista("Metrobús CU", "Estadio de Prácticas", 2)0.5
    g.agregarArista("Estadio de Prácticas", "MUCA", 3) 0.7
    g.agregarArista("MUCA", "Rectoría", 2) 0.9
    g.agregarArista("Rectoría", "Psicología", 2) 1.1
    g.agregarArista("Psicología", "Facultad de Filosofía", 3) 1.5
    g.agregarArista("Facultad de Filosofía", "Facultad de Derecho", 2) 0.3
    g.agregarArista("Facultad de Derecho", "Facultad de Economía", 3) 0.150
    g.agregarArista("Facultad de Economía", "Facultad de Odontología", 3) 1.3
    g.agregarArista("Facultad de Odontología", "Facultad de Medicina", 2) 0.9
    g.agregarArista("Facultad de Medicina", "Anexo de Ingenieria", 3) 0.9
    g.agregarArista("Anexo de Ingeniería", "FAcultad de COntaduría y Administración", 4) 1.9
    g.agregarArista("Facultad de Contaduria y Administración", "Escuela de Trabajo Social", 5)0.6
    g.agregarArista("Escuela de Trabajo Social", "Metrobús CU", 3) 2.9

    #RUTA 10
    g.agregarArista("Metrobús CU", "Jardín Botánico", 2)
    g.agregarArista("Jardín Botánico", "Biblioteca Nacional", 3)
    g.agregarArista("Biblioteca Nacional", "Zona Cultural", 2)
    g.agregarArista("Zona Cultural", "Avenida del IMAN", 2)
    g.agregarArista("Avenida del IMAN", "UNIVERSUM", 3)
    g.agregarArista("UNIVERSUM", "MUAC", 2)
    g.agregarArista("MUAC", "Biblioteca Nacional", 3)
    g.agregarArista("Biblioteca Nacional", "Espacio Escultorico", 3)
    g.agregarArista("Espacio Escultorico", "Tienda UNAM", 2)
    g.agregarArista("Tienda UNAM", "Facultad de Ciencias Políticas y Sociales", 3)
    g.agregarArista("Facultad de Ciencias Políticas y Sociales", "Metrobús CU", 4)

    #RUTA 11
    g.agregarArista("Metrobús CU", "Estadio de Prácticas", 2)
    g.agregarArista("Estadio de Prácticas", "MUCA", 3)
    g.agregarArista("MUCA", "Estacionamiento 8", 2)
    g.agregarArista("Estacionamiento 8", "Estacionamiento 7", 5)
    g.agregarArista("Estacionamiento 7", "Anexo de Filosofía", 5)
    g.agregarArista("Anexo de Filosofía", "Jardín Botánico", 2)
    g.agregarArista("Jardín Botánico", "Metrobús CU", 3)

    #RUTA 12
    g.agregarArista("Estadio Olímpico", "Psicología", 2) 0.2
    g.agregarArista("Psicología", "Facultad de Filosofía", 3)1.5
    g.agregarArista("Facultad de Flosofía", "Facultad de Derecho", 2) 0.3
    g.agregarArista("Facultad de Derecho", "Facultad de Economía", 2) 0.1
    g.agregarArista("Facultad de Economía", "Facultad de Odontología", 3) 1.7
    g.agregarArista("Facultad de Odontología", "Facultad de Medicina", 2) 1
    g.agregarArista("Facultad de Medicina", "Facultad de Química", 3) 0.8
    g.agregarArista("Facultad de Química", "ENALT", 4) 0.5
    g.agregarArista("Estadio de Prácticas", "MUCA", 5) 0.7
    g.agregarArista("ENALT", "Facultad de Ingeniería", 3) 0.2
    g.agregarArista("Facultad de Ingeniería", "Facultad de Arquitectura", 3) 0.2
    g.agregarArista("Facultad de Arquitectura", "Estacionamiento 8", 3) 0.7
    g.agregarArista("Estacionamiento 8", "Estacionamiento 7", 4) 0.3 
    g.agregarArista("Estacionamiento 7", "Estacionamiento 6", 5) 0.15
    g.agregarArista("Estacionamiento 6", "Estacionamiento 4", 5) 0.4
    g.agregarArista("Estacionamiento 4", "Estacionamiento 3", 5) 0.4
    g.agregarArista("Estacionamiento 3", "Estacionamiento 2", 5) 0.5
    g.agregarArista("Estacionamiento 2", "Estadio Olímpico", 5) 0.3
    

    #RUTA 13
    g.agregarArista("Metrobús CU", "Facultad de Filosofía", 3) 1.5
    g.agregarArista("Facultad de Flosofía", "Facultad de Derecho", 2)0.3
    g.agregarArista("Facultad de Derecho", "Facultad de Economía", 2) 0.15
    g.agregarArista("Facultad de Economía", "Facultad de Odontología", 3) 1.3
    g.agregarArista("Facultad de Odontología", "Facultad de Medicina", 2)1
    g.agregarArista("Facultad de Medicina", "Anexo de Ingeniería", 3)0.8
    g.agregarArista("Anexo de Ingeniería", "FAcultad de COntaduría y Administración", 4) 0.15
    g.agregarArista("Facultad de Contaduria y Administración", "Escuela de Trabajo Social", 5) 0.6
    g.agregarArista("Escuela de Trabajo Social", "Metrobús CU", 3) 2.9
    g.agregarArista("Metrobús CU", "Estadio de Prácticas", 5) 0.6
    g.agregarArista("Estadio de Prácticas", "Biblioteca Nacional", 3)1.1
    g.agregarArista("Biblioteca Nacional", "Zona Cultural", 3) 2.5
    g.agregarArista("Zona Cultural", "UNIVERSUM", 3) 1.8
    g.agregarArista("UNIVERSUM", "Tienda UNAM", 4) 2.7
    g.agregarArista("Tienda UNAM", "Facultad de Ciencias Políticas y Sociales", 5) 3.5
    g.agregarArista("Facultad de Ciencias Políticas y Sociales", "Metrobús CU", 5) 1.7
    g.agregarArista("Metrobús CU", "Estadio de Prácticas", 5) 0.5
    g.agregarArista("Estadio de Prácticas", "MUCA", 5)0.7
    g.agregarArista("MUCA", "Rectoría", 5) 0.9
    g.agregarArista("Rectoría", "Psicología", 5) 1.1
    g.agregarArista("Psicología", "Facultad de Filosofía", 5) 1.5
    g.agregarArista("Facultad de Filosofía", "Metrobús CU", 5)2.8
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
