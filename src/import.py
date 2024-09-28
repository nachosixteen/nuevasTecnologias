import pandas as pd 
import openpyxl
from tabulate import tabulate


dt=pd.read_excel("ejemplo.xlsx", sheet_name="Hoja1", header=None)
print(tabulate(dt