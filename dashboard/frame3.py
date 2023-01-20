
from app import app
from dash import html
from dash.dependencies import Input, Output

def create_layout():
    return html.Div([
        html.H2('This is the raw HTML page for Page 3'),
        html.P('You can add any raw HTML, CSS and JavaScript code here'),
        html.A('Example Link', href='https://www.example.com')
    ])

# Add the callback to update the content of the page3-content div
@app.callback(Output('page3-content', 'children'), [Input('url', 'pathname')])
def update_page1_content(pathname):
    if pathname == '/page3':
        return create_layout()