import re
c = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
score = 0
for k in range(0,255):
    m = []
    for j in re.findall(".{2}",c):
        m += [chr(k^int(j,16))]
        
    mm = "".join(m)
    nn = len(re.findall("[a-zA-Z]",mm))
    if nn > score:
        score = nn
        M = mm
        key = chr(k)
        
print 'The key is:', key
print 'The M is:', M
            

