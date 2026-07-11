import tkinter as tk
import settings

def app():
    root = tk.Tk()
    root.geometry("500x600")
    root.title("Number Guessing Game By Wyatt Stark") 
    print("App Started!")
    
    black= fg= "black"
    normalbg = bg= "white"
    # title1
    label1 = tk.Label(root, text="Number Guessing Game", font=("Arial", 18), bg="blue")
    label1.pack(pady=5)
    # title2
    label2 = tk.Label(root, text="click a number 1 thru 3", font=("Arial", 18), bg="blue")
    label2.pack(pady=5)
    # points shit
    label3 = tk.Label(root, text="Points: 0", font=("Arial", 12), fg=black)
    label3.pack(pady=5)
    
    
    
    btnframe = tk.Frame(root)
    btnframe.columnconfigure(0, weight=1)
    btnframe.columnconfigure(1, weight=1)
    btnframe.columnconfigure(2, weight=1)

    popup_label = tk.Label(root, text="", font=("Arial", 16), fg="black", bg="blue")
    popup_label.pack(pady=10)
    
    popup_get = tk.Label(root, text="", font=("Arial", 16), fg="orange", bg="blue")
    popup_get.pack(pady=10)
    
    popup_right = tk.Label(root, text="", font=("Arial", 16), fg="green", bg="blue")
    popup_right.pack(pady=10)

    def wrong1():
        popup_label.config(text="Wrong")
    def wrong2():
        popup_get.config(text="Your getting there")
    def right1():
        popup_right.config(text="Correct +1 Point!")

    # FIX: Changed pady to 10 so the Open Settings button is visible
    settings_btn = tk.Button(btnframe, text="Open Settings", pady=10, font=("Arial", 18), bg="blue",  command=lambda: settings.open_settings(root))
    settings_btn.grid(row=4, column=1, sticky=tk.W+tk.E, pady=5)
    
    # FIX: Changed all paddings to positive 10 so the buttons don't disappear
    btn1 = tk.Button(btnframe, text="1", pady=10,  font=("Arial", 18), command=wrong1, bg="blue")
    btn1.grid(row=0, column=1, sticky=tk.W+tk.E, pady=5)

    btn2 = tk.Button(btnframe, text="2", pady=10, font=("Arial", 18), command=wrong2, bg="blue")
    btn2.grid(row=2, column=1, sticky=tk.W+tk.E, pady=5)
    
    btn3 = tk.Button(btnframe, text="3", pady=10, font=("Arial", 18), command=right1, bg="blue")
    btn3.grid(row=3, column=1, sticky=tk.W+tk.E, pady=5)
    
    print("Generating Next Level")
    btnframe.pack(fill='x', padx=20)
    
    root.mainloop()

app()
print('Closed App')
