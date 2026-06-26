print("Number Game By Wyatt Stark!")
# correct stuff!
num1 = 3
num2 = 7
num3 = 13


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
                    ask3 = (int(input)("Guess a number through 1 through 15: "))
                    if ask3 == (num3):
                              print("You Beat Game 3!")
                              break
                    elif ask3 < (num3):
                              print("Too Low")
                    elif ask3 > (num3):
                              print("Too High!")
#----------------------------------------------------------------------------------

def start_game4():
          pass

def difficulty():
          pass



start_game1()
start_game2()
start_game3()