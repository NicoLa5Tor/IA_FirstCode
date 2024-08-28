import numpy as np
#Esta libreria es única y exclusivamente para generar numeros aleatoreos
class Peticiones:
    def __init__(self) -> None:
        pass
    # la funcion weigths lo que haces es generar tres numeros en un rango de entre 0 y 1
    # esto sin incluir los numeros de partida (0,1)
    def weigths (self):
        return np.random.rand(3) * 1 - 0
    
