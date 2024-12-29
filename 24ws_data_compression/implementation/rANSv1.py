"""
this module implements the rANS and tANS algorithms for entropy coding
the original code is from Kedar Tatwawadi: https://github.com/kedartatwawadi/post--ANS/blob/master/public/rANS.js, base on the code in js file, I implement the rANS and tANS algorithms in Python
"""

import math
from bisect import bisect_right

def entropy(symbol_counts):
    H = 0
    counts_sum = sum(symbol_counts)
    
    for count in symbol_counts:
        H += (count / counts_sum) * math.log(counts_sum / count)
    
    H = H / math.log(2.0)
    return H

def rANS_encoder(symbol_counts, s_input):
    # compute cumulative frequencies
    cumul_counts = []
    sum_counts = 0
    for count in symbol_counts:
        cumul_counts.append(sum_counts)
        sum_counts += count
    
    state = 0
    output = []
    for s in s_input:
        Fs = symbol_counts[s]
        Cs = cumul_counts[s]
        state = (state // Fs) * sum_counts + Cs + (state % Fs)
        output.append((s, state))
    
    L_avg = math.ceil(math.log(state) / math.log(2.0)) / len(s_input)
    return output, state, L_avg, entropy(symbol_counts)

def rANS_decoder(symbol_counts, num_symbols, state):
    """
    rANS Decoder: Decodes a sequence of symbols from an rANS-compressed state.

    Args:
        symbol_counts (list): A list of frequencies for each symbol.
        num_symbols (int): The number of symbols to decode.
        state (int): The final state from which to decode.

    Returns:
        output (list): A list of decoded symbols.
        state (int): The remaining state after decoding all symbols.
    """
    # Compute cumulative frequencies
    cumul_counts = [0]  # Start with 0 as the first cumulative frequency
    total_frequency = sum(symbol_counts)
    for count in symbol_counts:
        cumul_counts.append(cumul_counts[-1] + count)

    def c_inv(y):
        """
        Binary search to find the symbol corresponding to the given slot.
        y: Slot value (state % total_frequency).
        Returns: Decoded symbol index.
        """
        return bisect_right(cumul_counts, y) - 1

    # Decoding process
    output = []  # List to store decoded symbols
    for _ in range(num_symbols):
        slot = state % total_frequency  # Find the slot in the cumulative frequency range
        s = c_inv(slot)                 # Get the symbol corresponding to the slot
        Fs = symbol_counts[s]           # Frequency of the symbol
        Cs = cumul_counts[s]            # Cumulative count of the symbol
        output.append((s,state))                # Append decoded symbol to the output
        state = (state // total_frequency) * Fs + (slot - Cs)  # Update the state

    return output, state

def rANS_streaming_encoder(symbol_counts, s_input):
    # compute cumulative frequencies
    cumul_counts = []
    sum_counts = 0
    for count in symbol_counts:
        cumul_counts.append(sum_counts)
        sum_counts += count
    
    state = sum_counts
    rANS_stream = ""
    output = []
    for s in s_input:
        Fs = symbol_counts[s]
        Cs = cumul_counts[s]

        out_bits = ""
        while state >= 2 * Fs:
            out_bits += str(state % 2)
            state //= 2
        state = (state // Fs) * sum_counts + Cs + (state % Fs)
        rANS_stream += out_bits
        output.append((s, state, out_bits))
    
    L_avg = (math.ceil(math.log(state) / math.log(2.0)) + len(rANS_stream)) / len(s_input)
    return output, state, rANS_stream, L_avg, entropy(symbol_counts)

def rANS_streaming_decoder(symbol_counts, num_symbols, state, rANS_stream):
    # compute cumulative frequencies
    cumul_counts = []
    sum_counts = 0
    for count in symbol_counts:
        cumul_counts.append(sum_counts)
        sum_counts += count
    
    def c_inv(y):
        for i in range(len(cumul_counts) - 1, -1, -1):
            if y >= cumul_counts[i]:
                return i
        return 0

    output = []
    rANS_stream = list(map(int, rANS_stream))
    for _ in range(num_symbols):
        slot = state % sum_counts
        s = c_inv(slot)
        Fs = symbol_counts[s]
        Cs = cumul_counts[s]
        output.append((s, state))
        state = (state // sum_counts) * Fs + slot - Cs

        while state < sum_counts:
            state = state * 2 + rANS_stream.pop()
    
    return output, state

def tANS_encoder(symbol_counts):
    # compute cumulative frequencies
    cumul_counts = []
    sum_counts = 0
    for count in symbol_counts:
        cumul_counts.append(sum_counts)
        sum_counts += count
    
    output_state = []
    output_bits = []
    for state in range(sum_counts, 2 * sum_counts):
        state_row = [state]
        bits_row = [state]
        for s in range(len(symbol_counts)):
            Fs = symbol_counts[s]
            Cs = cumul_counts[s]

            out_bits = ""
            out_state = state
            while out_state >= 2 * Fs:
                out_bits += str(out_state % 2)
                out_state //= 2
            out_state = (out_state // Fs) * sum_counts + Cs + (out_state % Fs)
            
            state_row.append(out_state)
            bits_row.append(out_bits)
        output_state.append(state_row)
        output_bits.append(bits_row)
    
    return output_state, output_bits

def tANS_decoder(symbol_counts):
    # compute cumulative frequencies
    cumul_counts = []
    sum_counts = 0
    for count in symbol_counts:
        cumul_counts.append(sum_counts)
        sum_counts += count
    
    def c_inv(y):
        for i in range(len(symbol_counts)):
            if y < cumul_counts[i]:
                break
        return i - 1

    decoder_table = []
    for state in range(sum_counts, 2 * sum_counts):
        state_row = [state]
        for s in range(len(symbol_counts)):
            count = symbol_counts[s]
            symbol = chr(65 + s)
            for _ in range(count):
                state_row.append(symbol)
        decoder_table.append(state_row)
    
    return decoder_table


# Example symbol frequencies
symbol_counts = [1, 3]  # P(0) = 1/4, P(1) = 3/4
num_symbols = 6         # Number of symbols to decode
state = 52              # Final state after encoding

# Decode symbols
decoded_symbols, final_state = rANS_decoder(symbol_counts, num_symbols, state)
print("Decoded symbols:", decoded_symbols)
print("Remaining state:", final_state)

