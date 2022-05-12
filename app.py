#llamar librerias
from dash import Dash, html, dcc  #libreria para servidor web de data science
import pandas as pd              #libreria para procesar datos
import plotly.graph_objs as go   #libreria para graficar

#declarar objetos principales
app = Dash(__name__)
#cargar la base de datos
df = pd.read_excel('data.xlsx')
#configurar el sitio web
app.layout = html.Div([html.H1('Programa para ver el covid en AMVA'),
                       html.Div('Informacion de la pagina, bla bla bla...'),
                       dcc.Graph(id= 'map',figure={
                           'data':[{'lat':df['Latitud'],
                                    'lon':df['Longitud'],
                                    'marker':{
                                        'color': 150,
                                        'size': df['Enfermos'],
                                        'opacity': 0.6
                                    },
                                    'customdata': df['Enfermos'],
                                    'type':'scattermapbox'}],
                           'layout':{'mapbox':{
                           'accesstoken': 'pk.eyJ1IjoibGVvbmFyZG9iZXRhbmN1ciIsImEiOiJjazlybGNiZWcwYjZ6M2dwNGY4MmY2eGpwIn0.EJjpR4klZpOHSfdm7Tsfkw',
                           'center':{'lat':6.240737,'lon':-75.589900},
                           'zoom':10},
                           'hovermode':'closest',
                           'margin':{'l':0,'r':0,'b':0,'t':0}}                           
                       })])
#funcion principal
if __name__ == '__main__':
    #cargar el objeto principal a todas las interfaces de red en el puerto 80
    app.run_server(host='0.0.0.0',port=80)