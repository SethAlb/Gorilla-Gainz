#Gorilla gains fitness app 
#Author: Seth Albergaira 
#\n
import time 

def main(): 
    running = True 
    TitlePage()
    name = input ("Enter Name: ")
    weight=UserWeight()
    goal = UserGoal() 
    
    WelcomeMessage(name)
    Cals = DailyCals(weight,goal)
    while (running == True):
        option = menu()
    



def TitlePage(): 
    Title = '''
     ____            _ _ _          ____       _           
    / ___| ___  _ __(_) | | __ _   / ___| __ _(_)_ __  ____
    | |  _ / _ \| '__| | | |/ _` | | |  _ / _` | | '_ \|_  /
    | |_| | (_) | |  | | | | (_| | | |_| | (_| | | | | |/ / 
     \____|\___/|_|  |_|_|_|\__,_|  \____|\__,_|_|_| |_/___|
    '''
    Tpic= '''            ."`".
        .-./ _=_ \.-.
        {  (,(oYo),) }}
        {{ |   "   |} }
        { { \(---)/  }}
        {{  }'-=-'{ } }
        { { }._:_.{  }}
        {{  } -:- { } }
        {_{ }`===`{  _}
        ((((\)     (/))))
    '''

    print(Title)
    print(Tpic)
def UserWeight():
    n=False 
    while(n==False): 
        try: 
            weight = int(input ("Enter Weight(lbs): "))
            n=True
        except: 
            print("Enter number only")
    return weight 
def UserGoal():
    n=False
    while(n==False): 
        print("Goal: \n1: Lose Weight \n2: Maintain Weight \n3: Gain Weight")
        try: 
            goal = int(input("Enter Goal 1-3:"))
            n= True
        except: 
            print("Please enter From option 1-3")
    return goal

def WelcomeMessage(n):
    print("Loading User info: \n \t\t please wait ")
    time.sleep(3)
    print("Welcome "+ n)

def DailyCals(w,g): 
    Cals = w *12 
    if(g==1): 
        Cals = Cals - 500 
        print("You need "+ str(Cals) +" a day to lose weight")
    elif(g==2):
        Cals = Cals  
        print("You need "+ str(Cals) +" a day to maintain weight")
    elif(g==3):
        Cals = Cals + 500 
        print("You need "+ str(Cals) +" a day to gain weight")
    return Cals 

def menu(): 
    print("What Would you like to do \n1:Food Checker \n2:Cal Tracker \n3:Exit")
    n=False
    while (n==False):
        try: 
            option = int(input("Enter :"))
            n= True
        except: 
                print("Please enter From option 1-3")  
        if (option == 1 ): 

        elif(option ==2 ):

        elif(option ==3 ): 
            exit()
    return option 

main ()




