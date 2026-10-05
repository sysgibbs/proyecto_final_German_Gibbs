cartelera = {
    "Lunes": [
        {
            "pelicula": "Resident Evil: Noche Cero",
            "sala": 1,
            "horario": "2:00 pm",
            "formato": "Normal",
        },
        {
            "pelicula": "Avengers: Endgame (reestreno)",
            "sala": 2,
            "horario": "4:30 pm",
            "formato": "3D",
        },
        {
            "pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2",
            "sala": 3,
            "horario": "6:00 pm",
            "formato": "4DX",
        },
        {
            "pelicula": "Rápido y Furioso (reestreno)",
            "sala": 4,
            "horario": "5:30 pm",
            "formato": "Normal",
        },
        {"pelicula": "El Final", "sala": 5, "horario": "8:00 pm", "formato": "CXC"},
    ],
    "Martes": [
        {
            "pelicula": "Resident Evil: Noche Cero",
            "sala": 3,
            "horario": "5:00 pm",
            "formato": "4DX",
        },
        {
            "pelicula": "Avengers: Endgame (reestreno)",
            "sala": 1,
            "horario": "7:00 pm",
            "formato": "Normal",
        },
        {
            "pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2",
            "sala": 2,
            "horario": "3:00 pm",
            "formato": "Normal",
        },
        {
            "pelicula": "Rápido y Furioso (reestreno)",
            "sala": 5,
            "horario": "6:30 pm",
            "formato": "3D",
        },
        {"pelicula": "El Final", "sala": 4, "horario": "9:00 pm", "formato": "Normal"},
    ],
    "Miércoles": [
        {
            "pelicula": "Resident Evil: Noche Cero",
            "sala": 4,
            "horario": "4:00 pm",
            "formato": "Normal",
        },
        {
            "pelicula": "Avengers: Endgame (reestreno)",
            "sala": 5,
            "horario": "2:30 pm",
            "formato": "CXC",
        },
        {
            "pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2",
            "sala": 1,
            "horario": "7:30 pm",
            "formato": "3D",
        },
        {
            "pelicula": "Rápido y Furioso (reestreno)",
            "sala": 2,
            "horario": "5:00 pm",
            "formato": "Normal",
        },
        {"pelicula": "El Final", "sala": 3, "horario": "8:30 pm", "formato": "4DX"},
    ],
    "Jueves": [
        {
            "pelicula": "Resident Evil: Noche Cero",
            "sala": 2,
            "horario": "6:30 pm",
            "formato": "3D",
        },
        {
            "pelicula": "Avengers: Endgame (reestreno)",
            "sala": 3,
            "horario": "3:30 pm",
            "formato": "Normal",
        },
        {
            "pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2",
            "sala": 4,
            "horario": "8:00 pm",
            "formato": "Normal",
        },
        {
            "pelicula": "Rápido y Furioso (reestreno)",
            "sala": 1,
            "horario": "2:00 pm",
            "formato": "4DX",
        },
        {"pelicula": "El Final", "sala": 5, "horario": "5:30 pm", "formato": "CXC"},
    ],
    "Viernes": [
        {
            "pelicula": "Resident Evil: Noche Cero",
            "sala": 5,
            "horario": "4:00 pm",
            "formato": "Normal",
        },
        {
            "pelicula": "Avengers: Endgame (reestreno)",
            "sala": 4,
            "horario": "7:00 pm",
            "formato": "3D",
        },
        {
            "pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2",
            "sala": 1,
            "horario": "5:30 pm",
            "formato": "CXC",
        },
        {
            "pelicula": "Rápido y Furioso (reestreno)",
            "sala": 3,
            "horario": "9:00 pm",
            "formato": "Normal",
        },
        {"pelicula": "El Final", "sala": 2, "horario": "2:30 pm", "formato": "4DX"},
    ],
    "Sábado": [
        {
            "pelicula": "Resident Evil: Noche Cero",
            "sala": 1,
            "horario": "3:00 pm",
            "formato": "Normal",
        },
        {
            "pelicula": "Avengers: Endgame (reestreno)",
            "sala": 2,
            "horario": "6:00 pm",
            "formato": "4DX",
        },
        {
            "pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2",
            "sala": 5,
            "horario": "8:30 pm",
            "formato": "3D",
        },
        {
            "pelicula": "Rápido y Furioso (reestreno)",
            "sala": 4,
            "horario": "4:30 pm",
            "formato": "Normal",
        },
        {"pelicula": "El Final", "sala": 3, "horario": "7:30 pm", "formato": "CXC"},
    ],
    "Domingo": [
        {
            "pelicula": "Resident Evil: Noche Cero",
            "sala": 3,
            "horario": "2:30 pm",
            "formato": "3D",
        },
        {
            "pelicula": "Avengers: Endgame (reestreno)",
            "sala": 5,
            "horario": "5:00 pm",
            "formato": "Normal",
        },
        {
            "pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2",
            "sala": 2,
            "horario": "7:00 pm",
            "formato": "CXC",
        },
        {
            "pelicula": "Rápido y Furioso (reestreno)",
            "sala": 1,
            "horario": "8:30 pm",
            "formato": "4DX",
        },
        {"pelicula": "El Final", "sala": 4, "horario": "4:00 pm", "formato": "Normal"},
    ],
}


def InicializarSistema():
    for funciones in cartelera.values():
        for funcion in funciones:

            matriz = []

            for a in range(5):
                fila = ["."] * 6
                matriz.append(fila)

            funcion["asientos"] = matriz
            funcion["reservas"] = {}


def obtenerFuncion():

    while True:
        dia = (
            input("Seleccione el dia a mostrar (Lunes-Domingo): ").capitalize().strip()
        )

        if dia in cartelera:
            break

        print("El dia seleccionado no existe. Intente de nuevo")

    verCartelera(dia)

    encontrado = False

    while not encontrado:
        horario = input("Seleccione la hora (pm): ").strip()
        verCartelera(dia)

        try:
            sala = int(input("Seleccione la sala: "))
        except (ValueError):
            print("Sala invalida")
            continue

        for funcion in cartelera[dia]:
            if horario == funcion["horario"] and sala == funcion["sala"]:
                encontrado = True
                break
        if not encontrado:
            verCartelera(dia)
            print(
                "======= Hora incorrecta o sala incorrecta. Intente de nuevo. ======="
            )
    return dia, horario, sala


def verCartelera(dia):
    if dia not in cartelera:
        print("El dia seleccionado no existe")
        return

    funciones = cartelera[dia]
    print(f"\n================ {dia} ================")

    for funcion in funciones:

        print(
            f"Pelicula: {funcion['pelicula']} | Sala: {funcion['sala']} | {funcion['horario']} | {funcion['formato']}"
        )


def mostrarMatriz(matriz_a_mostrar):
    listaNums = []

    for c in range(1, 7):
        columnas = str(c)
        listaNums.append(columnas)
    resultado = " ".join(listaNums)
    print(f"   {resultado}")

    for indice, fila in enumerate(matriz_a_mostrar):
        letraFila = chr(indice + 65)
        filaVisual = " ".join(fila)

        print(f"{letraFila}: {filaVisual}")


def mostrarAsientos(dia, horario, sala):
    asientos = cartelera[dia]
    for asiento in asientos:
        if asiento["sala"] == sala and asiento["horario"] == horario:
            print(
                f"Pelicula: {asiento['pelicula']} | Sala seleccionada: #{asiento['sala']} | En horario {asiento['horario']} | En: {asiento['formato']}."
            )

            print(f"\n========== Asientos sala: #{asiento['sala']} ==========")
            return asiento["asientos"], asiento["reservas"]


def contarAsientos(matriz):

    libres = 0
    ocupados = 0

    for fila in matriz:
        for asiento in fila:
            if asiento == ".":
                libres += 1
            elif asiento == "X":
                ocupados += 1

    return libres, ocupados


def disponibilidadDia(dia):

    if dia not in cartelera:
        print("El dia seleccionado no existe.")
        return

    for funcion in cartelera[dia]:
        libres, ocupados = contarAsientos(funcion["asientos"])

        total = libres + ocupados
        porcentaje = (ocupados / total) * 100

        print(
            f"Pelicula: {funcion['pelicula']} | Sala: {funcion['sala']} | Horario: {funcion['horario']} | Libres: {libres} | Ocupados: {ocupados} | Total asientos ocupados: {porcentaje:.1f}%"
        )


InicializarSistema()

opcion = 0

while opcion != 6:

    print("""\n===== CineMax - Sistema de Reservas =====
1. Ver cartelera de un día
2. Mostrar asientos de una función
3. Reservar asiento
4. Cancelar reserva
5. Ver disponibilidad
6. Salir
        """)
    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("\n Debe ingresar un numero.")
        continue

    if opcion == 1:
        dia = input("Seleccion una opcion (Lunes-Domingo): ").capitalize().strip()
        verCartelera(dia)


    elif opcion == 2:

        dia, horario, sala = obtenerFuncion()

        matriz, reservas = mostrarAsientos(dia, horario, sala)

        if matriz is not None:
            mostrarMatriz(matriz)

            print("\n================ Reservas ================")

            if not reservas:
                print("No hay reservas para esta funcion.")

            else:
                for asiento, nombre in reservas.items():
                    print(f"Asiento {asiento}: reservado por {nombre}")


    elif opcion == 3:
        print("\n================ Asiento a reservar ================")

        dia, horario, sala = obtenerFuncion()

        matriz, reservas = mostrarAsientos(dia, horario, sala)
        mostrarMatriz(matriz)

        while True:

            asiento = input("Seleccione el asiento (Ej: A2): ").upper().strip()

            if len(asiento) < 2 or not asiento[0].isalpha() or not asiento[1:].isdigit():

                print("Formato invalido. Ingrese una letra seguida de un numero.")
                continue

            fila = ord(asiento[0]) - 65
            columna = int(asiento[1:]) - 1

            if 0 <= fila < 5 and 0 <= columna < 6:
                break
            else:
                print("El asiento seleccionado no existe en la sala")

        if matriz[fila][columna] == ".":
            nombre = input("Ingrese el nombre de quien reserva: ").strip()

            matriz[fila][columna] = "X"
            reservas[asiento] = nombre

            print(f"{nombre} | {dia} | Asiento: {asiento} reservado con exito.")
        else:
            print("Lo sentimos este asiento esta ocupado.")

    elif opcion == 4:

        print("\n================ Reserva a cancelar ================")

        dia, horario, sala = obtenerFuncion()

        matriz, reservas = mostrarAsientos(dia, horario, sala)
        mostrarMatriz(matriz)

        if not reservas:
            print("No hay reservas para esta funcion.")
        else:
            print("\n================ Reservas actuales ================")

            for asiento, nombre in reservas.items():
                print(f"Asiento {asiento}: reservado por {nombre}")

        while True:

            asiento = (
                input("Seleccione el asiento a cancelar (Ej: A2): ").upper().strip()
            )

            if len(asiento) < 2 or not asiento[0].isalpha() or not asiento[1:].isdigit():

                print("Formato invalido. Ingrese una letra seguida de un numero.")
                continue

            fila = ord(asiento[0]) - 65
            columna = int(asiento[1:]) - 1

            if 0 <= fila < 5 and 0 <= columna < 6:
                break
            else:
                print("El asiento seleccionado no existe en la sala")

        if matriz[fila][columna] == "X":
            matriz[fila][columna] = "."

            if asiento in reservas:
                del reservas[asiento]

            print(f"{dia} = Reserva del asiento {asiento} cancelado con exito.")
        else:
            print("El asiento seleccionado ya estaba libre.")

    elif opcion == 5:
        print("================ Ver disponibilidad de asientos ================")
        dia = input("Seleccione una opcion (Lunes-Domingo): ").capitalize().strip()
        disponibilidadDia(dia)

    elif opcion == 6:
        print("Saliendo...")
    else:
        print("Opcion invalida")
