#-*-coding:utf8;-*-
#qpy:console
import random
#print (" roses are red \n violets are blue \n love you")

#lis = [2,4,8,9,8,9,8,6,7,]
#x = map(lambda x : x+1 , lis)


#y = filter(lambda x :x%3==0,lis)
#print (list(y))
print




def game():
    lose = [
    "wrqa+mqs",
    "hjra+wrqa",
    "mqs+hjra"
    ]
    draws = ["hjra+hjra","wrqa+wrqa","mqs+mqs"]
    #wins = ["wrqa+hjra","mqs+"]
    prop =["mqs","hjra","wrqa"]
    tries = 0
    loses = 0
    wins = 0
    eror = 0
    while tries < 3:
        play = input("khtar hjra/wrqa/mqs :")
        zhr = random.choice(prop)
        
        if str(play+"+"+zhr) in lose :
            print(str(zhr) + " ,lost!")
            tries += 1
            loses +=1
        elif str(play+"+"+zhr) in draws :
            print (str(zhr)+" ,ta3adol")
            tries += 1
        elif str(zhr+"+"+play) in lose :
            print(str(zhr)+" ,you win!")
            tries += 1
            wins +=1
        else :
            print("\n please chose from hajra/wrqa/mqs \n ")
            eror +=1
            break
    if  int(eror) <= 0 :
        if wins > loses :
            print("you won the game")
        elif wins == loses :
            print("ta3adol")
        else :
            print("you lost the game")
    else:
        eror=0
        tries =0
        game()
game()
            
            
