# -*- coding: cp936 -*-
import re 
import gmpy2
import time

Data = []
for i in [0,4]:
    with open('Frame'+str(i)) as fp:
        data = re.findall('(.{256})(.{256})(.{256})',fp.read().replace('\n',''))
        Data += data

print '[+]Common modulus attack'
N = [int(n,16) for n,e,c in Data]
C = [int(c,16) for n,e,c in Data]
E = [int(e,16) for n,e,c in Data]

n = N[0]
c1 = C[0]
c2 = C[1]

e1 = E[0]
e2 = E[1]

s = gmpy2.gcdext(min(e1, e2), max(e1, e2))

s1 = s[1]
s2 = s[2]

# 求模反元素
if s1 < 0:
    s1 = -s1
    c1 = gmpy2.invert(c1, n)

if s2 < 0:
    s2 = -s2
    c2 = gmpy2.invert(c2, n)

m = pow(c1, s1, n) * pow(c2, s2, n) % n
print '  [-]m is:' + '{:x}'.format(int(m))
print '  [-]m is:' + '{:x}'.format(int(m)).decode('hex')
print '\n[!]Timer:', round(time.clock(),2), 's'
print '[!]All Done!'
