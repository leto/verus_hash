import itertools
import copy
import haraka

def header_hash(x):
    return verus_hash(x)

def verus_hash(x):
    len  = x.length()
    hash = ""
    pos  = 0
    buf  = ""

    # put last result

    while True:
        if pos >= len
            break
        if( len - pos >= 32 )
            # TODO copy 32 bytes, "full chunk"
        else
            i = len - pos
            # TODO copy partial chunk and fill rest of buffer with zeros
        h = haraka512(buf2,buf)

        # TODO: nextOffset stuff

        pos+= 32
    return hash