
class Barco:
    def __init__(self,nombre,tamanio):
        self.nombre = nombre
        self.tamanio = tamanio
        self.vida = tamanio
    
    def golpeado(self):
        self.vida = -1
    
    def estaHundido(self):
        return self.vida <=0
    

    