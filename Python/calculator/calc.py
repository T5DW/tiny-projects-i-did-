#add function
def add():
          ask_add1 =  int(input("Enter Your First Number: "))
          ask_add2 =   int(input("Enter Your 2nd Number: "))
          sum = ask_add1 + ask_add2
          print("Your Sum is: " + str(sum))
#sub function
def sub():
          ask_sub1 = int(input("Enter Your FIrst Number: "))
          ask_sub2 = int(input("Enter Your Second Number: "))
          total = ask_sub1 - ask_sub2
          print("Your Total is : " + str(total))
def multi():
          ask_multi1 = int(input("Enter Your First Number: "))
          ask_multi2 = int(input("Enter Your Second Number: "))
          total2 = ask_multi1 * ask_multi2
          print("Your Total is: " + str(total2))


add()
ask3= input("Do you want to do subtraction? PUT y for yes n for no  ")
if ask3 == "y": 
          sub()
elif ask3 == "n":
          print("ok then")

ask4 = input("Do you want to do multiplication? PUT y for yes n for no  ")
if ask4 == "y":
          multi()
elif ask4 == "n":
          print("bye!")
