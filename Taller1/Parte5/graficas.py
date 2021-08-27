#datos tomados de: https://www.datos.gov.co/Educaci-n/Poblaci-n-Estudiantil/maqr-kqmi

import pandas as pd
import plotly.express as px

from plotly.offline import plot
    
datos = pd.read_excel("Poblacion_Estudiantil.xlsx")

fig = px.bar(datos, x='CANTIDAD MATRICULADOS', y='METODOLOGIA')
plot(fig)

fig2 = px.pie(datos, values='RECIBIERON APOYOS FINANCIEROS', names='AÑO')
plot(fig2)

fig3 = px.bar(datos, x='PROGRAMA', y='AÑO')
plot(fig3)

hombres = datos['HOMBRES']
hombres = sum(hombres)
mujeres = datos['MUJERES']
mujeres = sum(mujeres)
generos = pd.DataFrame()
generos['genero'] = ['HOMBRES','MUJERES']
generos['cantidad'] = [hombres,mujeres]
fig2 = px.pie(generos, values='cantidad', names='genero')
plot(fig2)
