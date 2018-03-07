from gmpy2 import *
import time, re
from random import randint
import multiprocessing

def Fermat(Q,n):
    a = isqrt_rem(n)[0]+1
    b = a ** 2 - n
    
    while 1:
        q = isqrt_rem(b)
        if q[1] == 0:
            Q.put([a - q[0], 'Fermat Done!', 'PollardRho killed', 'PollardRho p-1 killed!']) 
        
        a += 1
        b = a ** 2 - n

def PollardRho(Q, n):
    x = 2
    y = 2
    while 1:
        a = randint(1, n)
        while 1:
            x = (x**2+a)%n
            y = (((y**2+a)%n)**2+a)%n
            if x==y: break
            p = gcd(abs(x-y),n)
        
            if p>1:
                return Q.put([p, 'PollardRho Done!', 'Fermat killed', 'PollardRho p-1 killed!'])

def PollardRho_p_1(Q,N):
    a = i = 2
    while 1:
        a = pow(a, i, N)
        d = gcd(a - 1, N)
        if d != 1:
            Q.put([d, 'PollardRho p-1 Done!', 'PollardRho killed!', 'Fermat killed'])
        
        i += 1

if __name__ == "__main__":
    S = time.clock()
    Data = []
    N = []
    C = []
    E = []
    for i in [2, 6, 10, 14, 19]:
        with open('Frame'+str(i)) as fp:
            data = re.findall('(.{256})(.{256})(.{256})',fp.read().replace('\n',''))
            Data += data
    
    N = [int(n,16) for n,e,c in Data]
    C = [int(c,16) for n,e,c in Data]
    E = [int(e,16) for n,e,c in Data]
    
    for i in range(len(N)):
        s = time.clock()
        q = multiprocessing.Queue()
        n = N[i]
        p1 = multiprocessing.Process(target = Fermat, args = (q,n,))
        #p2 = multiprocessing.Process(target = PollardRho, args = (q,n,))
        p3 = multiprocessing.Process(target = PollardRho_p_1, args = (q,n,))
        p1.start()
        print '[!]Fermat Start...'
        #p2.start()
        #print '[!]PollardRho Start...'
        p3.start()
        print '[!]PollardRho p-1 Start...'
        
        f = q.get(True)
        if f:
            f1, f2 = f[0], n/f[0]
            print '[+]', f[1]
            print '  [x]', f[2]
            print '  [x]', f[3]
            print '  [-]Factor1:', f1
            print '  [-]Factor2:', f2
            p1.terminate()
            #p2.terminate()
            p3.terminate()
        
        phi = (f1 - 1) * (f2 - 1)
        d = invert(E[i], phi)
        print '  [-]d:', d
        M = pow(C[i], d, N[i])
        print M
        print '  [-]M:', ('%x' %M).decode('hex')
        print '[!]Timer', round(time.clock() - s, 2), 's'
        print '-'*50
    
    print '[!]All Done!'
    print '[!]Timer', round(time.clock() - S, 2), 's'