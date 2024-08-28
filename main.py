from Sources.peticiones import Peticiones
from Sources.compuertas import Compuertas
from Sources.formulas import Formulas
#quitar libreria, solo se usa para impresion de dato
import json
#variables globales
index = 0
epoca = 0
dict_total = {}
#creacion de objetos 
obj_peticiones = Peticiones()
obj_compuerta= Compuertas(n=1)
obj_formulas = Formulas(w=0)
# Declacarion de constantes
alfa = 0.5
en = [1,2,3,4] 
#::-1
#sumatoria 
list_weigth = obj_peticiones.weigths()
list_compuerta = obj_compuerta.comp()
obj_formulas.list_w = list_weigth[::-1]
#print("La lista w es: {} \n {}".format(list_weigth[::-1],list_weigth))
# por medio del uso de list comprehension recorre la matriz ubicando el indice de la fula en n-1 es decir
#en el ultimo indice
Y0p = [row[-1] for row in list_compuerta]
while index < 3: # se llama ala funcion de sumatoria para sacar al suma ponderada  neta
    sumatoria =obj_formulas.sum_net(list_index_logical=list_compuerta[index][::-1])
    #print("la sumatoria es {}".format(sumatoria))
    #añadimos el procesos al diccionario global, para tener un registro de lo hecho
    if f'Patron({index+1})-T+{index}' not in dict_total:
        dict_total[f'Patron({index+1})-T+{epoca}'] = {'NET' : sumatoria}
    else:
        dict_total[f'Patron({index+1})-T+{epoca}'] = {'NET' : sumatoria}
    # se hace la validacion de la sumatoria, por si sumatoria es mayo o igual a 0
    if sumatoria > 0:
        sumatoria = 1
    else:
        sumatoria = 0
    dict_total[f'Patron({index+1})-T+{epoca}'][f'YDp{index+1}'] = sumatoria
    
    index += 1

    

print(json.dumps(dict_total,indent=2))
#funciones simples

