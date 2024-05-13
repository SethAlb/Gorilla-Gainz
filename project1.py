#Gorilla gains fitness app 
#Author: Seth Albergaira 
#\n
#1105073 
import time,requests, csv 
import mysql.connector

global name 
global mydb 

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password='Seth', 
        database="gorillagainz "
        )

def main(): 
    running = True 
    TitlePage()
    name = input ("Enter Name: ")
    weight=UserWeight()
    goal = UserGoal() 
    
    WelcomeMessage(name)
    Cals = DailyCals(weight,goal)
    while (running == True):
        option = menu(name)
    

def AddCals(Food,Calories,name):    
   
    mycursor = mydb.cursor()

    date = input("Enter date: ")

    sql = "INSERT INTO calorietracker (name, Food,Calories,day) VALUES (%s, %s,%s,%s)"
    val = (name, Food, Calories,date)
    
    mycursor.execute(sql, val)
    mydb.commit()



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

def FoodChecker(name):
    apikey = "k8Bt3s6IchI/f39NvI3NAA==Q81aHPy4MJqLWj7t"
    food = input("Enter: (Serving amnt food )")
    url = 'https://api.calorieninjas.com/v1/nutrition?query='
    response = requests.get(url + food, headers={'X-Api-Key': apikey})
    json_data = response.json()
    calories = json_data["items"][0]["calories"]
    print (calories)
    food = json_data["items"][0]["name"]

    add = input("Would you like to add this to your Calorie  Tracker?\n1: Y \n2: N")

    if (add == "Y"):
        AddCals(food,calories,name)  
    elif(add == "N"): 
        print("")
    elif(): 
        add = input ("please enter either Y or N ")


def viewCals(name): 
    mycursor = mydb.cursor()
    sql = "SELECT * FROM calorietracker WHERE name ='"+name+"'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


def menu(name): 
    print("What Would you like to do \n1:Food Checker \n2:Cal Tracker \n3:Exit")
    n=False
    while (n==False):
        try: 
            option = int(input("Enter :"))
            n= True
        except: 
                print("Please enter From option 1-3")  
        if (option == 1 ): 
            FoodChecker(name)
        elif(option ==2 ):
                viewCals(name)
        elif(option ==3 ): 
            exit() 
    return option 

main ()




