import pandas as pd 
import openpyxl
from tabulate import tabulate
columnas=[0,3]

dt=pd.read_excel("ejemplo.xlsx", sheet_name="Hoja1", header=0, usecols=columnas)
print(tabulate(dt))
print(dt[dt["28 de julio"]==0])

#El punto 4 y 5 se tienen que realizar con ejemplo.xlsx, los demas con taller.xlsx