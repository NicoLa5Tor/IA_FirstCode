from Sources.peticiones import Peticiones
from Sources.compuertas import Compuertas
from Sources.formulas import Formulas
from Sources.operations_system import System_op
#Esta libreria se usa para obtener el tiempo de ejecucion del aprendizaje
import time
#variables globales
index = 0
epoca = 0
dict_total = {}
#creacion de objetos 
obj_peticiones = Peticiones()
obj_system = System_op()
#aqui si se envia un n = a un rango de 1 a 4, se asigna un compurta logica
#1.or
#2.and
#3.Nan
#4.Exor
obj_compuerta= Compuertas()
obj_formulas = Formulas()
##sumatoria 
list_weigth = obj_peticiones.weigths()
list_compuerta = obj_compuerta.comp()
#reasignacion de variables de contructores
#se hace una funcion para poder llamr de nuevo el reasignamiento de variables
def asign_new_val_constructor():
    obj_formulas.logical = obj_peticiones.list = list_compuerta
    obj_formulas.list_w = list_weigth
asign_new_val_constructor()
#Usamos la funcion last_column del objeto peticiones, para que me traiga la ultima
#columna d ela matriz, es decir para que traiga los Y deseados
Y0p = obj_peticiones.last_column()
#iniciamos el contador 
start_time = time.time()
while index < 4:#se recorre la matriz de las compuertas desde el primer patron hasta el ultimo
     # se llama ala funcion de sumatoria para sacar al suma ponderada  neta
    sumatoria =obj_formulas.sum_net(index=index)
    #print("la sumatoria es {}".format(sumatoria))
    #añadimos el procesos al diccionario global, para tener un registro de lo hecho
    if f'Epoca {epoca+1}' not in dict_total:
        dict_total[f'Epoca {epoca+1}'] = {}
    if f'Patron({index+1})-T+{index}' not in dict_total[f'Epoca {epoca+1}']:
        dict_total[f'Epoca {epoca+1}'][f'Patron({index+1})-T+{epoca}'] = {'NET' : sumatoria}
    else:
        dict_total[f'Epoca {epoca+1}'][f'Patron({index+1})-T+{epoca}'] = {'NET' : sumatoria}
    # se hace la validacion de la sumatoria, por si sumatoria es mayo o igual a 0, para asignar el YDp
    if sumatoria > 0:
        sumatoria = 1
    else:
        sumatoria = 0
    #agregamos los pesos al diccionario, pero validando que el index no se pase de los 3 pesos existentes
    if index < 3:
         dict_total[f'Epoca {epoca+1}'][f'Patron({index+1})-T+{epoca}'][f'W1{index}'] = list_weigth[index]
    #asignamos las variables al diccionario
    dict_total[f'Epoca {epoca+1}'][f'Patron({index+1})-T+{epoca}']['YD'] = list_compuerta[index][-1]
    dict_total[f'Epoca {epoca+1}'][f'Patron({index+1})-T+{epoca}'][f'x{index}'] = list_compuerta[index][-4+index]
    #asignamos el YDp al diccionario
    dict_total[f'Epoca {epoca+1}'][f'Patron({index+1})-T+{epoca}'][f'Y0p{index+1}'] = sumatoria
    #asignamos el valor del error al diccionario
    e = obj_formulas.actual_error(ob=sumatoria,esp=Y0p[index])
   # print(f"El peso es: {list_weigth}")
    print(f"El error del index {index} de la epoca {epoca} es: {e}")
    dict_total[f'Epoca {epoca+1}'][f'Patron({index+1})-T+{epoca}'][f'Ep{index+1}'] = e
    index += 1
    #validamos si hay que seguir el ciclo o reasignar pesos, (se revisa el error dado del patron actual)
    if e != 0:
        #primero se cartiga la neurona
        print(list_weigth)
        list_weigth = obj_formulas.reasing_weigth(err_actual=e,list_x=list_compuerta[index-1][::-1])
        asign_new_val_constructor()
        print(obj_formulas.list_w)
        #time.sleep(1)
        #se le dice a la red que comience de nuevo
        index = 0
        #se suma la cantidad de epocas
        epoca += 1
        
#funciones simples
#esta funcion solo retorna el tipo de compuerta que se esta usando, solo para ponerles titulo a 
#el archivo txt
def return_option_logicar():
    op = obj_compuerta 
    logical = ""
    if op == 1:
        logical = "Compuerta OR"
    elif op == 2:
        logical = "Compuerta AND"
    elif op == 3:
        logical = "Compuerta NAN"
    elif op == 4:
        logical = "Compuerta XOR"
    return logical
#apartado main o ejecución
 
#esta validacion se hace para evitar errores keytipe al agragar una nueva llave al diccionario dict
#y luego se agrega la llave (Pesos ideales) que señala los pesos que se debe usar
if 'Pesos ideales' not in dict_total:
    dict_total["Pesos ideales: "] = {'w10' : list_weigth[0], 'w11': list_weigth[1],'w12':list_weigth[2]}
obj_system.create_and_write_document_json(dictionary=dict_total)
#traemos la compuerta usada
compuerta = return_option_logicar()
#finalizamos el contador
end_time = time.time()
#creamos el archivo txt llamando el objeto System_op
print(compuerta)
txt = f"""
{compuerta} \n
La operación de aprendizaje tubo un total de {epoca} epocas.\n
El aprendizaje demoró aproximadamente {end_time}

"""
obj_system.create_txt(txtt=txt)


    