# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:04:51 
@author: Brandon Núñez 
Se pretende implementar un método de integración numérica sobre un automóbil 
con condiciones iniciales dadas, con la regla de simpson
"""
import numpy as np
import scipy as sp

def Crear_Matriz_de_Pesos(N,h):
    
    '''
    Esta función crea una matriz de pesos para integración numérica basado en 
    el método de simpson.

    Parameters
    ----------
    N : Es la cantidad de puntos que debe tener la matriz
        
    h : Es el espaciamiento entre puntos

    Returns
    -------
    w : Es vector con N pesos correspondientes a la regla de simpson

    '''
    
    w=np.zeros(N)

    for i in range(N):
        valor_local_peso=0
        
        if i==0 or i==N-1:
            valor_local_peso=h/3
        elif i%2!=0:
            valor_local_peso=4*h/3
        else:
            valor_local_peso=2*h/3
            
        w[i]=valor_local_peso
    return w

def Generar_Valores_de_X(N,h):
    '''
    Genera un vector con valores de x igualmente espaciados

    Parameters
    ----------
    N : Es la cantidad de puntos en x que se desea obtener
    h : Espaciamiento entre cada par de puntos

    Returns
    -------
    X : Es un vector con N valores de x igualmente espaciados una distancia h
    '''
    X=np.zeros(N)

    for i in range(N):
        X[i]=a+(i)*h
    return X

def Integrar(V,N,a,b):
    '''
    Integra una función V, numéricamente con la regla de simpson en un 
    intervalo de a a b con N puntos igualmente espaciado

    Parameters
    ----------
    V : Función a integrar
    N : Cantidad de puntos para la integración numérica
    a : Inicio del intérvalo a integrar
    b : Fin del intervalo a integrar

    Returns
    -------
    I : Valor numérico de la integral solicitada

    '''

    h=(b-a)/(N-1)
    
    w=Crear_Matriz_de_Pesos(N,h)
    X=Generar_Valores_de_X(N, h)

    I=0
    for i in range(N):
        I=I+V(X[i])*w[i]
    
    return I

#definición de condiciones iniciales. con N impar
N=3             
a=0
b=100

#definimos la función de velocidad
def V(t):
    v=0.5+0.005*t
    return v

'''
Código de la parte b)
    
'''
I=Integrar(V,N,a,b)    
print('El dezplamiento del automóvil de {0} a {1} es de {2}'.format(a,b,I))



'''
Código de la parte c)
    
'''
Matriz_de_resultados=np.zeros([5,3])
N=[3,5,15,101,1001]
Valor_referencia=75
for i in range(5):
    I=Integrar(V,N[i],a,b)
    Matriz_de_resultados[i,0]=N[i]
    Matriz_de_resultados[i,1]=I
    Matriz_de_resultados[i,2]=(I-Valor_referencia)/Valor_referencia*100

print(Matriz_de_resultados)

'''
Resolución son Simpson de Scipy
 
'''
h=50
a=0
b=100

X=np.arange(a,b+1,h)

Y=0.5+0.005*X

I=sp.integrate.simpson(Y,X)
print('La solución de la integral a través de scipy es {}'.format(I))