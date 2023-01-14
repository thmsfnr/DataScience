import dash
from dash import html, dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

import description
import frame1
import frame2
import frame3
import frame4
import frame5

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.H1("Analyse de l'arret de l'utilisation du nucléaire dans la production d'électricité en France"),
    dcc.Dropdown(
        id='page-selector',
        options=[
            {'label': 'Description', 'value': '/description'},
            {'label': 'Page 1', 'value': '/page1'},
            {'label': 'Page 2', 'value': '/page2'},
            {'label': 'Page 3', 'value': '/page3'},
            {'label': 'Page 4', 'value': '/page4'},
            {'label': 'Page 5', 'value': '/page5'},
        ],
        value='/description',
        style={'width': '50%'}
    ),
    html.Div(id='page-content')
])

@app.callback(Output('url', 'pathname'), [Input('page-selector', 'value')])
def update_pathname(pathname):
    return pathname

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page1':
        return frame1.create_layout()
    elif pathname == '/page2':
        return frame2.create_layout()
    elif pathname == '/page3':
        return frame3.create_layout()
    elif pathname == '/page4':
        return frame4.create_layout()
    elif pathname == '/page5':
        return frame5.create_layout()
    elif pathname == '/description':
        return description.create_layout()
    else:
        return '404 Page not found'

if __name__ == '__main__':
    app.run_server(debug=True)
