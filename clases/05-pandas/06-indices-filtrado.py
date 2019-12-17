# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:49:37 2019

@author: USRBET
"""

import pandas as pd

path_guardado_bin = "C://Users//USRBET//Documents//py-diaz-yanangomez-leslie-mishell//clases//05-pandas//data//artwork_data_bin.pickle"
dataframe = pd.read_pickle(path_guardado_bin)

## Obtener nombre artistas
serie_artistas_repetidos = dataframe['artist']

artistas = pd.unique(serie_artistas_repetidos)

## Cuantos artistas hay?
artistas.size # or len(artistas)

## obras de blake, william
blake = serie_artistas_repetidos == "Blake, William"
blake.value_counts()
serie_artistas_repetidos.value_counts()

df_blake = dataframe[blake]