import itertools
import copy
from haraka import haraka512256

def header_hash(x):
    return verus_hash(x)

def verus_hash(x):
    length    = len(x)
    print "Input is length=", length
    hash      = ""
    pos       = 0
    buf       = [0] * 64
    print "buf=", buf
    for i in xrange(0,length):
        print "i=",i
        if i <= len(x):
            buf[i] = x[i]

    #buf       = x[0:31]
    high, low = x[:1], x[1:2]

    # put last result

    while True:
        if pos >= length:
            break
        if ( length - pos >= 32 ):
            # TODO copy 32 bytes, "full chunk"
            pass
        else:
            i = length - pos
            # TODO copy partial chunk and fill rest of buffer with zeros
        h = haraka512256(buf)

        # TODO: nextOffset stuff

        pos+= 32
    return hash
