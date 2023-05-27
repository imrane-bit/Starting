#-*-coding:utf8;-*-
#qpy:console
import math
class subject :
    def __init__(self,name,x,y,z,coef):   
         
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.coef= coef

math0 = subject("math0","note1","note2","note3",7)
pc = subject("pc","note1","note2","note3",7)
svt = subject("svt","note1","note2","note3",7)
hg = subject("hg","note1","note2","note3",2)
ei = subject("ei","note1","note2","note3",2)
fr = subject("fr","note1","note2","note3",4)
philo = subject("philo","note1","note2","note3",2)
ar = subject("ar","note1","note2","note3",2)
en = subject("en","note1","note2","note3",3)

subjects = [math0 , pc , svt ,hg,ei,fr,ar,philo,en]
coefs =[ coefs.coef for coefs in subjects]

for subject in subjects :
    try :
        subject.x=float(input("first note in "+str(subject.name)+": "))
        subject.y=float(input("second note in "+str(subject.name)+": "))
        subject.z=float(input("third note in "+str(subject.name)+": "))
    except ValueError as a :
        print(a)


total = lambda subject : ((subject.x + subject.y + subject.z)/3)*subject.coef


noot = [total(noot) for noot in subjects]
final = math.fsum(noot)/math.fsum(coefs)

print ("your average is :"+str(final)) 