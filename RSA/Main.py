import RSA

class Main:
    def main():
        userInputMSG = input('Please enter the msg hier\n>>> ')
        rsa = RSA.RSAAlgo(userInputMSG)
        rsa.RSAEncrypt()
        denMSG = rsa.RSADencrypt()
        print(f"Your MSG: {userInputMSG}\nThe MSG after dencrypting: {denMSG}")

if __name__ == '__main__':
    Main.main()