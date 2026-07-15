run = True
mainmenu = True
mainmenu2 = False
settingsmenu = False
play = False
rules = False


while run:

    while mainmenu:
        name = "Matched Player"
        print("SIGNIN MENU")
        print("2: SETTINGS")
        print("3: RULES")
        print("4: QUIT")
        print("5: Name")

        player_input = input(": ")

        if player_input == "1":
            print("Starting game...")
            # play = True
            # mainmenu = False

        elif player_input == "2":
            settingsmenu = True
            mainmenu = False
            

        elif player_input == "3":
            rules = True
            mainmenu = False

        elif player_input == "4":
            run = False
            break
        elif player_input == "5":
            username = input(">Name:  ")
            print("hello " + username + "!" )
            mainmenu = False
            mainmenu2 = True
            username = username.strip()
        if username == "":
            username = "Matched Player"
            print("Hello " + username + "!" )
            mainmenu = False
            mainmenu2 = True
            
    while mainmenu2:
        print("MAIN MENU")
        print("1: NEW GAME")
        print("2: SETTINGS")
        print("3: RULES")
        print("4: QUIT")
        player_input = input(":")
        if player_input == "1":
         pass
        elif player_input == "2":
         settingsmenu = True
        mainmenu2 = False
    

    while settingsmenu :
              print("SETTINGS")
              print("1: CHANGE NAME")
              print("2: CHANGE DIFF")
              print("3: BACK")
              player_input = input(": ")
              if player_input == "1":
                print("Coming Soon!")
              elif player_input == "2":
                print('Coming Soon!')
              elif player_input == "3":
               print("Going Back to Main Menu")
              settingsmenu = False
              mainmenu = True

while rules:
        print("RULES")
        print("1: TO BE DONE....")
        print("2: GO BACK TO MAIN MENU")
        player_input = input(": ")
        if player_input == "1":
            print("GOING BACK TO MAIN MENU")
            rules = False
            mainmenu = True
        elif player_input == "2":
            rules = False
            mainmenu = True

        else:
            print("Invalid option!")

print("Goodbye!")
