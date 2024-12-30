import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from rANSv1 import rANS_encoder, rANS_decoder

app = dash.Dash(__name__)
app.title = "rANS Encoder and Decoder"

app.layout = html.Div([

    # Encoder
    html.H1("rANS Encoder", style={'textAlign': 'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Label("Symbol Counts:"),
                dcc.Input(
                    id='input-symbols',
                    type='text',
                    placeholder='Enter symbols separated by commas, e.g., 3,1,2',
                    value='1,3',
                    style={'width': 100, 'height': 30, 'marginBottom': 20},
                ),
            ], style={'width': '48%', 'display': 'inline-block'}),
            html.Div([
                html.Label("Input Sequence:"),
                dcc.Input(
                    id='input-sequence',
                    type='text',
                    placeholder='Enter sequence separated by commas, e.g., 0,1,0,2',
                    value='1,0,1,1,1,0',
                    style={'width': 100, 'height': 30, 'marginBottom': 20}
                ),
            ], style={'width': '48%', 'display': 'inline-block', 'marginLeft': '4%'}),
        ], style={'width': '50%', 'margin': 'auto'}),
    ], style={'width': '50%', 'margin': 'auto'}),
    html.Div([
        html.Button('Encode', id='encode-button', n_clicks=0, style={'marginRight': 10}),
    ], style={'textAlign': 'center', 'marginTop': 20}),
    html.Div(id='encoded-output', style={'marginTop': 20, 'textAlign': 'center'}),

    # Decoder
    html.H1("rANS Decoder", style={'textAlign': 'center'}),
    html.Div([
        html.Label("Symbol Counts:"),
        dcc.Input(
            id='decode-symbols',
            type='text',
            placeholder='Enter symbols separated by commas, e.g., 3,1,2',
            value='1,3',
            style={'width': '100%', 'marginBottom': 20}
        ),
        html.Label("Final State:"),
        dcc.Input(
            id='final-state',
            type='number',
            placeholder='Enter final state, e.g., 7',
            value=52,
            style={'width': '100%', 'marginBottom': 20}
        ),
        html.Button('Decode', id='decode-button', n_clicks=0),
    ], style={'width': '50%', 'margin': 'auto'}),
    html.Div(id='decoded-output', style={'marginTop': 20, 'textAlign': 'center'}),

    # Steaming Encoder
    html.H1("rANS Streaming Encoder", style={'textAlign': 'center'}),

    # Steaming Decoder
    html.H1("rANS Streaming Decoder", style={'textAlign': 'center'}),
])

@app.callback(
    Output('encoded-output', 'children'),
    Input('encode-button', 'n_clicks'),
    State('input-symbols', 'value'),
    State('input-sequence', 'value')
)
def encode(n_clicks, symbols, sequence):
    if n_clicks > 0:
        symbol_counts = list(map(int, symbols.split(',')))
        s_input = list(map(int, sequence.split(',')))
        encoded, state, L_avg, entropy = rANS_encoder(symbol_counts, s_input)
        
        table_rows = [html.Tr([html.Th("Input Symbol"), html.Th("State")])]
        for symbol, state in encoded:
            table_rows.append(html.Tr([html.Td(symbol), html.Td(state)]))
        
        return html.Div([
            html.H3("Encoded Output"),
            html.Table(table_rows, style={'width': '50%', 'margin': 'auto', 'border': '1px solid black'}),
            html.P(f'Final State: {state}'),
            html.P(f'Number of Input Symbols: {len(s_input)}'),
            html.P(f'Average Code Length: {L_avg}'),
            html.P(f'Entropy: {entropy}')
        ])
    return ''

@app.callback(
    Output('decoded-output', 'children'),
    Input('decode-button', 'n_clicks'),
    State('decode-symbols', 'value'),
    State('final-state', 'value')
)
def decode(n_clicks, symbols, final_state):
    if n_clicks > 0:
        symbol_counts = list(map(int, symbols.split(',')))
        # num_symbols = int(num_symbols)
        final_state = int(final_state)
        decoded, _ = rANS_decoder(symbol_counts, final_state)
        
        table_rows = [html.Tr([html.Th("State"), html.Th("Output Symbol")])]
        for symbol, state in decoded:
            table_rows.append(html.Tr([html.Td(state), html.Td(symbol)]))
        
        output_symbols = [symbol for symbol, state in decoded][::-1]

        return html.Div([
            html.H3("Decoded Output"),
            html.Table(table_rows, style={'width': '50%', 'margin': 'auto', 'border': '1px solid black'}),
            html.P(f'Output Symbols: {output_symbols}')
        ])
    return ''

if __name__ == '__main__':
    app.run_server(debug=True)
