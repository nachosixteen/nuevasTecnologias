import pandas as pd 
listauno = ["Mango", "Fresas", "Uva"]
serie = pd.Series(listauno)
print(serie)

listados = {"mango":45,"fresas":4456,"Uva":123}
seriedos = pd.Series(listados) 
print(seriedos)

listatres = ["nombres", "apellidos", "Edad", "Nota"]
listat = ["jesus","arias",45,3.5]
listaIndice = []
dicc = pd.DataFrame(listatres, columns = listat)
print(dicc)