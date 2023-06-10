infoss = ["name","nickname","age","country","email","number"]
class person :
    def __init__(self,name,nickname,age,country,email,number):
        self.name=name
        self.nickname=nickname
        self.age = age
        self.country = country
        self.email = email
        self.number=number
    
    def createfile(self):
        file = open("%s.txt" %self.name,"a")
        file.write("-------------INFORMATION-------------\n\n")
        
        for inf in infoss:
            if self.inf != None:
                file.write(f"    {inf} : {self.inf}\n   ")
        file.write("----------------------- -------------\n\n")
        return file
        
def getinfo():
    for inf in infoss :
        inf = input(f"{inf} : ")
    
def home():
    choice = input("WHAT OPPERATION YOU WANT TO DO ? : \n\n a)create a file of your infos \n\n b)edit an already exsting file \n\n c) exit \n\n     chose:")
    if choice == "a":
        getinfo()
    if choice == "b":
        print ("we still working on this feature")
home()


        
