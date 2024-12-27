import sys
import os

# Add the path to the stanford_compression_library directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'stanford_compression_library')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'stanford_compression_library', 'scl')))

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from compressors.rANS import rANSEncoder, rANSParams, Frequencies, DataBlock

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("rANS Encoding Steps"), className="text-center")
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Input Symbol Frequencies"),
            dcc.Textarea(
                id='input-frequencies',
                value='A A B B C',
                style={'width': '100%', 'height': 100},
            ),
            html.Button('Set Frequencies', id='set-frequencies-button', n_clicks=0),
            html.Div(id='frequencies-result')
        ], width=6),
        dbc.Col([
            html.H3("Input Sequence to Encode"),
            dcc.Textarea(
                id='input-sequence',
                value='A B C',
                style={'width': '100%', 'height': 100},
            ),
            html.Button('Encode', id='encode-button', n_clicks=0),
            html.Div(id='encoded-result')
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Encoding Steps"),
            html.Div(id='encoding-steps')
        ], width=12)
    ])
])

@app.callback(
    Output('frequencies-result', 'children'),
    Input('set-frequencies-button', 'n_clicks'),
    State('input-frequencies', 'value')
)
def set_frequencies(n_clicks, input_frequencies):
    if n_clicks > 0:
        symbol_list = input_frequencies.split()
        freqs = Frequencies({s: symbol_list.count(s) for s in set(symbol_list)})
        frequency_dict = {s: freqs.frequency(s) for s in freqs.alphabet}
        return f"Frequencies: {frequency_dict}"
    return ""

@app.callback(
    Output('encoded-result', 'children'),
    Output('encoding-steps', 'children'),
    Input('encode-button', 'n_clicks'),
    State('input-frequencies', 'value'),
    State('input-sequence', 'value')
)
def encode_sequence(n_clicks, input_frequencies, input_sequence):
    if n_clicks > 0:
        symbol_list = input_frequencies.split()
        freqs = Frequencies({s: symbol_list.count(s) for s in set(symbol_list)})
        params = rANSParams(freqs)
        encoder = rANSEncoder(params)
        sequence = input_sequence.split()
        
        state = params.INITIAL_STATE
        encoding_steps = []
        
        for s in sequence:
            state = encoder.rans_base_encode_step(s, state)
            encoding_steps.append(f"Symbol: {s}, State: {state}")
        
        return f"Final State: {state}", html.Ul([html.Li(step) for step in encoding_steps])
    return "", ""

if __name__ == '__main__':
    app.run_server(debug=True)
