
#Creado por Jesus Andres Sanchez Quintero
#https://share.cocalc.com/share/4bfb9fc2-c03f-4f81-b8f3-c809763900a5/Busqueda%20Fibonacci.ipynb?viewer=share

import math

#Método para la búsqueda de fibonacci
def fibonacci(funcion, Xi, Xs, e):
    Fn = (Xs-Xi)/e
    i = 2
    #Lista que contendrá la serie Fibonacci
    fibonacci = [1,1,2]
    #Llenado de lista Fibonacci
    while Fn > fibonacci[i]:
        fibonacci.append(fibonacci[i]+fibonacci[i-1])
        i = i + 1
    print("Serie de Fibonacci:",fibonacci)
    e = (Xs - Xi) / fibonacci[i]
    for i in range(i,1,-1):        
        ePrima = (fibonacci[i-1] * e)
        #Intervalos 
        x1 = Xi + ePrima
        x2 = Xs - ePrima
        #Calculando funciones 
        fx1 = fx2 = funcion
        #Cambia los valores de la X de la funcion por X1 y X2 
        librex1 = {"x":x1}
        librex2 = {"x":x2}
        funcs = vars(math)
        #Evaluacion de las funciones respecto X1 y X2
        fx1 = eval(fx1, funcs ,librex1)
        fx2 = eval(fx2, funcs ,librex2)
        print(Xi , "__" , x2 , "__" , x1 , "__" , Xs)
        if fx2 > fx1:
            Xs = x1
        else:
            Xi = x2
        i = i - 1
        fibonacci.remove(fibonacci[i])
    print("El máximo de la función: " , funcion , "es: " , ((x1+x2)/2))    

#Ingreso variables
print("Ingrese la función a evaluar: ")
print("(Utilice solo x en minuscula como variable)")
#$funcion contiene la función a la cual se le realizará la búsqueda
funcion = input()
print("Ingrese el intervalo menor:")
#$Xi contiene el intervalo menor
Xi = float(input())
print("Ingrese el intervalo mayor:")
#$Xs contiene el intervalo superior
Xs = float(input())
print("Ingrese el margen de error aceptado: ")
#$e contiene el margen de error
e = float(input())
print("Los valores insertados son: ")
print("Función: " , funcion , ", Intervalos :[" , Xi , "," , Xs ,"], Error = " ,e)
fibonacci(funcion, Xi, Xs , e)