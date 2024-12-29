"""
EE274 Version: https://stanforddatacompressionclass.github.io/notes/lossless_iid/ans.html
"""
# Base encoder and decoder

####### Encoding ###########
def rans_base_encode_step(x,s):
    x_next = (x//freq[s])*M + cumul[s] + x%freq[s]
    return x_next

def rans_base_encode(symbols):
    x = 0 # initial state
    for s in symbols:
        x = rans_base_encode_step(x,s)
    
    return to_binary(x)  # convert final state to bits

####### Decoding ###########
def rans_base_decode_step(x):
    # Step I: find block_id, slot
    block_id = x//M
    slot = x%M
    
    # Step II: Find symbol s
    s = find_bin(cumul_array, slot) 
    
    # Step III: retrieve x_prev
    x_prev = block_id*freq[s] + slot - cumul[s]

    return (s,x_prev)

def rans_base_decode(bits, num_symbols):
    x = to_uint(bits) # convert bits to final state

    # main decoding loop
    symbols = []
    for _ in range(num_symbols):
        s, x = rans_base_decode_step(x)
        symbols.append(s)
    return reverse(symbols) # need to reverse to get original sequence


# Streaming rANS
# Encoding

def shrink_state(x,s):
    # initialize the output bitarray
    out_bits = BitArray()

    # shrink state until we are sure the encoded state will lie in the correct interval
    while rans_base_encode_step(x,s) not in Interval[L,H]:
        out_bits.prepend(x%2)
        x = x//2
    x_shrunk = x
    return x_shrunk, out_bits

def rans_stream_encode_step(x,s):
    # shrink state x before calling base encode
    x_shrunk, out_bits = shrink_state(x, s)

    # perform the base encoding step
    x_next = rans_base_encode_step(x_shrunk,s)
    
    return x_next, out_bits

def rans_stream_encode(symbols):
    """
    Encodes a sequence of symbols using rANS.
    
    """
    x = L # initial state
    encoded_bitarray = BitArray()
    for s in symbols:
        x, out_bits = rans_stream_encode_step(x,s)

        # note that after the encode step, x lies in the interval [L,H]
        assert x in Interval[L,H]
        
        # add out_bits to output
        encoded_bitarray.prepend(out_bits)
    
    # add the final state at the beginning
    num_state_bits = ceil(log2(H))
    encoded_bitarray.prepend(to_binary(x, num_state_bits))
    return encoded_bitarray


# Steaming Decoder
def expand_state(x_shrunk, enc_bitarray):
    # init
    num_bits_step = 0

    # read in bits to expand x_shrunk -> x
    x = x_shrunk
    while x not in Interval[L,H]:
        x = x*2 + enc_bitarray[num_bits_step]
        num_bits_step += 1
    return x, num_bits_step

def rans_stream_decode_step(x, enc_bitarray):
    # decode s, retrieve prev state
    s, x_shrunk = rans_base_decode_step(x)

    # expand back x_shrunk to lie in Interval[L,H]
    x_prev, num_bits_step = expand_state(x_shrunk, enc_bitarray)
    return s, x_prev, num_bits_step

def rans_stream_decode(encoded_bitarray, num_symbols):
    # initialize counter of bits read from the encoded_bitarray
    num_bits_read = 0

    # read the final state 
    num_state_bits = ceil(log2(H))
    x = to_uint(encoded_bitarray[:num_state_bits])
    num_bits_read += num_state_bits

    # main decoding loop
    symbols = []
    for _ in range(num_symbols):
        # decoding step
        s, x, num_bits_step = rans_stream_decode_step(x, encoded_bitarray[num_bits_read:])
        symbols.append(s)

        # update num_bits_read counter
        num_bits_read += num_bits_step
    return reverse(symbols) # need to reverse to get original sequence