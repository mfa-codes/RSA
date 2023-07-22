from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

class RSAAlgo:
    def __init__(self, msg):
        self.msg = msg
        self.encryptedmsg = None
        self.keyPair = RSA.generate(1024)

    

    def RSAEncrypt(self):
        pubKey = self.keyPair.publickey()
        encryptor = PKCS1_OAEP.new(pubKey)
        encryptedMSG = encryptor.encrypt(self.msg.encode('utf8')) # enocde('ascii')
        self.encryptedmsg = encryptedMSG

    def RSADencrypt(self):
        decryptor = PKCS1_OAEP.new(self.keyPair)
        decryptedMSG = decryptor.decrypt(self.encryptedmsg).decode('utf8')
        return decryptedMSG
