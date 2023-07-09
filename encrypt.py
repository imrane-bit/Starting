from cryptography.fernet import Fernet
import sys


try :
    key = Fernet.generate_key()

    with open('key.key','wb') as keyfile :
        keyfile.write(key)
        keyfile.close()
    fernet = Fernet(key)


    with open(sys.argv[1], 'rb') as f:
        content = f.read()
        f.close()
    encrypted = fernet.encrypt(content)
    with open(sys.argv[1], 'wb') as f :
        f.write(encrypted)
        f.close()
    print("Done")
except Exception as e:
    print(e)
