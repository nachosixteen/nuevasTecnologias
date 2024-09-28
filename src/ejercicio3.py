#4. Muestre que estudiantes tienen falta

import pandas as pd 
import openpyxl
from tabulate import tabulate

columnas = [0,9]
dt=pd.read_excel("ejemplo.xlsx", sheet_name="Hoja1", header=0, useCols=columnas)
faltas = dt[dt.iloc[:, 1] < 0]
print(tabulate(faltas, headers='keys', tablefmt='psql'))