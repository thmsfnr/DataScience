
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
