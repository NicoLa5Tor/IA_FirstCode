import random
#Esta libreria es única y exclusivamente para generar numeros aleatoreos
class Peticiones:
    def __init__(self,list = []) :
        self.list =  list
        pass
    # la funcion weigths lo que haces es generar tres numeros en un rango de entre 0 y 1
    # esto sin incluir los numeros de partida (0,1)
    def weigths (self):
        return [round(random.uniform(a=-1,b=1),2) for _ in range(3)]
# por medio del uso de list comprehension recorre la matriz ubicando el indice de la fula en n-1 es decir
#en el ultimo indice
    def last_column(self):
        return [x[-1] for x in self.list]
    