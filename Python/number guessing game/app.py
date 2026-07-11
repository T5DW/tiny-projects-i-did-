import random
import tkinter as tk
import settings
import rating

def app():
    root = tk.Tk()
    root.geometry("700x700")
    root.title("Number Guessing Game By Wyatt Stark") 
    print("App Started!")
    
    lv1_correct = random.randint(1, 3)
    points = 0
    black = "black"
    
    # Function to change background color
    def change_background(color):
        root.config(bg=color)
        label1.config(bg=color)
        label2.config(bg=color)
        label3.config(bg=color)
        popup_label.config(bg=color)
        btnframe.config(bg=color)

    # Labels
    label1 = tk.Label(root, text="Number Guessing Game", font=("Arial", 18), bg="lightblue", fg="black")
    label1.pack(pady=5)
    
    label2 = tk.Label(root, text="click a number 1 thru 3", font=("Arial", 18), bg="lightblue", fg="black")
    label2.pack(pady=5)
    
    label3 = tk.Label(root, text=f"Points: {points}", font=("Arial", 12), bg="lightblue", fg=black)
    label3.pack(pady=5)

    popup_label = tk.Label(root, text="", font=("Arial", 16), fg="white", bg="blue")
    popup_label.pack(pady=10)

    def checkguess(guess):
        nonlocal points, lv1_correct
        if guess == lv1_correct:
            points += 1
            label3.config(text=f"Points: {points}")
            popup_label.config(text="Correct! +1 Point", fg="green")
        else:
            popup_label.config(text="Wrong!", fg="red")

    btnframe = tk.Frame(root, bg="lightblue")
    btnframe.columnconfigure(0, weight=1)
    btnframe.columnconfigure(1, weight=1)
    btnframe.columnconfigure(2, weight=1)

    # Game Buttons
    btn1 = tk.Button(btnframe, text="1", pady=10, font=("Arial", 18), bg="blue", 
                     command=lambda: checkguess(1))
    btn1.grid(row=0, column=1, sticky=tk.W+tk.E, pady=5)

    btn2 = tk.Button(btnframe, text="2", pady=10, font=("Arial", 18), bg="blue", 
                     command=lambda: checkguess(2))
    btn2.grid(row=2, column=1, sticky=tk.W+tk.E, pady=5)
    
    btn3 = tk.Button(btnframe, text="3", pady=10, font=("Arial", 18), bg="blue", 
                     command=lambda: checkguess(3))
    btn3.grid(row=3, column=1, sticky=tk.W+tk.E, pady=5)

    # Settings & Rating
    settings_btn = tk.Button(btnframe, text="Open Settings", pady=10, font=("Arial", 18), bg="blue", 
                             command=lambda: settings.open_settings(root, change_background))
    settings_btn.grid(row=4, column=1, sticky=tk.W+tk.E, pady=8)
    
    rating_btn = tk.Button(btnframe, text="Rate this Game here!", pady=10, font=("Arial", 18), bg="black", fg="white", 
                           command=lambda: rating.rating(root))
    rating_btn.grid(row=5, column=1, sticky=tk.W+tk.E, pady=8)

    btnframe.pack(fill='x', padx=20)
    
    root.mainloop()

app()
print('Closed App')
