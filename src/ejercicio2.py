#3. Cuál es el nombre de los estudiantes de los primeros 9 registros

import pandas as pd 
import openpyxl
from tabulate import tabulate

dt=pd.read_excel("taller.xlsx", sheet_name="hoja1", header=0)
# print(tabulate(dt))
print (tabulate(dt.head(9)["Nombre"]))