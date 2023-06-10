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

subjects = ["math" , "pc" , "svt" ,"hg","ei","fr","ar","philo","en"]
coeuf =[]
for i in range(9) :
    subjects[i] = subject(subjects[i],"","","",input(f"{subjects[i]} coefic :"))
    coeuf.append(float(subjects[i].coef))
    print(coeuf)
for i in range(9) :
    try :
        subjects[i].x=float(input("first note in "+str(subjects[i].name)+": "))
        subjects[i].y=float(input("second note in "+str(subjects[i].name)+": "))
        subjects[i].z=float(input("third note in "+str(subjects[i].name)+": "))
    except ValueError as a :
        print(a)

total = lambda i : ((float(subjects[i].x) + float(subjects[i].y) + (subjects[i].z))/3)*float(subjects[i].coef)
noot = [total(i) for i in range(9)]
final = math.fsum(noot)/math.fsum(coeuf)
print ("your average is :"+str(final)) 
