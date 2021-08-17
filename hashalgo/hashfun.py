import hashlib
import base64

def hashalgorithm(x):
    h = hashlib.sha256(x.encode('utf-8')).hexdigest()
    return h

def bsfenc(aadharnum):

    bsfnum = base64.b64encode(bytes(aadharnum, 'ascii'))
    bsfnum=bsfnum.decode('utf-8')
    return bsfnum

def bsfdec(bsfnum):

    aadharnum = base64.b64decode(bsfnum)
    aadharnum = aadharnum.decode('utf-8')
    return aadharnum


