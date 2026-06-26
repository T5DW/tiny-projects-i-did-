print("Number Guessing Game By Wyatt Stark!")
#-----correct stuff!-and variables-----------------------------------------------------------------
num1 = 3
num2 = 7
num3 = 13
num4 = 23
#------------------------point-stuff-----------------------------------------------------------
reg_points = 0
points = 1
#-----------------------guess-counter-------------------------------------------------
reg_counter = 0
counter = 1
#-----------------------difficulty's-------------------------------------------------
easy = 1
medium = 2
hard = 3
very_hard = 4
#---------------------Functions----------------------------------------------------
def start_game1():
          global  reg_counter
          reg_counter = 0
          global reg_points
          while True:
                    ask = (int)(input("Guess a number through 1 thru 3: "))
                    reg_counter += counter
                    if ask == (num1):
                              print("You Beat Game 1!")
                              reg_points += points
                              print("Your points are now: " + str(reg_points))
                              print("it took you this amount of guesses: " + str(reg_counter))
                              start_game2()
                    elif ask < (num1):
                              print('Too Low!')
                              reg_points -= points
                              print("You have lost a point: " + str(reg_points))
                    elif ask >(num1):
                              print("Too high!")
                              reg_points -= points
                              print("You have lost a point: " + str(reg_points))
#----------------------------------------------------------------------------------
def start_game2():
          global  reg_counter
          reg_counter = 0
          global reg_points
          while True:
                    ask2 =(int)(input("Guess a number through 1 through 8: "))
                    reg_counter += counter
                    if ask2 == (num2):
                              print("You Beat Game 2!")
                              reg_points += points
                              print("Your points are now: " + str(reg_points))
                              print("it took you this amount of guesses: " + str(reg_counter))
                              start_game3()
                    elif ask2 < (num2):
                              print("Too Low!")
                              reg_points -= points
                              print("You have lost a point:" + str(reg_points))
                    elif ask2 > (num2):
                              print("Too High!")
                              reg_points -= points
                              print("You have lost a point:" + str(reg_points))
#----------------------------------------------------------------------------------
def start_game3():
          global  reg_counter
          reg_counter = 0
          global reg_points
          while True:
                    ask3 =(int)(input("Guess a number through 1 through 15: "))
                    reg_counter += counter
                    if ask3 == (num3):
                              print("You Beat Game 3!")
                              reg_points += points
                              print("Your points are now: " + str(reg_points))
                              print("it took you this amount of guesses: " + str(reg_counter))
                              start_game4()
                    elif ask3 < (num3):
                              print("Too Low")
                              reg_points -= points
                              print("You have lost a point: " + str(reg_points))
                    elif ask3 > (num3):
                              print("Too High!")
                              reg_points -= points
                              print("You have lost a point: " + str(reg_points))
#----------------------------------------------------------------------------------
def start_game4():
          global  reg_counter
          reg_counter = 0
          global reg_points
          while True:
                    ask4 =(int)(input("Guess a number through 1 through 30: "))
                    reg_counter += counter
                    if ask4== (num4):
                              print("You Beat Game 4!")
                              reg_points += points
                              print("Your final points are:  " + str(reg_points))
                              print("it took you this amount of guesses: " + str(reg_counter))
                              break
                    elif ask4 < (num4):
                              print("Too Low")
                              reg_points -= points
                              print("You have lost a point:" + str(reg_points))
                    elif ask4 > (num4):
                              print("Too High!")
                              reg_points -= points
                              print("You have lost a point:" + str(reg_points))
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
