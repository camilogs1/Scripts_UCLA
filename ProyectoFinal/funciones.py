import pandas as pd
from dfply import *
import re

def getting(df, grupos):
    current = {}
    
    for i in grupos.index:
        print(i)
        articulo = pd.read_html(grupos.iloc[i][1])
        articulo = articulo[13]
        articulo = articulo.iloc[1: ,1]
        grupo = grupos.iloc[i][0]
        current.update(producto = articulo, grupo = grupo)
        df = df.append(pd.DataFrame(current))
    
    return df
    
def obtener_año(x):
    
    x = x.assign(año = lambda x: x['producto'].map(lambda producto: re.sub(".*ISSN", "", producto))).assign(año = lambda x: x['año'].map(lambda año:  re.sub(" vol.*", "", año))).assign(año = lambda x: x['año'].map(lambda año:  re.sub(".*, ", "", año)))
    return x