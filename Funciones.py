from Tablero import *
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
                print("Has elegido la opcion Easy  ")
                
                TableroPorDificultades(dificultad) 
                break
            elif dificultad == 2:
                print("Has elegido normal, buena suerte la necesitaras")
                TableroPorDificultades(dificultad)
                
                break
                
            elif dificultad == 3:
                print("Has elegido Hard, espero que estes preparado")
                TableroPorDificultades(dificultad)
                
                break
                
            else:
                print("Elige una opcion valida")

        except ValueError:
            print("Introduce una opcion valida")            
