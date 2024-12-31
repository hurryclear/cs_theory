import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from rANSv1 import rANS_encoder, rANS_decoder, rANS_stream_encoder, rANS_stream_decoder

app = dash.Dash(__name__)
app.title = "rANS Encoder and Decoder"

app.layout = html.Div([

    # Base Encoder
    html.H1("rANS Encoder", style={'textAlign': 'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Label("Symbol Counts:"),
                dcc.Input(
                    id='base-input-symbols',
                    type='text',
                    placeholder='Enter symbols separated by commas, e.g., 3,1,2',
                    value='1,3',
                    style={'width': 100, 'height': 30, 'marginBottom': 20},
                ),
            ], style={'width': '48%', 'display': 'inline-block'}),
            html.Div([
                html.Label("Input Sequence:"),
                dcc.Input(
                    id='base-input-sequence',
                    type='text',
                    placeholder='Enter sequence separated by commas, e.g., 0,1,0,2',
                    value='1,0,1,1,1,0',
                    style={'width': 100, 'height': 30, 'marginBottom': 20}
                ),
            ], style={'width': '48%', 'display': 'inline-block', 'marginLeft': '4%'}),
        ], style={'width': '50%', 'margin': 'auto'}),
    ], style={'width': '50%', 'margin': 'auto'}),
    html.Div([
        html.Button('Encode', id='base-encode-button', n_clicks=0, style={'marginRight': 10}),
    ], style={'textAlign': 'center', 'marginTop': 20}),
    html.Div(id='base-encoded-output', style={'marginTop': 20, 'textAlign': 'center'}),

    # Base Decoder
    html.H1("rANS Decoder", style={'textAlign': 'center'}),
    html.Div([
        html.Label("Symbol Counts:"),
        dcc.Input(
            id='base-decode-symbols',
            type='text',
            placeholder='Enter symbols separated by commas, e.g., 3,1,2',
            value='1,3',
            style={'width': '100%', 'marginBottom': 20}
        ),
        html.Label("Final State:"),
        dcc.Input(
            id='base-final-state',
            type='number',
            placeholder='Enter final state, e.g., 7',
            value=52,
            style={'width': '100%', 'marginBottom': 20}
        ),
        html.Button('Decode', id='base-decode-button', n_clicks=0),
    ], style={'width': '50%', 'margin': 'auto'}),
    html.Div(id='base-decoded-output', style={'marginTop': 20, 'textAlign': 'center'}),

    # Streaming Encoder
    html.H1("rANS Streaming Encoder", style={'textAlign': 'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Label("Symbol Counts:"),
                dcc.Input(
                    id='stream-input-symbols',
                    type='text',
                    placeholder='Enter symbols separated by commas, e.g., 3,1,2',
                    value='1,3',
                    style={'width': 100, 'height': 30, 'marginBottom': 20},
                ),
            ], style={'width': '48%', 'display': 'inline-block'}),
            html.Div([
                html.Label("Input Sequence:"),
                dcc.Input(
                    id='stream-input-sequence',
                    type='text',
                    placeholder='Enter sequence separated by commas, e.g., 0,1,0,2',
                    value='1,0,1,1,1,0',
                    style={'width': 100, 'height': 30, 'marginBottom': 20}
                ),
            ], style={'width': '48%', 'display': 'inline-block', 'marginLeft': '4%'}),
        ], style={'width': '50%', 'margin': 'auto'}),
    ], style={'width': '50%', 'margin': 'auto'}),
    html.Div([
        html.Button('Encode', id='stream-encode-button', n_clicks=0, style={'marginRight': 10}),
    ], style={'textAlign': 'center', 'marginTop': 20}),
    html.Div(id='stream-encoded-output', style={'marginTop': 20, 'textAlign': 'center'}),

    # Streaming Decoder
    html.H1("rANS Streaming Decoder", style={'textAlign': 'center'}),
    html.Div([
        html.Label("Symbol Counts:"),
        dcc.Input(
            id='stream-decode-symbols',
            type='text',
            placeholder='Enter symbols separated by commas, e.g., 3,1,2',
            value='1,3',
            style={'width': '100%', 'marginBottom': 20}
        ),
        html.Label("Final State:"),
        dcc.Input(
            id='stream-final-state',
            type='number',
            placeholder='Enter final state, e.g., 7',
            value=4,
            style={'width': '100%', 'marginBottom': 20}
        ),
        html.Label("Bit Stream:"),
        dcc.Input(
            id='stream-bit-stream',
            type='text',
            placeholder='Bit Stream',
            value='0,1,0,1,1',
            style={'width': '100%', 'marginBottom': 20}
        ),
        html.Label("Number of Symbols:"),
        dcc.Input(
            id='stream-num-symbols',
            type='number',
            placeholder='Number of Symbols',
            value=6,
            style={'width': '100%', 'marginBottom': 20}
        ),
        html.Button('Decode', id='stream-decode-button', n_clicks=0),
    ], style={'width': '50%', 'margin': 'auto'}),
    html.Div(id='stream-decoded-output', style={'marginTop': 20, 'textAlign': 'center'}),
])

@app.callback(
    Output('base-encoded-output', 'children'),
    Input('base-encode-button', 'n_clicks'),
    State('base-input-symbols', 'value'),
    State('base-input-sequence', 'value')
)
def base_encode(n_clicks, symbols, sequence):
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
    Output('base-decoded-output', 'children'),
    Input('base-decode-button', 'n_clicks'),
    State('base-decode-symbols', 'value'),
    State('base-final-state', 'value')
)
def base_decode(n_clicks, symbols, final_state):
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

@app.callback(
    Output('stream-encoded-output', 'children'),
    Input('stream-encode-button', 'n_clicks'),
    State('stream-input-symbols', 'value'),
    State('stream-input-sequence', 'value')
)
def stream_encode(n_clicks, symbols, sequence):
    if n_clicks > 0:
        symbol_counts = list(map(int, symbols.split(',')))
        s_input = list(map(int, sequence.split(',')))
        output, state, rANS_stream_final, L_avg, entropy = rANS_stream_encoder(symbol_counts, s_input)
        
        table_rows = [html.Tr([html.Th("Input Symbol"), html.Th("State"), html.Th("Streamed Out Bits"), html.Th("Bit Stream")])]
        for symbol, state, out_bits, rANS_stream in output:
            table_rows.append(html.Tr([html.Td(symbol), html.Td(state), html.Td(out_bits), html.Td(rANS_stream)]))
        
        return html.Div([
            html.H3("Encoded Output"),
            html.Table(table_rows, style={'width': '50%', 'margin': 'auto', 'border': '1px solid black'}),
            html.P(f'Final State: {state}'),
            html.P(f'Number of Input Symbols: {len(s_input)}'),
            html.P(f'Bit Stream: {",".join(map(str, rANS_stream_final))}'),
            html.P(f'Average Code Length: {L_avg}'),
            html.P(f'Entropy: {entropy}')
        ])
    return ''


@app.callback(
    Output('stream-decoded-output', 'children'),
    Input('stream-decode-button', 'n_clicks'),
    State('stream-decode-symbols', 'value'),
    State('stream-final-state', 'value'),
    State('stream-bit-stream', 'value'),
    Input('stream-num-symbols', 'value'),
)
def stream_decode(n_clicks, symbols, final_state, bit_stream, num_symbols):
    if n_clicks > 0:
        symbol_counts = list(map(int, symbols.split(',')))
        # num_symbols = int(num_symbols)
        final_state = int(final_state)
        decoded, _ = rANS_stream_decoder(
            symbol_counts, final_state, bit_stream, num_symbols)
        
        table_rows = [html.Tr([html.Th("State"), html.Th("Output Symbol")])]
        for symbol, x in decoded:
            table_rows.append(html.Tr([html.Td(x), html.Td(symbol)]))
        
        output_symbols = [symbol for symbol, state in decoded][::-1]

        return html.Div([
            html.H3("Decoded Output"),
            html.Table(table_rows, style={'width': '50%', 'margin': 'auto', 'border': '1px solid black'}),
            html.P(f'Output Symbols: {output_symbols}')
        ])
    return ''


if __name__ == '__main__':
    app.run_server(debug=True)
