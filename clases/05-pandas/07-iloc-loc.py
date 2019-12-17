# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:04:45 2019

@author: USRBET
"""

import pandas as pd
import numpy as np

path_guardado_bin = "C://Users//USRBET//Documents//py-diaz-yanangomez-leslie-mishell//clases//05-pandas//data//artwork_data_bin.pickle"
dataframe = pd.read_pickle(path_guardado_bin)
dataframe_2 = pd.read_pickle(path_guardado_bin)
columnas_index = dataframe_2["id"]
dataframe_2 = dataframe_2.set_index("id")
primero_sin_columnas = dataframe.loc[1035]

datos = {
        "nota1":{
            "Pepito": 7,
            "Juanita": 8,
            "Maria": 9},
        "disciplina": {
            "Pepito": 5,
            "Juanita": 9,
            "Maria": 3
                }}
notas = pd.DataFrame(datos)

notas.loc["Pepito", "disciplina"]
 ## INDICE, COLUMNAS
notas.loc[["Pepito", "Juanita"], "nota1"]
notas.loc[["Pepito"], ["disciplina", "nota1"]]

### CONDICIONES
condicion_nota = notas["nota1"] > 7 
condicion_disciplina = notas["disciplina"] > 7
mayores_7 = notas.loc[condicion_nota]

## Especifico - setear valor
notas.loc["Maria", "disciplina"] = 7

## Columna
notas.loc[:, "disciplina"] = 7

## Fila
##subir disciplina a 7
condicion_nota = notas["disciplina"] < 7
notas.loc[condicion_nota, "disciplina"] = 7

## Promedio final
notas["promedio"] = (notas["nota1"] + notas["disciplina"])/2