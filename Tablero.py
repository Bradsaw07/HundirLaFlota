import random
from Barcos import *

class Tablero:
    def __init__(self, filas,columnas):
        self.filas = filas
        self.columnas = columnas
        self.casillas =  [[None for _ in range(columnas)] for _ in range(filas)]

def cargarBarcos(dificultad, nombreId,barco_jugador):
    
    if dificultad == 1:
        tablero = Tablero(10, 10)
        tamaño_barcos = 3
    elif dificultad == 2:
        tablero = Tablero(20, 20)
        tamaño_barcos = 4
    elif dificultad == 3:
        tablero = Tablero(30, 30)
        tamaño_barcos = 5
    else:
        print(f"La dificultad elegida no es válida {dificultad}")
        return None


    for _ in range(5):  # Cargar 5 barcos
        orientacion = random.randint(0, 1)  # 0 = horizontal, 1 = vertical
        if orientacion == 0:  # Horizontal
            fila = random.randint(0, tablero.filas - 1)
            columna = random.randint(0, tablero.columnas - tamaño_barcos)
        else:  # Vertical
            fila = random.randint(0, tablero.filas - tamaño_barcos)
            columna = random.randint(0, tablero.columnas - 1)

        barco = Barco(tamaño_barcos, orientacion, fila, columna)
        barco_jugador.append(barco)

        for i in range(tamaño_barcos):
            if orientacion == 0:  # Horizontal
                tablero.casillas[fila][columna + i] = barco
            else:  # Vertical
                tablero.casillas[fila + i][columna] = barco

    # Visualizar el tablero con los encabezados y el nombre del jugador
    print(f"Tablero de {nombreId}:")
    encabezado_columnas = '   ' + ' '.join(str(i + 1) for i in range(tablero.columnas))
    print(encabezado_columnas)
    for i, fila in enumerate(tablero.casillas):
        print(chr(65 + i), ' '.join(['B' if casilla else '.' for casilla in fila]))

    return tablero, barco_jugador

def cargarTableroMaquina(dificultad,tablero_maquina,barcos_maquina, mostrar_barcos):
    if dificultad == 1:
        tablero_maquina = Tablero(10, 10)
        tamaño_barcos = 3
    elif dificultad == 2:
        tablero_maquina = Tablero(20, 20)
        tamaño_barcos = 4
    elif dificultad == 3:
        tablero_maquina = Tablero(30, 30)
        tamaño_barcos = 5
    else:
        print(f"La dificultad elegida no es válida {dificultad}")
        return None

    for _ in range(5):  # Cargar 5 barcos
        orientacion = random.randint(0, 1)  # 0 = horizontal, 1 = vertical
        if orientacion == 0:  # Horizontal
            fila = random.randint(0, tablero_maquina.filas - 1)
            columna = random.randint(0, tablero_maquina.columnas - tamaño_barcos)
        else:  # Vertical
            fila = random.randint(0, tablero_maquina.filas - tamaño_barcos)
            columna = random.randint(0, tablero_maquina.columnas - 1)

        barco = Barco(tamaño_barcos, orientacion, fila, columna)
        barcos_maquina.append(barco)

        for i in range(tamaño_barcos):
            if orientacion == 0:  # Horizontal
                tablero_maquina.casillas[fila][columna + i] = barco
            else:  # Vertical
                tablero_maquina.casillas[fila + i][columna] = barco

    # Visualizar el tablero con los encabezados y el nombre del jugador
    print(f"Tablero de la máquina:")
    encabezado_columnas = '   ' + ' '.join(str(i + 1) for i in range(tablero_maquina.columnas))
    print(encabezado_columnas)
    for i, fila in enumerate(tablero_maquina.casillas):
        if mostrar_barcos:
            print(chr(65 + i), ' '.join(['B' if casilla else '.' for casilla in fila]))
        else:
            print(chr(65 + i), ' '.join(['.' for _ in fila]))  # Mostrar solo puntos para esconder los barcos

    return tablero_maquina, barcos_maquina
  


