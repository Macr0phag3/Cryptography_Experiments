import difflib
from math import ceil
import base64
import re

with open('6.txt','r') as fp:
    C=[base64.b64decode(i).encode('hex') for i in fp.readlines()]
    C=''.join(C)
print len(C)
L = 10000
for Keylen in range(1,41):
    CC = re.findall('.{'+str(Keylen*2)+'}', C)
    
    Hm = 0
    for c in range(len(CC)):
        for cc in range(c+1,len(CC)):
            diff = difflib.SequenceMatcher(None, str(bin(int(CC[c],16))), str(bin(int(CC[cc],16)))).ratio()
            Hm += int(ceil((1-diff)*(len(str(bin(int(CC[c],16))))-2)))
        #print c
    print Keylen,Hm
    if L>Hm:
        L = Hm
        keysize = Keylen
        
print L
print keysize
        
#diff = difflib.SequenceMatcher(None, b1, b2).ratio()

#print diff
#print int(ceil((1-diff)*len(b1)))
