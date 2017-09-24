import re 
with open('8.txt','r') as fp:
    C = [i.replace('\n','') for i in fp.readlines()]

for ECB in C:
    block = re.findall('.{16}',ECB)
    if len(block) - len(set(block)):
        print ECB
