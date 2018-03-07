from Crypto.Cipher import DES3
import re

with open('1.txt','rb') as fp:
    data = ''.join(fp.read().split())

print len(data)
N = 0
for k in range(999999):
    iv = str(k).zfill(6)
    key = 'COPACOBANA'+iv
    cipher = DES3.new(key, DES3.MODE_CBC, IV=('0'*16).decode('hex'))
    m = cipher.decrypt(data.decode('hex')[:2352])
    n = len(re.findall('[a-zA-Z]',m))
    if N < n:
        N = n
        M = m
        K = key

        print 'The key is:',K
        print 'The M is:',M
        print '+'*50
                

