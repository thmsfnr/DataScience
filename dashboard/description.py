
from app import app
from dash import html
from dash.dependencies import Input, Output

def create_layout():
    return html.Div([
        html.P("Ce projet est une analyse de la sortie du nucléaire dans la production d'électricité française réalisée lors d'un cours à Polytech Montpellier."),
        html.P("Ce projet visait initialement à nous permettre d'approfondir certaines connaissances acquises au cours de notre formation, d'en découvrir d'autres, d'identifier des méthodes appropriées pour répondre à un objectif donné, de combiner des méthodes complémentaires, de comparer des méthodes concurrentes pour répondre à des objectifs donnés, d'interpréter et éventuellement de comparer les résultats des méthodes mises en œuvre, ainsi que d'avoir un esprit critique vis-à-vis de la collecte des données, des méthodes mises en œuvre et de leur paramétrage."),
        html.P("Concernant le sujet, nous avions le choix entre différents thèmes et nous avons choisi celui lié à l'étude des données ouvertes, plus précisément lié au projet d'Université des données ouvertes mené par l'association Latitudes en lien avec le site institutionnel national data gouv. Les jeux de données de ce thème sont alors multiples, sachant que nous avons fait le choix d'étudier celui associé à l'énergie en France."),
        html.P("Concernant la problématique, nous en avons choisi une qui diffère de celle proposée dans le projet. Au lieu de centrer notre étude sur les conséquences énergétiques de la guerre en Ukraine, nous allons déterminer les conséquences de la fin du nucléaire dans la production d'électricité en France."),
        html.A("Pour plus d'informations", href='https://github.com/thmsfnr/DataScience')
    ])

# Add the callback to update the content of the description-content div
@app.callback(Output('description-content', 'children'), [Input('url', 'pathname')])
def update_page1_content(pathname):
    if pathname == '/description':
        return create_layout()
