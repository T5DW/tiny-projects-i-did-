print("Number Guessing Game By Wyatt Stark!")
# correct stuff!
num1 = 3
num2 = 7
num3 = 13
num4 = 23
#difficultys
easy = 1
medium = 2
hard = 3
very_hard = 4
#---------------------Functions----------------------------------------------------
def start_game1():
          while True:
                    ask = (int)(input("Guess a number through 1 thru 3: "))
                    if ask == (num1):
                              print("You Beat Game 1!")
                              break
                    elif ask < (num1):
                              print('Too Low!')
                    elif ask >(num1):
                              print("Too high!")
#----------------------------------------------------------------------------------
def start_game2():
          while True:
                    ask2 =(int)(input("Guess a number through 1 through 8: "))
                    if ask2 == (num2):
                              print("You Beat Game 2!")
                              break
                    elif ask2 < (num2):
                              print("Too Low!")
                    elif ask2 > (num2):
                              print("Too High!")   
#----------------------------------------------------------------------------------
def start_game3():
          while True:
                    ask3 =(int)(input("Guess a number through 1 through 15: "))
                    if ask3 == (num3):
                              print("You Beat Game 3!")
                              break
                    elif ask3 < (num3):
                              print("Too Low")
                    elif ask3 > (num3):
                              print("Too High!")
#----------------------------------------------------------------------------------
def start_game4():
          while True:
                    ask4 =(int)(input("Guess a number through 1 through 30: "))
                    if ask4== (num4):
                              print("You Beat Game 4!")
                              break
                    elif ask4 < (num4):
                              print("Too Low")
                    elif ask4 > (num4):
                              print("Too High!")
#----------------------------------------------------------------------------------
def difficulty():
           ask5 =(int)(input("What difficulty do you want to start out with 1 is easy 2 is med 3 is hard 4 is very hard pls type your number: "))
           if ask5 == (easy):
                     start_game1()
           elif ask5 == (medium):
                     start_game2()
           elif ask5 == (hard):
                     start_game3()
           elif ask5 == (very_hard):
                     start_game4()
#----------------------------------------------------------------------------------                    
difficulty()
start_game1()
start_game2()
start_game3()
start_game4()
