from pygments.lexers import go

from app import app
from dash import html, dcc
from dash.dependencies import Input, Output

# Frame 1 : Conséquence de la répartitiion des filieres sur le prix & sur l'environnement
# ( mettre des sliders pour les filieres (la part) et l'évolution en fonction du prix)
# pour vous @thmsfnr @Loxy

def create_layout():
    # mettre deux div a cote (une pour le prix et une pour l'environnement)
    # mettre un slider pour la part de chaque filière
    return html.Div([
        html.Div([
            html.P('Hydraulique :'),
            dcc.Slider(0, 100, 1, value=5, marks=None,
                       tooltip={"placement": "bottom", "always_visible": True}),
            html.P('Nucléaire :'),
            dcc.Slider(id='nuclear',min =0, max= 100, step=1, value=5, marks=None,
                       tooltip={"placement": "bottom", "always_visible": True}),
            html.P('Eolien :'),
            dcc.Slider(id='wind', min=0, max=100, step=1, value=5, marks=None,
                       tooltip={"placement": "bottom", "always_visible": True}),
            html.P('Solaire :'),
            dcc.Slider(id='solar', min=0, max=100, step=1, value=5, marks=None,
                        tooltip={"placement": "bottom", "always_visible": True}),
            html.P('Gaz :'),
            dcc.Slider(id='gas', min=0, max=100, step=1, value=5, marks=None,
                        tooltip={"placement": "bottom", "always_visible": True}),
            html.P('Charbon :'),
            dcc.Slider(id='coal', min=0, max=100, step=1, value=5, marks=None,
                        tooltip={"placement": "bottom", "always_visible": True}),
            html.P('Fioul :'),
            dcc.Slider(id='oil', min=0, max=100, step=1, value=5, marks=None,
                        tooltip={"placement": "bottom", "always_visible": True}),
        ]),
        html.Div([
            # Display the price
            html.P('Prix :'),
            html.Div(id='price'),
        ]),
    ])


@app.callback(
    Output('price', 'children'),
    [Input('nuclear', 'value'),
     Input('wind', 'value'),
     Input('solar', 'value'),
     Input('gas', 'value'),
     Input('coal', 'value'),
     Input('oil', 'value')])
def price(nuclear, wind, solar, gas, coal, oil):
    price = nuclear * 0.1 + wind * 0.2 + solar * 0.3 + gas * 0.4 + coal * 0.5 + oil * 0.6
    print(price)
    return f'{price} €'


# Add the callback to update the content of the page1-content div
@app.callback(Output('page1-content', 'children'), [Input('url', 'pathname')])
def update_page1_content(pathname):
    if pathname == '/page1':
        return create_layout()
