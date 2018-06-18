import itertools
import copy
from haraka import haraka512256

def header_hash(x):
    return verus_hash(x)

def verus_hash(x):
    len       = x.length()
    hash      = ""
    pos       = 0
    buf       = x[0:31]
    high, low = x[:1], x[1:2]

    # put last result

    while True:
        if pos >= len
            break
        if( len - pos >= 32 )
            # TODO copy 32 bytes, "full chunk"
        else
            i = len - pos
            # TODO copy partial chunk and fill rest of buffer with zeros
        h = haraka512256(buf)

        # TODO: nextOffset stuff

        pos+= 32
    return hash
