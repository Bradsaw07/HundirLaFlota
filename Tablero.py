import random
import string
import tkinter as tk
from Barcos import *

class Tablero:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.casillas = [["." for _ in range(columnas)] for _ in range(filas)]
        self.coordenadas_atacadas = []
    
    def generar_tableros(self, dificultad):
        if dificultad == 1:
            tablero_jugador = Tablero(10, 10)
            tablero_rival = Tablero(10, 10)
        elif dificultad == 2:
            tablero_jugador = Tablero(15, 15)
            tablero_rival = Tablero(15, 15)
        elif dificultad == 3:
            tablero_jugador = Tablero(20, 20)
            tablero_rival = Tablero(20, 20)

        return tablero_jugador, tablero_rival

    def cargar_barcos(self, barcos, mostrar_barcos=False):
        for barco in barcos:
            for fila, columna in barco.posiciones:
                if mostrar_barcos:
                    self.casillas[fila][columna] = "B"
                else:
                    self.casillas[fila][columna] = "."

    def atacar(self, fila, columna, barcos_rival, mostrar_barcos=False):
        if fila < 0 or fila >= self.filas or columna < 0 or columna >= self.columnas:
            print("Coordenada fuera del tablero")
            return False
        if (fila, columna) in self.coordenadas_atacadas:
            print("Coordenada ya atacada")
            return False
        self.coordenadas_atacadas.append((fila, columna))
        for barco in barcos_rival:
            if (fila, columna) in barco.posiciones:
                self.casillas[fila][columna] = "X"
                if mostrar_barcos:
                    print("¡Barco hundido!")
                if all((fila, columna) in self.coordenadas_atacadas for fila, columna in barco.posiciones):
                    print("¡Barco completamente hundido!")
                    barcos_rival.remove(barco)
                return True
        self.casillas[fila][columna] = "."
        print("¡Disparo fallido!")
        return False
    
    def atacar_normal(self, fila, columna, barcos_rival, mostrar_barcos=False):
        if fila < 0 or fila >= self.filas or columna < 0 or columna >= self.columnas:
            print("Coordenada fuera del tablero")
            return False
        if (fila, columna) in self.coordenadas_atacadas:
            print("Coordenada ya atacada")
            return False
        self.coordenadas_atacadas.append((fila, columna))
        for barco in barcos_rival:
            if (fila, columna) in barco.posiciones:
                self.casillas[fila][columna] = "X"
                if mostrar_barcos:
                    print("¡Barco hundido!")
                if all((fila, columna) in self.coordenadas_atacadas for fila, columna in barco.posiciones):
                    print("¡Barco completamente hundido!")
                    barcos_rival.remove(barco)
                return True
        self.casillas[fila][columna] = "A"
        print("¡Disparo fallido!")
        return False

    def atacar_dificil(self, fila, columna, barcos_rival, mostrar_barcos=False):
        if fila < 0 or fila >= self.filas or columna < 0 or columna >= self.columnas:
            print("Coordenada fuera del tablero")
            return False
        if (fila, columna) in self.coordenadas_atacadas:
            print("Coordenada ya atacada")
            return False
        self.coordenadas_atacadas.append((fila, columna))
        for barco in barcos_rival:
            if (fila, columna) in barco.posiciones:
                self.casillas[fila][columna] = "X"
                if mostrar_barcos:
                    print("¡Barco hundido!")
                if all((fila, columna) in self.coordenadas_atacadas for fila, columna in barco.posiciones):
                    print("¡Barco completamente hundido!")
                    barcos_rival.remove(barco)
                return True
        self.casillas[fila][columna] = "A"
        print("¡Disparo fallido!")
        return False

    def imprimir_tablero(self):
        print("  ", end="")
        for i in range(self.columnas):
            print(i, end=" ")
        print()
        for i, fila in enumerate(self.casillas):
            print(i, end=" ")
            for casilla in fila:
                print(casilla, end=" ")
            print()

    def imprimir_tablero_con_letras(self):
        print("  ", end="")
        for i in range(self.columnas):
            print(string.ascii_uppercase[i], end=" ")
        print()
        for i, fila in enumerate(self.casillas):
            print(i, end=" ")
            for casilla in fila:
                print(casilla, end=" ")
            print() 
def mostrar_ventana_ganador_easy():
        ventana = tk.Tk()
        ventana.title("Felicidadees,¡Has ganadoooo!")
        imagen_ganador = tk.PhotoImage(file="HundirLaFlota\Imagenes\Winner.png")
        label_imagen = tk.Label(ventana,image=imagen_ganador)
        label_imagen.pack()
        ventana.mainloop()
        
def mostrar_ventana_perdedor_easy():
        ventana = tk.Tk()
        ventana.title("¡Has perdido!")
        imagen_perdedor = tk.PhotoImage(file="HundirLaFlota\Imagenes\Loser.png")
        label_imagen = tk.Label(ventana, image=imagen_perdedor)
        label_imagen.pack()
        ventana.mainloop()

def mostrar_ventana_ganador_normal():
        ventana = tk.Tk()
        ventana.title("Enhorabuenaaa ¡Has ganadoooo!")
        imagen_ganador = tk.PhotoImage(file="HundirLaFlota\Imagenes\WinNormal.png")
        label_imagen = tk.Label(ventana,image=imagen_ganador)
        label_imagen.pack()
        ventana.mainloop()

def mostrar_ventana_perdedor_normal():
        ventana = tk.Tk()
        ventana.title("¡Has perdido!")
        imagen_perdedor = tk.PhotoImage(file="HundirLaFlota\Imagenes\Losser.png")
        label_imagen = tk.Label(ventana, image=imagen_perdedor)
        label_imagen.pack()
        ventana.mainloop()  

def mostrar_ventana_ganador_dificil():
        ventana = tk.Tk()
        ventana.title("Enhorabuenaaa ¡Has conseguidoo ganarrr!")
        imagen_ganador = tk.PhotoImage(file="HundirLaFlota\Imagenes\YouWin.jpeg")
        label_imagen = tk.Label(ventana,image=imagen_ganador)
        label_imagen.pack()
        ventana.mainloop()

def mostrar_ventana_perdedor_dificil():
        ventana = tk.Tk()
        ventana.title("¡Has perdido!")
        imagen_perdedor = tk.PhotoImage(file="HundirLaFlota\Imagenes\GameOver.png")
        label_imagen = tk.Label(ventana, image=imagen_perdedor)
        label_imagen.pack()
        ventana.mainloop()


def jugar(dificultad,nombreId):
        tablero_jugador, tablero_rival = Tablero(0, 0).generar_tableros(dificultad)
        barcos_jugador = Barco.crear_barcos(6, 3, "horizontal", tablero_jugador.filas, tablero_jugador.columnas)
        barcos_rival = Barco.crear_barcos(6, 3, "horizontal", tablero_rival.filas, tablero_rival.columnas)
        tablero_jugador.cargar_barcos(barcos_jugador)
        tablero_rival.cargar_barcos(barcos_rival, mostrar_barcos=True)
        while True:
            print(f"Tablero del jugador: {nombreId}")
            tablero_jugador.imprimir_tablero_con_letras()
            print("Tablero del rival:")
            tablero_rival.imprimir_tablero_con_letras()
            while True:
                fila = int(input("Ingrese la fila: "))
                columna = int(input("Ingrese la columna: "))
                if tablero_rival.atacar(fila, columna, barcos_rival):
                    print("¡Disparo acertado!")
                    if not barcos_rival:
                        print("¡Has ganado!")
                        mostrar_ventana_ganador_easy()
                        return
                else:
                    print("¡Disparo fallido!")
                    break
            # Turno de la máquina
            while True:
                fila_maquina = random.randint(0, tablero_jugador.filas - 1)
                columna_maquina = random.randint(0, tablero_jugador.columnas - 1)
                if tablero_jugador.atacar(fila_maquina, columna_maquina, barcos_jugador):
                    print("¡La máquina ha acertado!")
                    if not barcos_jugador:
                        print("¡Has perdido!")
                        mostrar_ventana_perdedor_easy()
                        return
                else:
                    print("¡La máquina ha fallado!")
                    break

def jugar_normal(dificultad, nombreId):
        tablero_jugador, tablero_rival = Tablero(0, 0).generar_tableros(dificultad)
        barcos_jugador = Barco.crear_barcos(5, 3, "horizontal", tablero_jugador.filas, tablero_jugador.columnas)
        barcos_rival = Barco.crear_barcos(5, 3, "horizontal", tablero_rival.filas, tablero_rival.columnas)
        tablero_jugador.cargar_barcos(barcos_jugador)
        tablero_rival.cargar_barcos(barcos_rival, mostrar_barcos=True)
        while True:
            print(f"Tablero del jugador: {nombreId}")
            tablero_jugador.imprimir_tablero_con_letras()
            print("Tablero del rival:")
            tablero_rival.imprimir_tablero_con_letras()
            while True:
                fila = int(input("Ingrese la fila: "))
                columna = int(input("Ingrese la columna: "))
                if tablero_rival.atacar_normal(fila, columna, barcos_rival):
                    print("¡Disparo acertado!")
                    if not barcos_rival:
                        print("¡Has ganado!")
                        mostrar_ventana_ganador_normal()
                        return
                else:
                    print("¡Disparo fallido!")

                    break
            # Turno de la máquina
            while True:
                fila_maquina = random.randint(0, tablero_jugador.filas - 1)
                columna_maquina = random.randint(0, tablero_jugador.columnas - 1)
                if tablero_jugador.atacar_normal(fila_maquina, columna_maquina, barcos_jugador):
                    print("¡La máquina ha acertado!")
                else:
                    print("¡La máquina ha fallado!")
                # Segundo ataque
                fila_maquina_segundo = None
                columna_maquina_segundo = None
                if fila_maquina - 1 >= 0:
                    fila_maquina_segundo = fila_maquina - 1
                else:
                    fila_maquina_segundo = fila_maquina + 1
                columna_maquina_segundo = columna_maquina
                if (fila_maquina_segundo, columna_maquina_segundo) not in tablero_jugador.coordenadas_atacadas:
                    if tablero_jugador.atacar_normal(fila_maquina_segundo, columna_maquina_segundo, barcos_jugador):
                        print("¡La máquina ha acertado de nuevo!")
                        if not barcos_jugador:
                            print("¡Has perdido!")
                            mostrar_ventana_perdedor_normal()
                            return
                    else:
                        print("¡La máquina ha fallado de nuevo!")
                        break
                else:
                    print("¡La máquina ha repetido coordenadas!")
                    break

                    


def jugar_dificil(dificultad, nombreId):
        tablero_jugador, tablero_rival = Tablero(0, 0).generar_tableros(dificultad)
        barcos_jugador = Barco.crear_barcos(5, 3, "horizontal", tablero_jugador.filas, tablero_jugador.columnas)
        barcos_rival = Barco.crear_barcos(5, 3, "horizontal", tablero_rival.filas, tablero_rival.columnas)
        tablero_jugador.cargar_barcos(barcos_jugador)
        tablero_rival.cargar_barcos(barcos_rival, mostrar_barcos=True)
        while True:
            print(f"Tablero del jugador: {nombreId}")
            tablero_jugador.imprimir_tablero_con_letras()
            print("Tablero del rival:")
            tablero_rival.imprimir_tablero_con_letras()
            while True:
                fila = int(input("Ingrese la fila: "))
                columna = int(input("Ingrese la columna: "))
                if tablero_rival.atacar_dificil(fila, columna, barcos_rival):
                    print("¡Disparo acertado!")
                    if not barcos_rival:
                        print("¡Has ganado!")
                        mostrar_ventana_ganador_dificil()
                        
                        return
                else:
                    print("¡Disparo fallido!")
                    break
            # Turno de la máquina
            while True:
                fila_maquina = random.randint(0, tablero_jugador.filas - 1)
                columna_maquina = random.randint(0, tablero_jugador.columnas - 1)
                if (fila_maquina, columna_maquina) not in tablero_jugador.coordenadas_atacadas:
                    break
            if tablero_jugador.atacar_dificil(fila_maquina, columna_maquina, barcos_jugador):
                print("¡La máquina ha acertado!")
                # Disparos inteligentes
                fila_maquina_base = fila_maquina
                columna_maquina_base = columna_maquina
                for _ in range(3):
                    direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    random.shuffle(direcciones)
                    for direccion in direcciones:
                        fila_maquina_nueva = fila_maquina_base + direccion[0]
                        columna_maquina_nueva = columna_maquina_base + direccion[1]
                        if (fila_maquina_nueva, columna_maquina_nueva) not in tablero_jugador.coordenadas_atacadas and 0 <= fila_maquina_nueva < tablero_jugador.filas and 0 <= columna_maquina_nueva < tablero_jugador.columnas:
                            if tablero_jugador.atacar_dificil(fila_maquina_nueva, columna_maquina_nueva, barcos_jugador):
                                print("¡La máquina ha acertado de nuevo!")
                                fila_maquina_base = fila_maquina_nueva
                                columna_maquina_base = columna_maquina_nueva
                                break
                            if not barcos_jugador:
                                print("¡Has perdido!")
                                mostrar_ventana_perdedor_dificil()
                                return
                            else:
                                print("¡La máquina ha fallado de nuevo!")
                                break
            else:
                print("¡La máquina ha fallado!")