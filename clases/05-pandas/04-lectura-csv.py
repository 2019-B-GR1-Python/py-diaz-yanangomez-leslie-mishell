# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:19:54 2019

@author: USRBET
"""

## Lectura CSV

import pandas as pd
import os
## Grupos de archivos que lee PANDAS
# 1) JSON, CSV, HTML, XML
# 2) BINARY FILES -> (sdf423rewwfc1°c 554))
# 3) Bases de datos relacionales

path_archivo = "C://Users//USRBET//Documents//py-diaz-yanangomez-leslie-mishell//clases//05-pandas//data//artwork_data.csv"
## Dataframe de un archivo
dataframe1 = pd.read_csv(path_archivo, nrows = 10)

columnas = ["id", "artist", "title",
            "medium", "year", "acquisitionYear", 
            "height", "width", "units"]

## Usar ciertas columnas
dataframe2 = pd.read_csv(path_archivo, nrows = 10, 
                         usecols = columnas )

## Usando una columna como index

dataframe3 = pd.read_csv(path_archivo, nrows = 10, 
                         usecols = columnas,
                         index_col = "id")

## Guardar dataframe con cambios realizados para que la tabla no se pierda (modificado)

path_guardado = "C://Users//USRBET//Documents//py-diaz-yanangomez-leslie-mishell//clases//05-pandas//data//artwork_data.pickle"

dataframe3.to_pickle(path_guardado)

dataframe4 = pd.read_csv(path_archivo)

path_guardado_bin = "C://Users//USRBET//Documents//py-diaz-yanangomez-leslie-mishell//clases//05-pandas//data//artwork_data_bin.pickle"

dataframe4.to_pickle(path_guardado_bin)

dataframe5 = pd.read_pickle(path_guardado)









