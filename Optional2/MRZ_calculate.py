from Crypto.Cipher import AES
from Crypto.Hash import SHA
import re, string, base64

def Odd_Even(ka):
    k = []
    for i in ka:
        if str(bin(int(i,16))[2:-1]).count('1')%2 == 0:
            k += [hex(int(str(bin(int(i,16))[2:-1])+'0',2)+1)[2:].zfill(2)]
        else:
            k += [hex(int(str(bin(int(i,16))[2:-1])+'0',2))[2:].zfill(2)]
            
    return ''.join(k)

def GetSHA1(D):
    h = SHA.new()
    h.update(D)
    return h.hexdigest()[:32]

    
C = '9MgYwmuPrjiecPMx61O6zIuy3MtIXQQ0E59T3xB6u0Gyf1gYs2i3K9Jxaa0zj4gTMazJuApwd6+jdyeI5iGHvhQyDHGVlAuYTgJrbFDrfB22Fpil2NfNnWFBTXyf7SDI'
C = base64.b64decode(C)

Visa = '12345678<8<<<1110182<1111167<<<<<<<<<<<<<<<4'
VisaNo = Visa[:9]
VVisa = Visa[9]
Nationality = Visa[10:13]
Birthday = Visa[13:19]
VBir = Visa[19]
Sex = Visa[20]
VisaEnd = Visa[21:27]
VVisaEnd = Visa[27]
Others = Visa[28:]

Info = VisaNo + VVisa + Birthday + VBir + VisaEnd + VVisaEnd
print Info

K_seed = GetSHA1(Info)

D = (K_seed + '0' * 7 + '1').decode('hex')

key = GetSHA1(D)

k1 = Odd_Even(re.findall('.{2}',key[:16]))
k2 = Odd_Even(re.findall('.{2}',key[16:]))

key = k1 + k2
print 'The key is:', key

cipher = AES.new(key.decode('hex'), AES.MODE_CBC, ('0'*32).decode('hex'))
print 'The M is:', cipher.decrypt(C)
