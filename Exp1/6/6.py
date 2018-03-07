# -*- coding: cp936 -*-
import re,pprint
from Crypto.Util import strxor
import base64

with open('6.txt','r') as fp:
    C=[base64.b64decode(i).encode('hex') for i in fp.readlines()]
    C=''.join(C)

G = []
for z in set(re.findall(r'(.{2})',C)): #2个一组
    loc = [0]+[s.start() for s in re.finditer(z, C)]
    G += [j-i for i,j in zip(loc,loc[1:])]

#分别计算能被1-40整除的距离数
pprint.pprint(sorted([(j,i) for (i,j) in [[i, sum([j for j in G if j%i==0 and j])] for i in range(1,41)]], reverse = True))

Score = 0

for Keylen in range(1,41):
    #Keylen = 29
    Key = ['*'] * Keylen

    #Keylen *2 个一组, 因为 2*hex = 1*str
    Csplit = [re.findall(r'(.{2})',z) for z in re.findall(r'(.{'+str(Keylen*2)+'})',C)]
    #转置
    Transpose = map(list,[zip(*Csplit)])[0]

    for i in range(Keylen):
        m = 0
        for k in range(255):
            #统计字母, 标点个数
            score = len(re.findall(r'[a-zA-Z ,\.;?!:]',''.join([strxor.strxor(c.decode('hex'), chr(k)) for c in Transpose[i]])))
            if m < score:
                m = score
                Key[i] = chr(k).encode('hex')

            
                
    key = str(''.join(Key).decode('hex'))*10000
    m = strxor.strxor(key[:len(C.decode('hex'))],C.decode('hex'))
    n = len(re.findall('[a-zA-Z]',m))
    if n>Score:
        Score = n
        M = m
        l = Keylen
        K = str(''.join(Key).decode('hex'))

#print Keylen
print 'The Key length is:', l
print 'The Key is:', K
print 'The M is:', M
