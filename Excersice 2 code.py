"""
Tarea semana 02: Integración y derivación numérica

Sección 2 - Newton-Raphson

@author: Elena Esquivel Murillo
"""
import numpy as np;

def DefinirFunción(t):
    '''
    Define la función de posición y la evalúa en un tiempo t

    Parámetros
    ----------
    t : tiempo en el cual se evalúa la función.

    Devuelve
    -------
    valorFunción : Valor de la funcion en el tiempo t

    '''
    valorFunción=-5+0.005*t**2
    return valorFunción

def DerivarFunción(t):
    '''
    Según la derivada analitica de la función de posición,
    calcula el valor de esta en un tiempo t

    Parámetros
    ----------
    t : tiempo en el cual se evalúa la derivada

    Devuelve
    -------
    derivada : Valor de la derivada en el tiempo t

    '''
    derivada=0.01*t
    return derivada

def CalcularTi(t0):
    '''
    Calcula la siguiente aproximación de la variable independiente (tiempo, t)
    para encontrar la raíz de la función según la fórmula de Newton-Raphson

    Parámetros
    ----------
    t0 : aproximación de tiempo anterior

    Devuelve
    -------
    ti : nueva aproximación de tiempo.

    '''
    ti=t0-DefinirFunción(t0)/(DerivarFunción(t0))
    return ti

def CalcularIncertidumbre(t):
    '''
    Define el valor exacto según la solución analitica de la función de
    posición y calcula la incertidumbre relativa al valor exacto para un
    tiempo t

    Parámetro
    ----------
    t : tiempo para calcula la incertidumbre

    Devuelve
    -------
    incertidumbreRelativa : valor de la incertidumbre relativa al valor
    exacto en el tiempo t

    '''
    valorExacto=10*10**(1/2)
    incertidumbreRelativa=(valorExacto-np.absolute(t))/valorExacto
    print(incertidumbreRelativa)
    return incertidumbreRelativa

t0=3
print(DefinirFunción(t0))
contador=0
while np.absolute(CalcularIncertidumbre(t0))>0.01:
    ti=CalcularTi(t0)
    t0=ti
    contador=contador+1
    print(contador)
    print(t0)