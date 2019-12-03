# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:56:50 2019

@author: Leslie :)
"""

# Output DATA 3/12/2019
import pandas as pd
import numpy as np
import os
import sqlite3
import xlsxwriter

workbook = xlsxwriter.Workbook(path_excel_colores)


path_guardado_bin = "C://Users//USRBET//Documents//py-diaz-yanangomez-leslie-mishell//clases//05-pandas//data//artwork_data_bin.pickle"
dataframe = pd.read_pickle(path_guardado_bin)
df = dataframe.iloc[49999:50100,:].copy()

# Tipos archivos
# 1)JSON
# 2)EXCEL
# 3)SQL

# EXCEL
path_excel = 'C://Users//USRBET//Documents//py-diaz-yanangomez-leslie-mishell//clases//05-pandas//data//mi_dataframe_completo.xlsx'
df.to_excel(path_excel, index=False)
columnas = ['artist', 'title', 'year']
df.to_excel(path_excel, columns=columnas)

# - Multiples hojas de trabajo (en Excel)
path_excel_multiple = 'C://Users//USRBET//Documents//py-diaz-yanangomez-leslie-mishell//clases//05-pandas//data//mi_dataframe_multiple.xlsx'
writer = pd.ExcelWriter(path_excel_multiple, 
                        engine = 'xlsxwriter')

df.to_excel(writer, 
            sheet_name = "Primera")
df.to_excel(writer, 
            sheet_name = "Segunda", 
            index = False)
df.to_excel(writer, 
            sheet_name = "Tercera", 
            columns=columnas)

writer.save()

# Colores

num_artistas = df['artist'].value_counts()

path_excel_colores = 'C://Users//USRBET//Documents//py-diaz-yanangomez-leslie-mishell//clases//05-pandas//data//mi_dataframe_colores.xlsx'
writer = pd.ExcelWriter(path_excel_colores, 
                        engine = 'xlsxwriter')

num_artistas.to_excel(writer, 
            sheet_name = "Artistas")

hoja_artistas = writer.sheets['Artistas']
## Evitar quemado de variables, binding (o algo asi)
rango_celdas = 'B2:B{}'.format(len(num_artistas.index) + 1)

formato_artista = {
        "type": "2_color_scale",
        "min_value": "10",
        "min_type": "percentile",
        "max_value": "99",
        "max_type": "percentile"
        }

hoja_artistas.conditional_format(rango_celdas, formato_artista)

chart = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart.add_series({'values': num_artistas})

# Insert the chart into the worksheet.
hoja_artistas.insert_chart('Artistas', chart)
writer.save()



































