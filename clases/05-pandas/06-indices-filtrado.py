# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:49:37 2019

@author: USRBET
"""

import pandas as pd

path_guardado_bin = "C://Users//USRBET//Documents//py-diaz-yanangomez-leslie-mishell//clases//05-pandas//data//artwork_data_bin.pickle"
dataframe = pd.read_pickle(path_guardado_bin)
# df = dataframe.iloc[49999:50100,:].copy()