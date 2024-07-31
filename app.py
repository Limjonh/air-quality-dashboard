import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Dados fictícios para a demonstração
data = {
    'Local': ['Área 1', 'Área 2', 'Área 3', 'Área 4', 'Área 5'],
    'PM2.5': [55, 40, 65, 30, 50],
    'PM10': [100, 80, 120, 60, 90],
    'O3': [30, 25, 40, 20, 35]
}
df = pd.DataFrame(data)

# Inicializar o aplicativo Dash
app = dash.Dash(__name__)

# Layout do Dashboard
app.layout = html.Div(children=[
    html.H1(children='Dashboard de Qualidade do Ar'),

    html.Div(children='''
        Monitoramento da qualidade do ar em tempo real.
    '''),

    dcc.Dropdown(
        id='sensor-dropdown',
        options=[
            {'label': 'PM2.5', 'value': 'PM2.5'},
            {'label': 'PM10', 'value': 'PM10'},
            {'label': 'O3', 'value': 'O3'}
        ],
        value='PM2.5'
    ),

    dcc.Graph(
        id='air-quality-graph'
    )
])

# Callback para atualizar o gráfico
@app.callback(
    Output('air-quality-graph', 'figure'),
    Input('sensor-dropdown', 'value')
)
def update_graph(selected_sensor):
    fig = px.bar(df, x='Local', y=selected_sensor, title=f'Níveis de {selected_sensor}')
    fig.update_layout(xaxis_title='Local', yaxis_title=selected_sensor)
    return fig

# Executar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
