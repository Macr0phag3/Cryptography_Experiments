import re
with open("4.txt") as fp:
  C = [i.replace("\n","") for i in fp.readlines()]

score = 0

for i in C:
    for k in range(0,255):
        m = []
        for j in re.findall(".{2}",i):
            m += [chr(k^int(j,16))]
        
        mm = "".join(m)
        nn = len(re.findall("[a-z]",mm))

        if nn > score:
            score = nn
            c = i
            M = mm
            key = chr(k)

print 'The C is:', c
print 'The key is:', key
print 'The M is:', M
            
