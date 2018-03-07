from Crypto.Util import strxor
m = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = "ICE"*1000
print strxor.strxor(m,key[:len(m)]).encode('hex')

