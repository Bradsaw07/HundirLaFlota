from Tablero import *
from Barcos import *
from Variables import *
#Clase para definir todas las Funciones del HundirLaFlota
def HundirLaFlota(nombreId):
    while(True):
        try:
            print("Selecciona una dificultad")
            print("1. Easy")
            print("2. Normal")
            print("3. Hard")
            dificultad = int(input("Dificultad: "))
       
            if dificultad == 1:
                jugar_partida(nombreId,dificultad)               
                break
            elif dificultad == 2:
                jugar_partida(nombreId,dificultad)  
                break
                
            elif dificultad == 3:
                jugar_partida(nombreId,dificultad)
                break
                
            else:
                print("Elige una opcion valida")

        except ValueError:
            print("Introduce una opcion valida")            


def jugar_partida(nombreId,dificultad):
    # Inicializar variables
    tablero_jugador = []
    tablero_maquina = []
    turno_jugador = True
    barcos_jugador = []
    barcos_maquina = []
    # Seleccionar dificultad
    while True:
        try:
            if dificultad == 1:
                print("Has elegido la opcion Easy  ")
                cargarBarcos(dificultad, nombreId, barcos_jugador)
                cargarTableroMaquina(dificultad, tablero_maquina,barcos_maquina, mostrar_barcos=True)
                break
            elif dificultad == 2:
                print("Has elegido normal, buena suerte la necesitaras")
                cargarBarcos(dificultad, nombreId, barcos_jugador)
                cargarTableroMaquina(dificultad, tablero_maquina,barcos_maquina, mostrar_barcos=True)
                break
            elif dificultad == 3:
                print("Has elegido Hard, espero que estes preparado")
                cargarBarcos(dificultad, nombreId, barcos_jugador)
                cargarTableroMaquina(dificultad, tablero_maquina,barcos_maquina, mostrar_barcos=True)
                break
            else:
                print("Elige una opcion valida")

        except ValueError:
            print("Introduce una opcion valida")

    # Inicializar tableros
    for i in range(dificultad * 10):
                    tablero_jugador.append(["." for _ in range(dificultad * 10)])
                    tablero_maquina.append(["." for _ in range(dificultad * 10)])   

    # Jugar partida
    while len(barcos_jugador) > 0 and len(barcos_maquina) > 0:
        if turno_jugador == True:
            print("Turno del jugador")
            print("Tablero maquina:")
            imprimir_tablero(tablero_maquina)
            x, y = pedir_coordenadas()
            if atacar(x, y, tablero_maquina, barcos_maquina):
                print("Has acertado!")
                turno_jugador = True
            else:
                print("Has fallado!")
                turno_jugador = False
        else:
            if dificultad == 1:
                x, y = atacar_aleatorio(tablero_jugador)
            elif dificultad == 2:
                x, y = atacar_inteligente(tablero_jugador, barcos_jugador)
            elif dificultad == 3:
                for _ in range(4):
                    x, y = atacar_inteligente(tablero_jugador, barcos_jugador)
                    if not atacar(x, y, tablero_jugador, barcos_jugador):
                        break
            if atacar(x, y, tablero_jugador, barcos_jugador):
                print("La maquina ha acertado!")
                turno_jugador = False
            else:
                print("La maquina ha fallado!")
                turno_jugador = True

        # Verificar si hay ganador
        if len(barcos_jugador) < 0:
            print("La maquina ha ganado!")
            break
        elif len(barcos_maquina) < 0:
            print("El jugador ha ganado!")
            break

def pedir_coordenadas():
    while True:
        try:
            x = int(input("Introduce la coordenada del 0-9 x: "))
            y = int(input("Introduce la coordenada del 0-9 y: "))
            return x, y
        except ValueError:
            print("Introduce coordenadas validas")

def atacar(x, y, tablero_maquina, barcos_maquina):
    if tablero_maquina[x][y] == "B":
        tablero_maquina[x][y] = "X"
        for barco in barcos_maquina:
            if x in barco.fila and y in barco.columna:
                barco.impactos += 1
                if barco.impactos == len(barco.tamanio):
                    barcos_maquina.remove(barco)
                return True
        return False
    else:
        return False

def atacar_aleatorio(tablero):
    import random
    x = random.randint(0, len(tablero) - 1)
    y = random.randint(0, len(tablero) - 1)
    return x, y


def atacar_inteligente(tablero, barco_jugador):
    # Buscar barcos con menos impactos
    barcos_ordenados = sorted(barco_jugador, key=lambda barco: barco.impactos)
    barco_objetivo = barcos_ordenados[0]
    
    # Buscar coordenadas posibles del barco objetivo
    coordenadas_posibles = []
    for x in range(len(tablero)):
        for y in range(len(tablero)):
            if tablero[x][y] == ".":
                for coordenada in barco_objetivo.coordenadas:
                    if abs(coordenada[0] - x) <= 1 and abs(coordenada[1] - y) <= 1:
                        coordenadas_posibles.append((x, y))
    
    # Seleccionar una coordenada al azar entre las posibles
    if coordenadas_posibles:
        x, y = random.choice(coordenadas_posibles)
    else:
        # Si no hay coordenadas posibles, atacar de manera aleatoria
        x = random.randint(0, len(tablero) - 1)
        y = random.randint(0, len(tablero) - 1)
    
    return x, y

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))




