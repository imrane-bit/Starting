from cryptography.fernet import Fernet
import sys 

filetaken = sys.argv[1]
keyf = sys.argv[2]



with open(keyf, 'rb') as keyfile:
    seckey = keyfile.read()
    keyfile.close()


with open(filetaken, 'rb') as encfile:
    data = encfile.read()
    decrypted = Fernet(seckey).decrypt(data)
    encfile.close()


with open(filetaken, 'wb') as encfile :
    encfile.write(decrypted)
    encfile.close()


    
