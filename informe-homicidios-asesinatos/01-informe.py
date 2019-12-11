# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:45:18 2019

@author: PAVILLION
"""

import numpy as np
import pandas as pd
import os

path_dataset = "L://Familia//Documents//2019B-OCTAVOSEMESTRE//Python//py-diaz-yanangomez-leslie-mishell//informe-homicidios-asesinatos//dataset-homicidios.csv"

columnas = ["State", 
            "Year", 
            "Month",
            "Crime Type",
            "Crime Solved",
            "Victim Sex",
            "Victim Age",
            "Victim Race",
            "Victim Ethnicity",
            "Perpetrator Sex",
            "Perpetrator Age",
            "Perpetrator Race",
            "Perpetrator Ethnicity",
            "Relationship",
            "Weapon"]

dataframe = pd.read_csv(path_dataset,
                        nrows = 10000,
                        usecols = columnas)

# ESTADISTICAS
estado = dataframe["State"].value_counts() # En EEUU
año =  dataframe["Year"].value_counts()
mes = dataframe["Month"].value_counts()
tipo_crimen = dataframe["Crime Type"].value_counts() # Asesinato u Homicidio/Homicidio por negligencia
is_crimen_resuelto = dataframe["Crime Solved"].value_counts() # Crimenes resueltos si o no
sexo_victima = dataframe["Victim Sex"].value_counts() # Hombre, mujer, otros
edad_victima = dataframe["Victim Age"].value_counts()
raza_victima = dataframe["Victim Race"].value_counts() # Blanco, Negro, Otros
etnia_victima = dataframe["Victim Ethnicity"].value_counts() #Desconocido, Hispano, No hispano
sexo_perpetrador = dataframe["Perpetrator Sex"].value_counts()
edad_perpetrador = dataframe["Perpetrator Age"].value_counts()
raza_perpetrador = dataframe["Perpetrator Race"].value_counts()
etnia_perpetrador = dataframe["Perpetrator Ethnicity"].value_counts()
relacion = dataframe["Relationship"].value_counts()
groupby_arma = dataframe.groupby("Perpetrator Sex")["Weapon"]
print(groupby_arma)

#PROMEDIO
#Rangos de edad victima
#Rangos de edad perpetrador
# Hombres --> Armas de preferencia

# Mujeres --> Armas de preferencia
# Femicidios --> Hombre, Mujer, Husband/Wife
# Cuantos casos resueltos para el rango de edades mas frecuente

