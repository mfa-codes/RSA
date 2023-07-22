from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

class RSAFile:
    def __init__(self):
        self.msg = None
        self.encryptedmsg = None
        self.keyPair = RSA.generate(1024)

    def choiceFile(self):
        line = ""
        print('File content:')
        with open("testFile.txt", "r") as file:
            for line in file:
                print(str(line))
        file.close()
        self.msg = line

    def RSAEncrypt(self):
        pubKey = self.keyPair.publickey()
        encryptor = PKCS1_OAEP.new(pubKey)
        self.choiceFile()
        encryptedMSG = encryptor.encrypt(self.msg.encode('utf8')) # enocde('ascii')
        self.encryptedmsg = encryptedMSG

    def RSADencrypt(self):
        decryptor = PKCS1_OAEP.new(self.keyPair)
        decryptedMSG = decryptor.decrypt(self.encryptedmsg).decode('utf8')
        return decryptedMSG

    def main():
        rsa = RSAFile()
        rsa.RSAEncrypt()
        denMSG = rsa.RSADencrypt()
        print(f"The MSG after dencrypting: {denMSG}")
        

if __name__ == '__main__':
    RSAFile.main()
