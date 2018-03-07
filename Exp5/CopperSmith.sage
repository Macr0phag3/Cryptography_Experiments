import re

def CopperSimth(message, e, c, n):
    ZmodN = Zmod(n)
    c = ZmodN(c)
    message = ZmodN(message)
    P.<x> = PolynomialRing(ZmodN)
    pol = ((message + x) ^ e) - c
    pol = pol.monic()
    xval = pol.small_roots(epsilon=1/11)
    if len(xval): return '%x' %(message + xval[0])
    return 0

Data = []
N = []
C = []
E = []
for i in [7, 11, 15]:
    with open('Frame'+str(i)) as fp:
        data = re.findall('(.{256})(.{256})(.{256})',fp.read().replace('\n',''))
        Data += data

N = [int(n,16) for n,e,c in Data]
C = [int(c,16) for n,e,c in Data]
E = [int(e,16) for n,e,c in Data]

for id in range(len(N)):
	n = N[id]
	e = E[id]
	c = C[id]
	print '[+]n:', n
	print '[+]e:', e
	for i in xrange(17):
	    rmessage = '9876543210abcdef0000000%s00000000000000000000000000000000000000000000000000000000000000000000000000000000000000005858585858585858' %i
	    message = int(rmessage,16)

	    recover = CopperSimth(message, e, c, n)
	    if recover:
	    	print '  [-]m:', recover
	print '-' * 50
print '[!]All Done!'