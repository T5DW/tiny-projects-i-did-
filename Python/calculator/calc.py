#add function
def add():
          ask_add1 =  int(input("Enter Your First Number: "))
          ask_add2 =   int(input("Enter Your 2nd Number: "))
          sum = ask_add1 + ask_add2
          print("Your Sum is: " + str(sum))
#sub function
def sub():
          ask_sub1 = int(input("Enter Your First Number: "))
          ask_sub2 = int(input("Enter Your Second Number: "))
          total = ask_sub1 - ask_sub2
          print("Your Total is : " + str(total))
# multi function
def multi():
          ask_multi1 = int(input("Enter Your First Number: "))
          ask_multi2 = int(input("Enter Your Second Number: "))
          total2 = ask_multi1 * ask_multi2
          print("Your Total is: " + str(total2))
# division function
def divsion():
          ask_divi1 = int(input("Enter Your First Number: "))
          ask_divi2 = int(input("Enter Your Second Number: "))
          total3 = ask_divi1 / ask_divi2
          print("Your Total is: " + str(total3))
# call add here
add()
ask1= input("Do you want to do subtraction? PUT y for yes n for no: ")
if ask1 == "y": 
          sub()
elif ask1 == "n":
          print("ok then")
#ask2
ask2 = input("Do you want to do multiplication? PUT y for yes n for no: ")
if ask2 == "y":
          multi()
elif ask2 == "n":
          print("bye!")
ask3 = input("Do you want to do division? PUT y for yes n for no: ")
if ask3 == "y":
          divsion()
elif ask3 == "n":
          print("ok")
