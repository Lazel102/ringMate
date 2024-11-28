import numpy as np
import matplotlib.pyplot as plt
import json


# Chemin du fichier JSON
file_path = 'we2.json'

# Chargement du fichier JSON
with open(file_path, 'r') as file:
    data = json.load(file)

# Récupération de la liste L
L = data['L']
begin_box=""
end_box=""
print(L)
eps_z=25

i=0
N=len(L)
dic_value_x_begin={0 : L[0][coordinates][x]}
dic_value_y_begin={L[0][coordinates][y]}
value_x_begin=0
value_y_begin=0
value_y_end=0
value_x_end=0
dic_value_x_end={}
dic_value_y_end={}

while np.abs(L[i][coordinates][x]-L[0][coordinates][x])<eps_z :
    dic_value_x_begin[i+1]=L[i+1][coordinates][x]
    dic_value_y_begin[i+1]=L[i+1][coordinates][y]
    i=i+1
for j in range(len(dic_value_x_begin)):
    value_x_begin+=dic_value_x_begin[j]
    value_y_begin+=dic_value_y_begin[j]
value_x_begin=value_x_begin/len(dic_value_x_begin)
value_y_begin=value_y_begin/len(dic_value_x_begin)
while np.abs(L[i][coordinates][x]-L[0][coordinates][x])>eps_z :
    i=i+1
while i<len(L):
    dic_value_x_end[i+1]=L[i+1][coordinates][x]
    dic_value_y_end[i+1]=L[i+1][coordinates][y]
    i=i+1
for j in range(len(dic_value_x_end)):
    value_x_end+=dic_value_x_end[j]
    value_y_end+=dic_value_y_end[j]
value_x_end=value_x_end/len(dic_value_x_end)
value_y_end=value_y_end/len(dic_value_x_end)