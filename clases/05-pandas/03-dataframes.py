# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:41:42 2019

@author: Leslie :)
"""

## DATAFRAMES

import numpy as np
import pandas as pd

arr_pandas = np.random.randint(0,10,6).reshape(2,3)

dataframe_1 = pd.DataFrame(arr_pandas)

s1 = dataframe_1[0]
s2 = dataframe_1[1]
s3 = dataframe_1[2]

s4 = pd.Series(np.array([6,11]))
## Añade como fila (s4 debe ser de 3 items)
dataframe_1.append(s4, ignore_index=True)
## Añade como columna
dataframe_1[3] = s4
dataframe_1[4] = s1 * s2

datos_fisicos_uno = pd.DataFrame(arr_pandas, columns = [
        "Estatura (cm)",
        "Peso (kg)",
        "Edad (anios)"])

datos_fisicos_uno["Estatura (cm)"]

datos_fisicos_dos = pd.DataFrame(arr_pandas, 
        columns = [
        "Estatura (cm)",
        "Peso (kg)",
        "Edad (anios)"],
        index = [
                "Leslie",
                "Mishell"])

## Renombrar columnas e índices
dataframe_1.index = ["Leslie", "Mishell"]
dataframe_1.columns= ["1c", "2c", "3c", "4c", "5c"]

