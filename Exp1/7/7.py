from Crypto.Cipher import AES
import base64, re

with open('7.txt') as fp:
    C = [base64.b64decode(i.replace('\n','')) for i in fp.readlines()]
    C = ''.join(C)

key = "YELLOW SUBMARINE"
cipher = AES.new(key, AES.MODE_ECB)
m = cipher.decrypt(C)
print m
