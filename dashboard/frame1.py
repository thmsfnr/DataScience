
from app import app
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

def create_layout():
    dcc.Store(id='energy-mix', storage_type='session',
              data={'hydraulic': 5, 'nuclear': 5, 'wind': 5, 'solar': 5, 'gas': 5, 'coal': 5, 'oil': 5}),
    return html.Div([
        html.H2('Energy Mix Simulator'),
        html.P('Adjust the proportion of different energy sources using the sliders below'),
        dcc.Store(id='energy-mix', storage_type='session'),
        html.Div([
            html.P('Hydraulic :'),
            dcc.Slider(id='hydraulic', min=0, max=100, step=1, value=5, marks={i: f'{i}%' for i in range(0, 101, 25)},
                      tooltip={"placement": "bottom", "always_visible": True}),
            html.P('Nuclear :'),
            dcc.Slider(id='nuclear', min=0, max=100, step=1, value=5, marks={i: f'{i}%' for i in range(0, 101, 25)},
                      tooltip={"placement": "bottom", "always_visible": True}),
            html.P('Wind :'),
            dcc.Slider(id='wind', min=0, max=100, step=1, value=5, marks={i: f'{i}%' for i in range
            (0, 101, 25)},
                       tooltip={"placement": "bottom", "always_visible": True}),
            html.P('Solar :'),
            dcc.Slider(id='solar', min=0, max=100, step=1, value=5, marks={i: f'{i}%' for i in range(0, 101, 25)},
                       tooltip={"placement": "bottom", "always_visible": True}),
            html.P('Gas :'),
            dcc.Slider(id='gas', min=0, max=100, step=1, value=5, marks={i: f'{i}%' for i in range(0, 101, 25)},
                       tooltip={"placement": "bottom", "always_visible": True}),
            html.P('Coal :'),
            dcc.Slider(id='coal', min=0, max=100, step=1, value=5, marks={i: f'{i}%' for i in range(0, 101, 25)},
                       tooltip={"placement": "bottom", "always_visible": True}),
            html.P('Oil :'),
            dcc.Slider(id='oil', min=0, max=100, step=1, value=5, marks={i: f'{i}%' for i in range(0, 101, 25)},
                       tooltip={"placement": "bottom", "always_visible": True}),
        ]),
        html.Div([
                     # Display the price
                     html.P('Price :'),
            html.Div(id='price', style = {'color': 'blue'}, children='Initial Price'),
        ]),
    ])

# callback to store current slider values in the energy-mix store
@app.callback(
    Output('energy-mix', 'data'),
    [Input('hydraulic', 'value'), Input('nuclear', 'value'), Input('wind', 'value'),
     Input('solar', 'value'), Input('gas', 'value'), Input('coal', 'value'), Input('oil', 'value')])
def store_energy_mix(hydraulic, nuclear, wind, solar, gas, coal, oil):
    energy_mix = {'hydraulic': hydraulic, 'nuclear': nuclear, 'wind': wind, 'solar': solar, 'gas': gas, 'coal': coal,
                  'oil': oil}
    dash.callback_context.response.set_data(energy_mix)


# callback to update the displayed price
@app.callback(
    Output('price', 'children'),
    [Input('energy-mix', 'data')])
def update_price(energy_mix):
    total = energy_mix['hydraulic'] + energy_mix['nuclear'] + energy_mix['wind'] + energy_mix['solar'] + energy_mix['gas'] + energy_mix['coal'] + energy_mix['oil']
    if total != 100:
        return 'Invalid energy mix'
    else:
        price = energy_mix['hydraulic'] * 0.1 + energy_mix['nuclear'] * 0.2 + energy_mix['wind'] * 0.3 + energy_mix['solar'] * 0.4 + energy_mix['gas'] * 0.5 + energy_mix['coal'] * 0.6 + energy_mix['oil'] * 0.7
        return price

        # Add the callback to update the content of the page1-content div
@app.callback(Output('page1-content', 'children'), [Input('url', 'pathname')])
def update_page1_content(pathname):
    if pathname == '/page1':
        return create_layout()
