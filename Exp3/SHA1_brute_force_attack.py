# -*- coding: cp936 -*-
import time
import multiprocessing
import itertools
import hashlib

def Func(C):
    return [c for c in itertools.permutations(C, 8) if hashlib.sha1(
        ''.join(c)).hexdigest() == '67ae1a64661ac8b4494666f58c4822408dd0a3e4']

def Check(s):
    return s[:3].count('0')>0 and s[3:].count('0')>0 #( I = * N 至少一个，% Q W 至少一个
    #return s.count('0')>1
    
if __name__ == "__main__":
    stime = time.clock()
    keyChars = [('Q', 'q'), ('W', 'w'), ('%', '5'), ('(', '8'),('=', '0'), ('I', 'i'), ('*', '+'), ('N', 'n')]
    Choose = filter(Check,[str(bin(i))[2:].zfill(8) for i in range(256)]) #列表过滤

    pool = multiprocessing.Pool()
    for res in [pool.apply_async(
            Func, ([keyChars[j][int(i[j])] for j in range(len(i))], )) for i in Choose]:
        
        if res.get() != []:
            print 'The key is:', ''.join(res.get()[0])
            
    print 'Timer:', round(time.clock() - stime, 2), 's'

