'''
from app import app
from dash import html
from dash.dependencies import Input, Output

def create_layout():
    return html.Div([
        html.H2('This is the raw HTML page for Page 2'),
        html.P('You can add any raw HTML, CSS and JavaScript code here'),
        html.A('Example Link', href='https://www.example.com')
    ])

# Add the callback to update the content of the page2-content div
@app.callback(Output('page2-content', 'children'), [Input('url', 'pathname')])
def update_page2_content(pathname):
    if pathname == '/page2':
        return create_layout()
'''

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objects as go


app = Dash(__name__)

colors = {
    'background': 'grey',
    'text': '#7FDBFF'
}

#-----------Lecture dataframe--------------------------------------------------------------   
df_bioenergie_prevision = pd.read_csv('prevision-production/bioenergie/prevision-bioenergie.csv', sep=',')
df_bioenergie_actuelle = pd.read_csv('cleaneddata/production_electricite_bioenergie.csv', sep=',')
df_charbon_prevision = pd.read_csv('prevision-production/charbon/prevision-charbon.csv', sep=',')
df_charbon_actuelle = pd.read_csv('cleaneddata/production_electricite_charbon.csv', sep=',')
df_eolien_prevision = pd.read_csv('prevision-production/eolien/prevision-eolien.csv', sep=',')
df_eolien_actuelle = pd.read_csv('cleaneddata/production_electricite_eolien.csv', sep=',')
df_gaz_prevision = pd.read_csv('prevision-production/gaz/prevision-gaz.csv', sep=',')
df_gaz_actuelle = pd.read_csv('cleaneddata/production_electricite_gaz.csv', sep=',')
df_hydro_prevision = pd.read_csv('prevision-production/hydraulique/prevision-hydraulique.csv', sep=',')
df_hydro_actuelle = pd.read_csv('cleaneddata/production_electricite_hydraulique.csv', sep=',')
df_nucleaire_prevision = pd.read_csv('prevision-production/nucleaire/prevision-nucleaire.csv', sep=',')
df_nucleaire_actuelle = pd.read_csv('cleaneddata/production_electricite_nucleaire.csv', sep=',')
df_solaire_prevision = pd.read_csv('prevision-production/solaire/prevision-solaire.csv', sep=',')
df_solaire_actuelle = pd.read_csv('cleaneddata/production_electricite_solaire.csv', sep=',')

#-----------Nettoyage dataframe------------------------------------------------------------
#bioenergie
df_bioenergie_prevision = df_bioenergie_prevision[df_bioenergie_prevision['ds'] > '2020-12-31']
df_bioenergie_prevision = df_bioenergie_prevision[['ds','yhat']]
df_bioenergie_prevision = df_bioenergie_prevision.rename(columns={'ds':'annee','yhat':'production électricité MWh'})
df_bioenergie = pd.concat([df_bioenergie_actuelle,df_bioenergie_prevision], axis=0)
df_bioenergie['filière'] = "bioénergie"

#charbon
df_charbon_prevision = df_charbon_prevision[df_charbon_prevision['ds'] > '2020-12-31']
df_charbon_prevision = df_charbon_prevision[['ds','yhat']]
df_charbon_prevision = df_charbon_prevision.rename(columns={'ds':'annee','yhat':'production électricité MWh'})
df_charbon_actuelle['production électricité TWh'] = df_charbon_actuelle['production électricité TWh'] * 1000000
df_charbon_actuelle = df_charbon_actuelle.rename(columns={'production électricité TWh':'production électricité MWh'})
df_charbon = pd.concat([df_charbon_actuelle,df_charbon_prevision], axis=0)
df_charbon['filière'] = "charbon"

#eolien
df_eolien_prevision = df_eolien_prevision[df_eolien_prevision['ds'] > '2020-12-31']
df_eolien_prevision = df_eolien_prevision[['ds','yhat']]
df_eolien_prevision = df_eolien_prevision.rename(columns={'ds':'annee','yhat':'production électricité MWh'})
df_eolien_actuelle['production électricité TWh'] = df_eolien_actuelle['production électricité TWh'] * 1000000
df_eolien_actuelle = df_eolien_actuelle.rename(columns={'production électricité TWh':'production électricité MWh'})
df_eolien = pd.concat([df_eolien_actuelle,df_eolien_prevision], axis=0)
df_eolien['filière'] = "éolien"

#gaz
df_gaz_prevision = df_gaz_prevision[df_gaz_prevision['ds'] > '2020-12-31']
df_gaz_prevision = df_gaz_prevision[['ds','yhat']]
df_gaz_prevision = df_gaz_prevision.rename(columns={'ds':'annee','yhat':'production électricité MWh'})
df_gaz_actuelle['production électricité TWh'] = df_gaz_actuelle['production électricité TWh'] * 1000000
df_gaz_actuelle = df_gaz_actuelle.rename(columns={'production électricité TWh':'production électricité MWh'})
df_gaz = pd.concat([df_gaz_actuelle,df_gaz_prevision], axis=0)
df_gaz['filière'] = "gaz"

#hydraulique
df_hydro_prevision = df_hydro_prevision[df_hydro_prevision['ds'] > '2020-12-31']
df_hydro_prevision = df_hydro_prevision[['ds','yhat']]
df_hydro_prevision = df_hydro_prevision.rename(columns={'ds':'annee','yhat':'production électricité MWh'})
df_hydro_actuelle['production électricité TWh'] = df_hydro_actuelle['production électricité TWh'] * 1000000
df_hydro_actuelle = df_hydro_actuelle.rename(columns={'production électricité TWh':'production électricité MWh'})
df_hydro = pd.concat([df_hydro_actuelle,df_hydro_prevision], axis=0)
df_hydro['filière'] = "hydraulique"

#nucleaire
df_nucleaire_prevision = df_nucleaire_prevision[df_nucleaire_prevision['ds'] > '2020-12-31']
df_nucleaire_prevision = df_nucleaire_prevision[['ds','yhat']]
df_nucleaire_prevision = df_nucleaire_prevision.rename(columns={'ds':'annee','yhat':'production électricité MWh'})
df_nucleaire_actuelle["production électricité TWh"] = df_nucleaire_actuelle["production électricité TWh"] * 1000000
df_nucleaire_actuelle = df_nucleaire_actuelle.rename(columns={'production électricité TWh':'production électricité MWh'})
df_nucleaire = pd.concat([df_nucleaire_actuelle,df_nucleaire_prevision], axis=0)
df_nucleaire['filière'] = "nucléaire"

#solaire
df_solaire_prevision = df_solaire_prevision[df_solaire_prevision['ds'] > '2020-12-31']
df_solaire_prevision = df_solaire_prevision[['ds','yhat']]
df_solaire_prevision = df_solaire_prevision.rename(columns={'ds':'annee','yhat':'production électricité MWh'})
df_solaire_actuelle['production électricité TWh'] = df_solaire_actuelle['production électricité TWh'] * 1000000
df_solaire_actuelle = df_solaire_actuelle.rename(columns={'production électricité TWh':'production électricité MWh'})
df_solaire = pd.concat([df_solaire_actuelle,df_solaire_prevision], axis=0)
df_solaire['filière'] = "solaire"

#fusion de tous les dataframes
df_production = pd.concat([df_bioenergie,df_charbon,df_eolien,df_gaz,df_hydro,df_nucleaire,df_solaire], axis=0)
df_production['annee']= df_production['annee'].replace(regex="-12-31",value="")


#sauvegarde du dataframe
#df_production.to_csv('df_production.csv', index=False)


fig = px.bar(df_production, x="annee", y="production électricité MWh", color="filière", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='bar-chart',
        figure=fig
    ),
    dcc.Checklist(
        id="checklist-bar",
        options=["nucléaire", "éolien", "gaz","solaire","hydraulique","charbon","bioénergie"],
        value=["nucléaire", "gaz","charbon"],
        inline=True,
    ),
    html.Div(children=[
        html.Label('Dropdown'),
        dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),

        html.Br(),
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'],
                    ['Montréal', 'San Francisco'],
                    multi=True),

        html.Br(),
        html.Label('Radio Items'),
        dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        html.Label('Checkboxes'),
        dcc.Checklist(['New York City', 'Montréal', 'San Francisco'],
                    ['Montréal', 'San Francisco']
        ),

        html.Br(),
        html.Label('Text Input'),
        dcc.Input(value='MTL', type='text'),

        html.Br(),
        html.Label('Slider'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
            value=5,
        ),
    ], style={'padding': 10, 'flex': 1}),
    html.Div([
    html.H4('Life expentancy progression of countries per continents'),
    dcc.Graph(id="line-chart"),
    dcc.Checklist(
        id="checklist-line",
        options=["nucléaire", "éolien", "gaz","solaire","hydraulique","charbon","bioénergie"],
        value=["nucléaire", "gaz","charbon"],
        inline=True,
    ),
    ])
])


@app.callback(
    Output("line-chart", "figure"), 
    Input("checklist-line", "value"))
def update_line_chart(filiere):
    filtre = df_production['filière'].isin(filiere)
    fig = px.line(df_production[filtre], 
        x="annee", y="production électricité MWh", color='filière')
    return fig

@app.callback(
    Output("bar-chart", "figure"), 
    Input("checklist-bar", "value"))
def update_bar_chart(filiere):
    filtre = df_production['filière'].isin(filiere)
    fig = px.bar(df_production[filtre], x="annee", y="production électricité MWh", color='filière',barmode="group")
    
    '''
    fig.add_trace(
        go.Scatter(
        x=df_production[df_production['production électricité MWh'][(df_production['filière'] == 'nucléaire')]],
        y=df_production['annee'],
    ))
    '''
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)


app = Dash(__name__)
