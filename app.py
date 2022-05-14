#libreria para manejar el entorno grafico desde un server web
import dash             #libreria princiap
from dash import dcc    #libreria para objetos graficos
from dash import html   #libreria para elementos html 
import plotly.graph_objs as go # libreria para graficar 
import pandas as pd    #libreria para manejar datos

app = dash.Dash()   #creo el objeto app con los atributos y metodos de dash
df = pd.read_excel('data.xlsx') #leo mi base de datos
#configuracion web
app.layout = html.Div([
    html.H1('Social Life'),
    html.Div('Usuarios conectados actualmente',id='text-content'),
    dcc.Graph(id='map', figure={
        'data': [{
            'lat': df['lat'],
            'lon': df['lon'],
            'marker': {
                'color': 150,
                'size': df['enfermos'],
                'opacity': 0.6
            },
            'customdata': df['riesgo'],
            'type': 'scattermapbox'
        }],
        'layout': {
            'mapbox': {
                'accesstoken': 'pk.eyJ1IjoibGVvbmFyZG9iZXRhbmN1ciIsImEiOiJjazlybGNiZWcwYjZ6M2dwNGY4MmY2eGpwIn0.EJjpR4klZpOHSfdm7Tsfkw',
                'center' : {
                    'lat': 6.240737,
                    'lon': -75.589900
                    },
                'zoom' : 10
            },
            'hovermode': 'closest',
            'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0}
        }
    })
])
#llamado al programa principal
if __name__ == '__main__':
    app.run_server(debug=True,port=80)
