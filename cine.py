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

    dia = (input("Seleccione el dia a mostrar (Lunes-Domingo): ").capitalize().strip())
    verCartelera(dia)

    encontrado = False

    while not encontrado:
        horario = input("Seleccione la hora (pm): ").strip()
        verCartelera(dia)
        sala = int(input("Seleccione la sala: "))

        for funcion in cartelera[dia]:
            if horario == funcion["horario"] and sala == funcion["sala"]:
                encontrado = True
                break
        if not encontrado:
            verCartelera(dia)
            print("======= Hora incorrecta o sala incorrecta. Intente de nuevo. =======")
    return dia, horario, sala

def verCartelera(dia):
    if dia not in cartelera:
        print("El dia seleccionado no existe")
        return

    funciones = cartelera[dia]
    print(
        f"\n================================================ {dia} ================================================"
    )

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


def mostrarAsientos(dia,horario ,sala):
    asientos = cartelera[dia]
    for asiento in asientos:
        if asiento["sala"] == sala and asiento["horario"] == horario:
            print(
                f"Pelicula: {asiento['pelicula']} | Sala seleccionada: #{asiento['sala']} | En horario {asiento['horario']} | En: {asiento['formato']}."
            )

            print(f"\n========== Asientos sala: #{asiento['sala']} ==========")
            return asiento["asientos"]


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
        mostrar_asientos = mostrarAsientos(dia, horario, sala)
        mostrarMatriz(mostrar_asientos)

    elif opcion == 3:
        print("\n============ Asiento a reservar ============")

        dia, horario, sala = obtenerFuncion()


        matriz = mostrarAsientos(dia, horario, sala)
        mostrarMatriz(matriz)
        while True:
            asiento = input("Seleccione el asiento (Ej: A2): ").upper().strip()

            if len(asiento) < 2 or not asiento[0].isalpha() or not asiento[1].isdigit():
                print("Formato invalido. Ingrese una letra seguida de un numero.")
                continue

            fila = ord(asiento[0]) - 65
            columna = int(asiento[1:]) - 1

            if 0 <= fila < 5 and 0 <= columna < 6:
                break
            else:
                print("El asiento seleccionado no existe en la sala")

        if matriz[fila][columna] == ".":
            matriz[fila][columna] = "X"
            print(f"Asiento {asiento} reservado con exito.")
        else:
            print("Lo sentimos este asiento esta ocupado.")


    elif opcion == 4:
        print("\n============ Reserva a cancelar ============")

        dia, horario, sala = obtenerFuncion()

        matriz = mostrarAsientos(dia, horario, sala)
        mostrarMatriz(matriz)
        while True:
            asiento = input("Seleccione el asiento a cancelar (Ej: A2): ").upper().strip()

            if len(asiento) < 2 or not asiento[0].isalpha() or not asiento[1].isdigit():
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
            print(f"Reserva del asiento {asiento} cancelado con exito.")
        else:
            print("El asiento seleccionado ya estaba libre.")

    elif opcion == 5:
        print("============ Ver disponibilidad de asientos ============")
        dia, horario, sala = obtenerFuncion()

    elif opcion == 6:
        print("Saliendo...")
    else:
        print("Opcion invalida")
