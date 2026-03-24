torneo = {}

while True:
    print("1 - Agregar equipo")
    print("2 - Registrar resultado (4 - 2)")
    print("3 - Mostrar tabla de posiciones")
    print("4 - Eliminar equipo")
    print("5 - Salir")
    opcion = int(input("Elegís una opcion: "))

    if opcion == 1: 
        equipo = input("Nombre del equipo: ").lower()
        if equipo not in torneo:
            torneo[equipo] = 0
            print(f"Equipo '{equipo}' agregado.")
        else:
            print(f"El equipo '{equipo}' ya existe.")

    if opcion == 2:
        local = input("Equipo local: ").lower()
        visitante = input("Equipo visitante: ").lower()

        marcador = input("Ingrese marcador en formato 4 - 2: ").split("-")
        if local not in torneo or visitante not in torneo:
            print("Uno o ambos equipos no existen")
        else:
            golsl = int(marcador[0])
            golsv = int(marcador[1])

            if golsl > golsv:
                torneo[local] += 3
            elif golsv > golsl:
                torneo[visitante] += 3
            else:
                torneo[local] += 1
                torneo[visitante] += 1
            print(f"Partida agregada: {local} {golsl} - {golsv} {visitante}")
    if opcion == 3:
        for equipo in torneo:
            print(f" {equipo}: {torneo[equipo]}")

    if opcion == 4:
        equipo_eliminar = input("Qué equipo desea eliminar? ")
        if equipo_eliminar in torneo:
            torneo.pop(equipo_eliminar)
            print(f"Equipo '{equipo_eliminar}' eliminado.")
        else:
            print("El equipo no se encuentra en el torneo.")

    elif opcion == 5:
        print("Saliendo...")
        break

    else:
        print("Opción no válida.")
