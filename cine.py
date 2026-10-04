import json

cartelera = {
    "Lunes": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 1, "horario": "2:00 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 2, "horario": "4:30 pm", "formato": "3D"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 3, "horario": "6:00 pm", "formato": "4DX"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 4, "horario": "5:30 pm", "formato": "Normal"},
        {"pelicula": "El Final", "sala": 5, "horario": "8:00 pm", "formato": "CXC"},
    ],
    "Martes": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 3, "horario": "5:00 pm", "formato": "4DX"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 1, "horario": "7:00 pm", "formato": "Normal"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 2, "horario": "3:00 pm", "formato": "Normal"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 5, "horario": "6:30 pm", "formato": "3D"},
        {"pelicula": "El Final", "sala": 4, "horario": "9:00 pm", "formato": "Normal"},
    ],
    "Miércoles": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 4, "horario": "4:00 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 5, "horario": "2:30 pm", "formato": "CXC"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 1, "horario": "7:30 pm", "formato": "3D"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 2, "horario": "5:00 pm", "formato": "Normal"},
        {"pelicula": "El Final", "sala": 3, "horario": "8:30 pm", "formato": "4DX"},
    ],
    "Jueves": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 2, "horario": "6:30 pm", "formato": "3D"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 3, "horario": "3:30 pm", "formato": "Normal"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 4, "horario": "8:00 pm", "formato": "Normal"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 1, "horario": "2:00 pm", "formato": "4DX"},
        {"pelicula": "El Final", "sala": 5, "horario": "5:30 pm", "formato": "CXC"},
    ],
    "Viernes": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 5, "horario": "4:00 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 4, "horario": "7:00 pm", "formato": "3D"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 1, "horario": "5:30 pm", "formato": "CXC"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 3, "horario": "9:00 pm", "formato": "Normal"},
        {"pelicula": "El Final", "sala": 2, "horario": "2:30 pm", "formato": "4DX"},
    ],
    "Sábado": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 1, "horario": "3:00 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 2, "horario": "6:00 pm", "formato": "4DX"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 5, "horario": "8:30 pm", "formato": "3D"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 4, "horario": "4:30 pm", "formato": "Normal"},
        {"pelicula": "El Final", "sala": 3, "horario": "7:30 pm", "formato": "CXC"},
    ],
    "Domingo": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 3, "horario": "2:30 pm", "formato": "3D"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 5, "horario": "5:00 pm", "formato": "Normal"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 2, "horario": "7:00 pm", "formato": "CXC"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 1, "horario": "8:30 pm", "formato": "4DX"},
        {"pelicula": "El Final", "sala": 4, "horario": "4:00 pm", "formato": "Normal"},
    ],
}

def verCartelera(dia):
    funciones = cartelera[dia]
    print(f"\n================================================ {dia} ================================================")
    for funcion in funciones:
            print( f"Pelicula: {funcion['pelicula']} | Sala: {funcion['sala']} | {funcion['horario']} | {funcion['formato']}")

def mostrarAsientos(dia, sala, horario):
    asientos = cartelera[dia]
    for asiento in asientos:
        if asiento["sala"] == sala and asiento["horario"] == horario:
            print(f"Pelicula: {asiento['pelicula']} | Sala seleccionada: #{asiento['sala']} | En horario {asiento['horario']} | En: {asiento['formato']}.")

            print(f"\n========== Asientos sala: #{asiento['sala']} ==========")
            matriz  = []
            for a in range(5):
                fila = ['  .'] * 6
                matriz.append(fila)
            return matriz

def mostrarMatriz(matriz_a_mostrar):
    listaNums = []

    for c in range(1,7):
        columnas = str(c)
        listaNums.append(columnas)
    resultado = "   ".join(listaNums)
    print(f"     {resultado}")

    for indice, fila in enumerate(matriz_a_mostrar):
        letraFila = chr(indice + 65)
        filaVisual = " ".join(fila)

        print(f"{letraFila}: {filaVisual}")



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

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        dia = input("Seleccion una opcion (Lunes-Domingo): ").capitalize().strip()
        verCartelera(dia)

    elif opcion == 2:
        dia = input("Seleccione el dia a mostrar (Lunes-Domingo): ").capitalize().strip()
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



        mostrar_asientos = mostrarAsientos(dia,sala, horario)
        mostrarMatriz(mostrar_asientos)

    elif opcion == 6:
        print("Saliendo...")
    else:
        print("Opcion invalida")
