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
        "Facultad de Economía",
        "Facultad de Odontología",
        "Facultad de Medicina",
        "Facultad de Veterinaria",
        "Estadio Olímpico", 
        "Facultad de Ciencias",
        "Facultad de Contaduría y Administración",
        "Escuela de Trabajo Social",
        "Metrobús CU",
        "Facultad de Ciencias Politicas y Sociales",
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
        "Anexo de Ingeniería",
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
    g.agregarArista("Metro CU", "Facultad de Química", 1.8)
    g.agregarArista("Facultad de Química", "ENALLT", 0.35)
    g.agregarArista("ENALLT", "Facultad de Ingeniería", 0.24)
    g.agregarArista("Facultad de Ingeniería", "Facultad de Arquitectura", 0.45)
    g.agregarArista("Facultad de Arquitectura", "Rectoría", 0.4)
    g.agregarArista("Rectoría", "Psicología", 0.3)
    g.agregarArista("Psicología", "Facultad de Derecho", 0.45)
    g.agregarArista("Facultad de Derecho", "Facultad de Economía", 0.3)
    g.agregarArista("Facultad de Economía", "Facultad de Odontología", 0.21)
    g.agregarArista("Facultad de Odontología", "Facultad de Medicina", 0.55)
    g.agregarArista("Facultad de Medicina", "Facultad de Veterinaria", 0.8)
    g.agregarArista("Facultad de Veterinaria", "Metro CU", 0.9)

    #RUTA 2 conexión con ruta 4, 6, 8, 9, 10, 11, 13
    g.agregarArista("Metro CU", "Facultad de Ciencias", 0.7)
    g.agregarArista("Facultad de Ciencias", "Facultad de Contaduría y Administración", 1.3)
    g.agregarArista("Facultad de Contaduría y Administración", "Escuela de Trabajo Social", 0.35)
    g.agregarArista("Escuela de Trabajo Social", "Metrobús CU", 0.45)
    g.agregarArista("Metrobús CU", "Facultad de Ciencias", 1)
    g.agregarArista("Facultad de Ciencias", "Metro CU", 0.7)

    # RUTA 3 – EXTERIOR (Ruta más rápida) conexión con ruta 1, ruta 5, ruta 10, 13
    g.agregarArista("Metro CU", "Facultad de Ciencias Polítias y Sociales", 1)
    g.agregarArista("Facultad de Ciencias Políticas y Sociales", "Biblioteca Nacional", 1.1)
    g.agregarArista("Biblioteca Nacional", "Zona Cultural", 0.35)
    g.agregarArista("Zona Cultural", "Avenida del IMAN", 1.1)
    g.agregarArista("Avenida del IMAN", "UNIVERSUM", 0.55)
    g.agregarArista("UNIVERSUM", "MUAC", 0.8)
    g.agregarArista("MUAC", "Tienda UNAM", 1.9)
    g.agregarArista("Tienda UNAM", "Metro CU", 0.45)

    #RUTA 4
    g.agregarArista("Metro CU", "Facultad de Ciencias", 0.7)
    g.agregarArista("Facultad de Ciencias", "Facultad de Contaduría y Administración", 1.3)
    g.agregarArista("Facultad de Contaduría y Administración", "Escuela de Trabajo Social", 0.35)
    g.agregarArista("Escuela de Trabajo Social", "Metrobús CU", 0.45)
    g.agregarArista("Metrobús CU", "Estadio de Prácticas", 0.6)
    g.agregarArista("Estadio de Prácticas", "Jardín Botánico", 6.9)
    g.agregarArista("Jardín Botánico", "Facultad de Ciencias", 6.2)
    g.agregarArista("Facultad de Ciencias", "Metro CU", 0.7)

    #RUTA 5 #Circuito exterior
    g.agregarArista("Metro CU", "Medicina", 1.2)
    g.agregarArista("Medicina", "Odontología", 0.45)
    g.agregarArista("Odontología", "Economía ", 0.19)
    g.agregarArista("Economía  ", "Derecho", 0.4)
    g.agregarArista("Derecho", "Filosofía", 0.3)
    g.agregarArista("Filosofía", "Facultad de Psicología", 0.15)
    g.agregarArista("Facultad de Psicología", "Facultad de Derecho", 0.45)
    g.agregarArista("Facultad de Derecho", "Facultad de Economía", 0.3)
    g.agregarArista("Facultad de Economía", "Facultad de Odontología", 0.21)
    g.agregarArista("Facultad de Odontología", "Facultad de Medicina", 0.55)
    g.agregarArista("Facultad de Medicina", "Facultad de Veterinaria", 0.8)
    g.agregarArista("Facultad de Veterinaria", "Metro CU", 0.9)

    #Base Estadio Olímpico
    #RUTA 6
    g.agregarArista("Estadio Olímpico", "Jardín Botánico", 5.3)
    g.agregarArista("Jardín Botánico", "Metrobús CU", 1.1)
    g.agregarArista("Metrobús CU", "Facultad de Ciencias", 1)
    g.agregarArista("Facultad de Ciencias", "Anexo de Ingeniería", 0.5)
    g.agregarArista("Anexo de Ingeniería", "Facultad de Contaduría y Administración", 0.7)
    g.agregarArista("Facultad de Contaduría y Administración", "Escuela de Trabajo Social", 0.35)
    g.agregarArista("Escuela de Trabajo Social", "Metrobús CU", 0.45)
    g.agregarArista("Metrobús CU", "Estadio de Prácticas", 0.6)
    g.agregarArista("Estadio de Prácticas", "MUCA", 0.6)
    g.agregarArista("MUCA", "Estacionamiento 8", 0.45)
    g.agregarArista("Estacionamiento 8", "Estacionamiento 7", 1.4)
    g.agregarArista("Estacionamiento 7", "Estacionamiento 6", 0.1)
    g.agregarArista("Estacionamiento 6", "Estacionamiento 4", 0.14)
    g.agregarArista("Estacionamiento 4", "Estacionamiento 3", 0.18)
    g.agregarArista("Estacionamiento 3", "Estacionamiento 2", 0.24)
    g.agregarArista("Estacionamiento 2", "Estadio Olímpico", 0.23)

    #RUTA 7
    g.agregarArista("Estadio Olímpico", "Facultad de Psicología", 1.2)
    g.agregarArista("Facultad de Psicología", "Facultad de Filosofía", 0.45)
    g.agregarArista("Facultad de Flosofía", "Facultad de Derecho", 0.2)
    g.agregarArista("Facultad de Derecho", "Facultad de Economía", 0.3)
    g.agregarArista("Facultad de Economía", "Facultad de Odontología", 0.21)
    g.agregarArista("Facultad de Odontología", "Facultad de Medicina", 0.55)
    g.agregarArista("Facultad de Medicina", "Facultad de Química", 0.85)
    g.agregarArista("Facultad de Química", "ENALLT", 0.35)
    g.agregarArista("ENALLT", "Facultad de Ingeniería", 0.24)
    g.agregarArista("Facultad de Ingeniería", "Facultad de Arquitectura", 0.45)
    g.agregarArista("Facultad de Arquitectura", "Estacionamiento 8", 0.65)
    g.agregarArista("Estacionamiento 8", "Estacionamiento 7", 1.4)
    g.agregarArista("Estacionamiento 7", "Estacionamiento 6", 0.1)
    g.agregarArista("Estacionamiento 6", "Estacionamiento 4", 0.14)
    g.agregarArista("Estacionamiento 4", "Estacionamiento 3", 0.18)
    g.agregarArista("Estacionamiento 3", "Estacionamiento 2", 0.24)
    g.agregarArista("Estacionamiento 2", "Estadio Olímpico", 0.23)

    #RUTA 8
    g.agregarArista("Estadio Olímpico", "Metrobús CU", 1.8)
    g.agregarArista("Metrobús CU", "Estadio de Prácticas", 0.6)
    g.agregarArista("Estadio de Prácticas", "Centro Médico", 0.8)
    g.agregarArista("Centro Médico", "Alberca", 0.2)
    g.agregarArista("Alberca", "Ingeniería", 0.04)
    g.agregarArista("Ingeniería", "IIMAS", 0.4)
    g.agregarArista("IIMAS", "Anexo de Ingeniería", 0.7) 
    g.agregarArista("Anexo de Ingeniería", "Facultad de Contaduría y Administración", 0.75) 
    g.agregarArista("Facultad de Contaduría y Administración", "Escuela de Trabajo Social", 0.35)
    g.agregarArista("Escuela de Trabajo Social", "Metrobús CU", 0.45)
    g.agregarArista("Metrobús CU", "Estadio de Prácticas", 0.6)
    g.agregarArista("Estadio de Prácticas", "MUCA", 0.6)
    g.agregarArista("MUCA", "Estacionamiento 8", 0.65) 
    g.agregarArista("Estacionamiento 8", "Estacionamiento 7", 1.4)
    g.agregarArista("Estacionamiento 7", "Estacionamiento 6", 0.1)
    g.agregarArista("Estacionamiento 6", "Estacionamiento 4", 0.14)
    g.agregarArista("Estacionamiento 4", "Estacionamiento 3", 0.18)
    g.agregarArista("Estacionamiento 3", "Estacionamiento 2", 0.24)
    g.agregarArista("Estacionamiento 2", "Estadio Olímpico", 0.23)

    #Base metrobús CU
    #RUTA 9
    g.agregarArista("Metrobús CU", "Estadio de Prácticas", 0.6)
    g.agregarArista("Estadio de Prácticas", "MUCA", 0.45)
    g.agregarArista("MUCA", "Rectoría", 0.35)
    g.agregarArista("Rectoría", "Psicología", 0.29)
    g.agregarArista("Psicología", "Facultad de Filosofía", 0.24)
    g.agregarArista("Facultad de Flosofía", "Facultad de Derecho", 0.2)
    g.agregarArista("Facultad de Derecho", "Facultad de Economía", 0.3)
    g.agregarArista("Facultad de Economía", "Facultad de Odontología", 0.21)
    g.agregarArista("Facultad de Odontología", "Facultad de Medicina", 0.55)
    g.agregarArista("Facultad de Medicina", "Anexo de Ingeniería", 1.1)
    g.agregarArista("Anexo de Ingeniería", "Facultad de Contaduría y Administración", 0.7)
    g.agregarArista("Facultad de Contaduría y Administración", "Escuela de Trabajo Social", 0.35)
    g.agregarArista("Escuela de Trabajo Social", "Metrobús CU", 0.45)

    #RUTA 10
    g.agregarArista("Metrobús CU", "Jardín Botánico", 1.9)
    g.agregarArista("Jardín Botánico", "Biblioteca Nacional", 2.2)
    g.agregarArista("Biblioteca Nacional", "Zona Cultural", 0.35)
    g.agregarArista("Zona Cultural", "Avenida del IMAN", 1.1)
    g.agregarArista("Avenida del IMAN", "UNIVERSUM", 0.55)
    g.agregarArista("UNIVERSUM", "MUAC", 0.8)
    g.agregarArista("MUAC", "Biblioteca Nacional", 0.28)
    g.agregarArista("Biblioteca Nacional", "Espacio Escultorico", 1.2)
    g.agregarArista("Espacio Escultorico", "Tienda UNAM", 2)
    g.agregarArista("Tienda UNAM", "Facultad de Ciencias Políticas y Sociales", 0.26)
    g.agregarArista("Facultad de Ciencias Políticas y Sociales", "Metrobús CU", 2.3)


    #RUTA 11
    g.agregarArista("Metrobús CU", "Estadio de Prácticas", 0.6)
    g.agregarArista("Estadio de Prácticas", "MUCA", 0.45)
    g.agregarArista("MUCA", "Estacionamiento 8", 0.65)
    g.agregarArista("Estacionamiento 8", "Estacionamiento 7", 1.4)
    g.agregarArista("Estacionamiento 7", "Anexo de Filosofía", 1)
    g.agregarArista("Anexo de Filosofía", "Jardín Botánico", 1.6)
    g.agregarArista("Jardín Botánico", "Metrobús CU", 3)

    #RUTA 12
    g.agregarArista("Estadio Olímpico", "Psicología", 0.850)
    g.agregarArista("Psicología", "Facultad de Filosofía", 0.24)
    g.agregarArista("Facultad de Flosofía", "Facultad de Derecho", 0.2)
    g.agregarArista("Facultad de Derecho", "Facultad de Economía", 0.3)
    g.agregarArista("Facultad de Economía", "Facultad de Odontología", 0.21)
    g.agregarArista("Facultad de Odontología", "Facultad de Medicina", 0.55)
    g.agregarArista("Facultad de Medicina", "Facultad de Química", 0.85)
    g.agregarArista("Facultad de Química", "ENALLT", 0.35)
    g.agregarArista("ENALLT", "Facultad de Ingeniería", 0.24)
    g.agregarArista("Facultad de Ingeniería", "Facultad de Arquitectura", 0.45)
    g.agregarArista("Facultad de Arquitectura", "Estacionamiento 8", 0.65)
    g.agregarArista("Estacionamiento 8", "Estacionamiento 7", 1.4)
    g.agregarArista("Estacionamiento 7", "Estacionamiento 6", 0.1)
    g.agregarArista("Estacionamiento 6", "Estacionamiento 4", 0.14)
    g.agregarArista("Estacionamiento 4", "Estacionamiento 3", 0.18)
    g.agregarArista("Estacionamiento 3", "Estacionamiento 2", 0.24)
    g.agregarArista("Estacionamiento 2", "Estadio Olímpico", 0.23)
    

    #RUTA 13
    g.agregarArista("Metrobús CU", "Facultad de Filosofía", 1.5)
    g.agregarArista("Facultad de Flosofía", "Facultad de Derecho", 0.2)
    g.agregarArista("Facultad de Derecho", "Facultad de Economía", 0.3)
    g.agregarArista("Facultad de Economía", "Facultad de Odontología", 0.21)
    g.agregarArista("Facultad de Odontología", "Facultad de Medicina", 0.55)
    g.agregarArista("Facultad de Medicina", "Anexo de Ingeniería", 1.1)
    g.agregarArista("Anexo de Ingeniería", "Facultad de Contaduría y Administración", 0.7)
    g.agregarArista("Facultad de Contaduría y Administración", "Escuela de Trabajo Social", 0.35)
    g.agregarArista("Escuela de Trabajo Social", "Metrobús CU", 0.45)
    g.agregarArista("Metrobús CU", "Estadio de Prácticas", 0.6)
    g.agregarArista("Estadio de Prácticas", "Biblioteca Nacional", 2.3)
    g.agregarArista("Biblioteca Nacional", "Zona Cultural", 0.35)
    g.agregarArista("Zona Cultural", "UNIVERSUM", 1.5)
    g.agregarArista("UNIVERSUM", "Tienda UNAM", 2.2)
    g.agregarArista("Tienda UNAM", "Facultad de Ciencias Políticas y Sociales", 0.26)
    g.agregarArista("Facultad de Ciencias Políticas y Sociales", "Metrobús CU", 2.3)
    g.agregarArista("Metrobús CU", "Estadio de Prácticas", 0.6)
    g.agregarArista("Estadio de Prácticas", "MUCA", 0.9)
    g.agregarArista("MUCA", "Rectoría", 0.35)
    g.agregarArista("Rectoría", "Psicología", 0.29)
    g.agregarArista("Psicología", "Facultad de Filosofía", 0.8)
    g.agregarArista("Facultad de Filosofía", "Metrobús CU", 2.6)
    return g

# MAIN 
if __name__ == "__main__":
    grafo = construir_grafo_pumabus()

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