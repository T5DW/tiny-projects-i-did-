#add
ask_add1 =  int(input("Enter Your First Number: "))
ask_add2 =   int(input("Enter Your 2nd Number: "))
#sub function
def sub():
          ask_sub1 = int(input("Enter Your FIrst Number: "))
          ask_sub2 = int(input("Enter Your Second Number: "))
          total = ask_sub1 - ask_sub2
          print("Your Total is : " + str(total))

#sum for the add
sum = ask_add1 + ask_add2

#TODO: Make a add function so this code is mainly functions
def addthemup():
          print("Your Sum is: " + str(sum))


addthemup()
ask3= input("Do you want to do subtraction? PUT y for yes n for no  ")
if ask3 == "y": 
          sub()
elif ask3 == "n":
          print("ok then")
