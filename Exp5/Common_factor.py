# -*- coding: cp936 -*-
'''n1 和n2具有相同的素因子'''
import re
import gmpy2
	
Data = []
for i in [1,18]:
    with open('Frame'+str(i)) as fp:
        data = re.findall('(.{256})(.{256})(.{256})',fp.read().replace('\n',''))
        Data += data
    
N = [int(n,16) for n,e,c in Data]
C = [int(c,16) for n,e,c in Data]
E = [int(e,16) for n,e,c in Data]
print N
print E
print C
p = gmpy2.gcd(N[0], N[1])

q1 = N[0] / p
q2 = N[1] / p

print 'p is:\n', p
print 'q1 is:\n', q1
print 'q2 is:\n', q2


print '{:x}'.format(pow(C[0],gmpy2.invert(E[0],(p-1)*(q1-1)),p*q1))
print '{:x}'.format(pow(C[1],gmpy2.invert(E[1],(p-1)*(q2-1)),p*q2))

print '{:x}'.format(pow(C[0],gmpy2.invert(E[0],(p-1)*(q1-1)),p*q1)).decode('hex')
print '{:x}'.format(pow(C[1],gmpy2.invert(E[1],(p-1)*(q2-1)),p*q2)).decode('hex')
