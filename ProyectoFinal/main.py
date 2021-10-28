import pandas as pd
from dfply import *
import re
from funciones import *

grupos_ucla = pd.read_csv("https://docs.google.com/spreadsheets/d/10fAVkAksNJbBec5lyc8zYMq9UH3lF2GPwkKJpGQqnQY/export?format=csv&gid=0")

grupos_comparar = pd.read_csv("https://docs.google.com/spreadsheets/d/10fAVkAksNJbBec5lyc8zYMq9UH3lF2GPwkKJpGQqnQY/export?format=csv&gid=176714491")


grupo_df_ucla = pd.DataFrame(columns=['grupo','producto'])
grupo_df_comparar = pd.DataFrame(columns=['grupo','producto'])

#Producción articulos
grupo_df_ucla = getting(grupo_df_ucla, grupos_ucla)
grupo_df_comparar = getting(grupo_df_comparar, grupos_comparar)


#limpieza
cleaning_ucla = cleaning(grupo_df_ucla)
ucla = cleaning_ucla.drop(["producto"], axis=1)
cleaning_comparar = cleaning(grupo_df_comparar)
comparar = cleaning_comparar.drop(["producto"], axis=1)

#Exportar
exportar(ucla,comparar)
