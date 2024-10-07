

class Tablero:
    def __init__(self, filas,columnas):
        self.filas = filas
        self.columnas = columnas
        self.casillas =  [[None for _ in range(columnas)] for _ in range(filas)]

def TableroPorDificultades(dificultad):
        if dificultad ==  1:
            DimensTabE = Tablero(10, 10)
            tableroE = [['.'] * DimensTabE.columnas for _ in range(DimensTabE.filas)]
            # Imprimir el encabezado
            encabezado_columnas = '   ' + ' '.join(str(i + 1) for i in range(DimensTabE.columnas))
            print(encabezado_columnas)
            # Imprimir el tablero con letras de filas
            for i, fila in enumerate(tableroE):
                print(chr(65 + i), ' '.join(fila))  # Convertir índice a letra (A=65, B=66, ...)

        elif dificultad == 2:
            DimensaTabN = Tablero(12,12)
            tableroN = [['.'] * DimensaTabN.columnas for _ in range(DimensaTabN.filas)]
            # Imprimir el encabezado
            encabezado_columnas = '   ' + ' '.join(str(i + 1) for i in range(DimensaTabN.columnas))
            print(encabezado_columnas)
            # Imprimir el tablero con letras de filas
            for i, fila in enumerate(tableroN):
                print(chr(65 + i), ' '.join(fila))  # Convertir índice a letra (A=65, B=66, ...)
            
        elif dificultad == 3:
            DimensaTabH = Tablero(20,20)
            tableroH = [['.'] * DimensaTabH.columnas for _ in range(DimensaTabH.filas)]
            # Imprimir el encabezado
            encabezado_columnas = '   ' + ' '.join(str(i + 1) for i in range(DimensaTabH.columnas))
            print(encabezado_columnas)
            # Imprimir el tablero con letras de filas
            for i, fila in enumerate(tableroH):
                print(chr(65 + i), ' '.join(fila))  # Convertir índice a letra (A=65, B=66, ...)
        else:
            print(f"La dificultad elegida no es valida {dificultad}")



        