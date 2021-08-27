#datos tomados de: https://www.datos.gov.co/Educaci-n/Poblaci-n-Estudiantil/maqr-kqmi

import pandas as pd

datos = pd.read_excel("Poblacion_Estudiantil.xlsx")

resumen_cuanti = datos.loc[:,['CANTIDAD MATRICULADOS','HOMBRES','MUJERES','RECIBIERON APOYOS FINANCIEROS','RECIBIERON APOYOS ACADÉMICOS']]
resumen = resumen_cuanti.describe().iloc[[0,1,2,3,7], ]
resumen_cuali = datos.iloc[:, 3:5]
cuali = resumen_cuali['METODOLOGIA'].value_counts()
cuali2 = resumen_cuali['PROGRAMA'].value_counts()

print("Resumen estaditico de los estudiantes matriculados en el Colegio Mayor de Antioquia, desde el 2018-2 hasta el 2019-2\n",resumen)
print("\nCantidad de periodos en los que se ofertaron las carreras en el Colegio Mayor de Antioquia del 2018-2 als 2019-2:\n", cuali2)
print("\nModalidad de estudio en las diferentes carreras:\n",cuali)
