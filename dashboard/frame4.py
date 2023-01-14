
from app import app
from dash import html
from dash.dependencies import Input, Output

def create_layout():
    return html.Div([
        html.H2('This is the raw HTML page for Page 4'),
        html.P('You can add any raw HTML, CSS and JavaScript code here'),
        html.A('Example Link', href='https://www.example.com')
    ])

# Add the callback to update the content of the page4-content div
@app.callback(Output('page4-content', 'children'), [Input('url', 'pathname')])
def update_page1_content(pathname):
    if pathname == '/page4':
        return create_layout()
