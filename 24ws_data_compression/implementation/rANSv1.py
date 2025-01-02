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
    """
    rANS Encoder: Encodes a sequence of symbols using rANS.
    Input:  symbol_counts - A list of frequencies for each symbol.
            s_input - A list of symbols to encode.
    Output: output - A list of tuples containing the encoded symbol and the state.
    """
    # compute cumulative frequencies
    cumul_freq = [] # c_s
    sum_freq = 0 # m
    x = 0 # initial state
    output = [] # list to store encoded (symbols, state)

    for count in symbol_counts:
        cumul_freq.append(sum_freq)
        sum_freq += count
    for s in s_input:
        F_s = symbol_counts[s]
        c_s = cumul_freq[s]
        x = sum_freq * (x // F_s) + (x % F_s) + c_s
        output.append((s, x))
    
    L_avg = math.ceil(math.log(x) / math.log(2.0)) / len(s_input)
    return output, x, L_avg, entropy(symbol_counts)

def rANS_decoder(symbol_counts, x):
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
    cumul_freq = []  # c_s
    sum_freq = 0 # m
    output = []  # List to store decoded symbols and states

    # compute m and c_s
    for count in symbol_counts:
        cumul_freq.append(sum_freq)
        sum_freq += count
    # def c_inv(y):
    #     """
    #     Binary search to find the symbol corresponding to the given slot.
    #     y: Slot value (state % total_frequency).
    #     Returns: Decoded symbol index.
    #     """
    #     return bisect_right(cumul_freq, y) - 1
    # Decoding process
    # for _ in range(num_symbols):
    while x > 0:
        slot = x % sum_freq  # Find the slot in the cumulative frequency range
        s = bisect_right(cumul_freq, slot) - 1 # Binary search to find the symbol corresponding to the given slot.
        F_s = symbol_counts[s]         # Frequency of the symbol
        c_s = cumul_freq[s]            # Cumulative count of the symbol
        output.append((s,x))           # Append decoded symbol to the output
        x = (x // sum_freq) * F_s + x % sum_freq - c_s  # Update the state
    return output, x


def rANS_stream_encoder(symbol_counts, s_input):
    # compute cumulative frequencies c_s and total frequency m
    cumul_freq = []
    sum_freq = 0
    for count in symbol_counts:
        cumul_freq.append(sum_freq)
        sum_freq += count
    
    x = sum_freq  # why x = sum_freq not 0?
    bit_stream = ""
    output = []
    maxX_s = [] # how to compute maxX_s
    L_s = 0

    for s in s_input:
        F_s = symbol_counts[s]
        c_s = cumul_freq[s]
        L_s = F_s # k = 1
        maxX_s = 2 * L_s - 1
        out_bits = ""

        while x > maxX_s:
            out_bits += str(x % 2)
            x = x // 2
        x = (x // F_s) * sum_freq + (x % F_s) + c_s
        bit_stream += out_bits
        output.append((s, x, out_bits, bit_stream))
    
    L_avg = (math.ceil(math.log(x) / math.log(2.0)) + len(bit_stream)) / len(s_input)
    return output, x, bit_stream, L_avg, entropy(symbol_counts)

def rANS_stream_decoder(symbol_counts, x, bit_stream, num_symbols):
    # compute cumulative frequencies
    cumul_freq = [] # c_s
    sum_freq = 0 # m
    for count in symbol_counts:
        cumul_freq.append(sum_freq)
        sum_freq += count

    output = []
    bit_stream = list(map(int, bit_stream.split(',')))  # Convert bit_stream to a list of integers
    for _ in range(num_symbols):
        slot = x % sum_freq
        s = bisect_right(cumul_freq, slot) - 1
        F_s = symbol_counts[s]
        c_s = cumul_freq[s]
        output.append((s, x))
        x = (x // sum_freq) * F_s + slot - c_s

        while x < sum_freq and len(bit_stream) > 0: 
            x = x * 2 + bit_stream.pop()
    
    return output, x

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
            F_s = symbol_counts[s]
            c_s = cumul_counts[s]

            out_bits = ""
            out_state = state
            while out_state >= 2 * F_s:
                out_bits += str(out_state % 2)
                out_state //= 2
            out_state = (out_state // F_s) * sum_counts + c_s + (out_state % F_s)
            
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
x = 4              # Final state after encoding
bit_stream = "0,1,0,1,1"   # Bit stream
num_symbols = 6

# Decode symbols
output, x_i = rANS_stream_decoder(symbol_counts, x, bit_stream, num_symbols)
print("Decoded symbols:", output)
print("Remaining state:", x_i)

