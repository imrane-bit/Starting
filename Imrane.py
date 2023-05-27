#a bit advanced calculator
def calc():
    print ("\n \n \n \n this is a bit advanced calculator\n \n \n \n ")
    try :
        a = float(input("enter the number a : "))
        b = float(input("enter the number b : "))
    except ValueError as err :
        print("\n\n\n" + str(err) )
        calc()
#addition function
    def sumo():
        result = a+b
        print ("\n \n the result is : "+str(result)+"\n \n \n \n \n ")
        calc()
#substraction function
    def sub():
        result = a-b
        print ("\n \n the result is : "+str(result)+"\n \n \n \n \n ")
        calc()
#multiplication function
    def mult():
        result = a*b
        print ("\n \n the result is : "+str(result)+"\n \n \n \n \n ")
        calc()
 #division function
    def div():
        try :
            result = a/b
            print ("\n \n the result is : "+str(result)+"\n \n \n \n \n ")
            calc()
        except ZeroDivisionError as erro :
            print ("\n\n"+ str(erro))
            calc()
#exponential function
    def exp(): 
  #  a = float(input ("insert number  : "))
  #  b = float(input ("insert power : "))        
        powd = 1
        z = a*1
        while powd < b :
            z = z*a
            powd += 1
        print ("\n \n the result is : "+str(z)+"\n \n \n \n \n ")
        calc()

    
    opperation = input ("\n\n\n\ntype the operation (+,-,×,÷,exp : ")
    if opperation=="+":
        sumo()
    elif opperation=="-":
        sub()
    elif opperation=="÷":
        div()
    elif opperation=="×":
        mult()
    elif opperation=="exp" :
        exp()
    elif opperation==str(6) :
        print( )
    else:
        print("\n \n \n \n \n invalid operation\n \n \n \n \n \n \n \n ")
        calc()
calc()

#dictionaries

'''socimedwords ={
    "mrc": "merci",
	   "nvm":"never mind",
	   "btw":"by the way",
	   "ofc":"of course", 
	
	}
print (socimedwords.get("oc","not a valid key"))
'''


def gessgame() :
    count = 0
    word= ""
    countlim =3
    zerotry = False
    while word != "Luca" and not(zerotry) : 
            if count< countlim :
                word = input("guess the name of my loved cat: ")
                count +=1
            else :
                zerotry = True
                
    if not(zerotry) :
        print("you won!")
    if zerotry :
        print ("game over!")
    

#gessgame()

#for word in range(3) :
    if word==1 :
        print ("it's one")
    else :
        print ("not one")

#def power():        
    pow = 1
    z = a*1
    while pow < b :
        z = z*a
        pow += 1
    print (z)
#power()

def power2(i,o):
    result=1
    for index in range(o) :
        result=result*i
    return(result)
#print(power2(2,5))
'''numbergrid =[
["a","b","o"],
["s","o","r"],
["x","o","o"],
]
print (numbergrid[1][2])
for row in numbergrid :
    for unity in row:
        print(unity)'''

def translation (word):
    lowvowels =[    
    'a','e','i','o','u'
    ]
    upvowels =[
    "A","E","I","O","U"
    ]
    
    for letter in word :
        for letter in lowvowels:
            word= word.replace(letter,"g")
        for letter in upvowels :
            word= word.replace(letter,"G")
    return word 
#print (translation(input("Give word:")))

'''passfiles = open("/storage/emulated/0/imrane.txt","w")
passfiles.write("\ntbonmok")
print(passfiles.readlines())
for password in passfiles.readlines():
    print (password)
n=10000
rep=0
while rep <= n :
    #passfiles.write("\ntbonmok")
    #rep += 1
print (passfiles.readline())
print (passfiles.readlines()[45])

passfiles.close()
#creat files
filei = open("fileitbon.html","w")
filei.write("<p>tbonmok</p>")
import math

a= math.copysign(9, -1)
print(a)'''
class tbon :
    def __init__(self,name, color,size,isinfected,isvirgin) :
        self.name = name
        self.color = color 
        self.size =size
        self.isinfected = isinfected
        self.isvirgin = isvirgin
class question:
    def __init__(self, prompt,choice1,choice2,answer):
        self.prompt = prompt
        self.choice1 = choice1 
        self.choice2 =choice2
        self.answer = answer

def square(x):
    return x*x
for number in range(-10,11):
    print(square(number))
