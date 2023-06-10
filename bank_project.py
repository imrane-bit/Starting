import pickle
import click
class user () :
    def __init__(self,name,gender,age,password,credit):
        self.name = name
        self.gender = gender
        self.password = password
        self.credit = credit
        self.age = age
    def save (self):
        try:
            accfile = open("acc.dat","wb")
            pickle.dump(self,accfile,protocol=pickle.HIGHEST_PROTOCOL)
            return accfile
        finally:
            user.panel(self)

    def giftcodee(self):
        gift_codes = [8767689888,67567655,87656789,87657887,9876543,243567897,686865767]
        try : 
            code = float(input("enter your code here: "))
            if code in gift_codes :
                self.credit = self.credit + 400
                print (f"congrats, you won 400$ , YOUR CREDIT NOW is {self.credit}")
                return self.credit
            else :
                print("wrong code")
        except ValueError :
            print(ValueError)
        finally:
            user.save(self)
        
    def withrawal (self):
        try :
            withr = float(input("how much you want to withrawal :"))
            if self.credit >= withr:
                self.credit  = self.credit - withr
                print(f"your credit has been sucessfuly updated : {self.credit}$")
                return self.credit
        
            else :
                print("your balence is not enough")
        except ValueError as v :
            print(v)
        finally :
            user.save(self)
    def disposit (self):
        try :
            self.credit  = self.credit + float(input("how much you want to disposit :"))
            print(f"your credit has been sucessfuly updated : {self.credit}$")
            return self.credit
        except ValueError as v :
            print (v)
            user.disposit()

        finally:
            user.save(self)
    def panel (self):
        print("WELCOME TO YOUR ACCOUNT \n \n your account information are :")
        print ("your name is : "+self.name+ "\n")
        print ("your age is : "+str(self.age)+ "\n" )
        print ("your gender is : "+self.gender+ "\n")
        print ("your credit is : "+str(self.credit) + "$\n")
        def opperation(self) :
            opper = input(" \n        a)disposit\n        b)withrawal \n        c)use giftcode \n        d)exit \n chose an opperation (a or b or c or d)")
            if opper == "a":
                user.disposit(self)                
            elif opper == "b":
                user.withrawal(self) 
                
            elif opper == "d" :
                regislog()
            
            elif opper == "c" :
                user.giftcodee(self)
            else : 
                print("\n\n    please enter a or b")
                opperation(self)
            
            accfile = open("acc.dat","wb")
            
            pickle.dump(self,accfile,protocol=pickle.HIGHEST_PROTOCOL)
            return accfile
            panel(self)
        opperation(self)
def register() :
    
    print("to register in our bank , please enter the following information :")
    try :
        name0 = str(input(" your name : "))
        age0 = float(input("your age : "))
        gender0 = str(input("your gender: "))
        password0 = str(input("make a strong password : "))
        newuser = user(str(name0),str(gender0),float(age0),str(password0),0)
        accfile = open("acc.dat","wb")
        pickle.dump(newuser,accfile,protocol=pickle.HIGHEST_PROTOCOL)
        accfile.close
        return accfile
    except ValueError as v :
        print(v)
        register()

def login():
    print("to login enter :\n" )
    logname = input("your name :")
    logpass = input("your password :")
    accfile = open("acc.dat","rb")
    O = pickle.load(accfile)
    if logname == O.name and logpass == O.password :
        print("\n\n\n LOGED IN SUCCESSFULLY \n\n\n")
        user.panel(O)
    else :
        print("inccorect")
        login()
def regislog ():
    click.clear()
    a = input("you want to login /register/exit :")
    if str(a) == "login":
        login()
    elif str(a) == "register":
        register()
        login()
    elif str(a) == "exit" :
        quit()
    else:
        print("wrong")

regislog()
