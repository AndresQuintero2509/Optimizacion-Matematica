#Importando librerias
import math
import random

def aleatorio(funcion, Xi, Xs, Yi, Ys):
    maxf = -1E9
    funcs = vars(math)
    #Numero aleatorio
    for n in range(10000):
        r = random.random()
        #Hallando X
        x = Xi + (Xs - Xi) * r
        y = Yi + (Ys - Yi) * r
        #Cambio de los valores en la funcion        
        fx = funcion
        librex = {"x":x , "y":y}
        fx = eval(fx, funcs ,librex)
        if fx > maxf:
            maxf = fx
            maxx = x
            maxy = y
    print(funcion , " = " , maxf)
    print("El máximo se encuentra en [ " , maxx ," , " , maxy ," ]")    

#Ingreso variables
print("Ingrese la función a evaluar: ")
print("(Utilice solo x & y en minuscula como variables)")
#$funcion contiene la función a la cual se le realizará la búsqueda
funcion = input()
print("Ingrese el intervalo menor para x:")
#$Xi contiene el intervalo menor
Xi = float(input())
print("Ingrese el intervalo mayor para x:")
#$Xs contiene el intervalo superior
Xs = float(input())
print("Ingrese el intervalo menor para y:")
#$Yi contiene el intervalo menor
Yi = float(input())
print("Ingrese el intervalo mayor para y:")
#$Ys contiene el intervalo superior
Ys = float(input())
print("Los valores insertados son: ")
print("Función: " , funcion , ", Intervalos :[" , Xi , "," , Xs ,"], [" , Yi , "," , Ys ,"]")
aleatorio(funcion, Xi, Xs, Yi, Ys)