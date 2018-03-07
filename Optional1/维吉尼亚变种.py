# -*- coding: cp936 -*-
import re,pprint
from Crypto.Util import strxor

C = 'F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CA\
B1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5\
B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC\
931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963\
FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EF\
D9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF59\
23AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA3\
6ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CE\
D5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85\
A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C\
96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794'

G = []
for z in set(re.findall(r'(.{2})',C)): #2个一组
    loc = [0]+[s.start() for s in re.finditer(z, C)]
    G += [j-i for i,j in zip(loc,loc[1:])]
    #print z,loc

#分别计算能被1-13整除的距离数
pprint.pprint(sorted([(j,i) for (i,j) in [[i, sum([j for j in G if j%i==0 and j])] for i in range(1,14)]], reverse = True))

#7较特殊, 在结果里却排名靠前, 说明Keylen很有可能是7
for Keylen in range(1,14):
    #Keylen = 7
    Key = ['*'] * Keylen

    #14个一组
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

    print 'Key:',''.join(Key)
    Key = str(''.join(Key).decode('hex'))*1000
    print 'M:',strxor.strxor(Key[:len(C.decode('hex'))],C.decode('hex'))
    #134 time pad
