
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
        if self.name != None:
            file.write(f"    name : {self.name}\n   ")
        if self.nickname != None:
            file.write(f"    nickname : {self.nickname}\n   ")
        if self.age != None:
            file.write(f"    age : {self.age}\n   ")
        if self.country != None:   
            file.write(f"    country : {self.country}\n   ")
        if self.email != None:
            file.write(f"    email : {self.email}\n   ")
        if self.number != None :
            file.write(f"    number : {self.number}\n   ")
        file.write("----------------------- -------------\n\n")
        return file
        
def getinfo():
    username = input("name :")
    usernickname = input("nickname :")
    userage = input("age :")
    usercountry = input("country :")
    useremail = input("email :")
    usernumber = input("number :")
    user = person(username,usernickname,userage,usercountry,useremail,usernumber)
    person.createfile(user)
    
def home():
    choice = input("WHAT OPPERATION YOU WANT TO DO ? : \n\n a)create a file of your infos \n\n b)edit an already exsting file \n\n c) exit \n\n     chose:")
    if choice == "a":
        getinfo()
    if choice == "b":
        print ("we still working on this feature")
home()


        
