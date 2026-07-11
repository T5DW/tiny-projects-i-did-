import tkinter as tk

# 1. FIX: Standardized variable assignment
text_white = "white"
black = "black"
rating_win = None  # Keeps track of the open window

def rating(root_window=None): 
    global rating_win  
    
    # If the window is already open, just bring it to the front
    if rating_win is not None and rating_win.winfo_exists():
        rating_win.lift()
        return
    
    # Create the window as a child of the main root window
    rating_win = tk.Toplevel(root_window)
    rating_win.title("Rating's Menu!")
    rating_win.geometry("500x350") # Expanded geometry so everything fits nicely
    rating_win.configure(bg="black")

     
    label1 = tk.Label(rating_win, text="Rating System", font=("Arial", 18), bg=black, fg=text_white)
    label1.pack(pady=5)

    # 2. FIX: Changed master from 'rating' to 'rating_win' and added black background
    popup_rat1 = tk.Label(rating_win, text="", font=("Arial", 12), fg="white", bg=black)
    popup_rat1.pack()
    
    popup_rat2 = tk.Label(rating_win, text="", font=("Arial", 12), fg="white", bg=black)
    popup_rat2.pack()
    
    popup_rat3 = tk.Label(rating_win, text="", font=("Arial", 12), fg="white", bg=black)
    popup_rat3.pack()
    
    popup_rat4 = tk.Label(rating_win, text="", font=("Arial", 12), fg="white", bg=black)
    popup_rat4.pack()

    popup_rat5 = tk.Label(rating_win, text="", font=("Arial", 12), fg="white", bg=black)
    popup_rat5.pack()

    # 3. FIX: Cleared previous texts so they don't pile up when clicking multiple buttons
    def clear_labels():
        popup_rat1.config(text="")
        popup_rat2.config(text="")
        popup_rat3.config(text="")
        popup_rat4.config(text="")
        popup_rat5.config(text="")

    def rat1():
        clear_labels()
        popup_rat1.config(text="thx ig....")
    def rat2():
        clear_labels()
        popup_rat2.config(text="Thanks")
    def rat3():
        clear_labels()
        popup_rat3.config(text="Thanks")
    def rat4():
        clear_labels()
        popup_rat4.config(text="Thanks!") # 4. FIX: Fixed typo 'confog' -> 'config'
    def rat5():
        clear_labels()
        popup_rat5.config(text="Your the Best!!!!!!!!!!")
     
    # Parent the frame to 'rating_win'
    btnframe = tk.Frame(rating_win, bg=black) 
    btnframe.pack(pady=10) # Added .pack() so the 1-5 buttons actually display
    
    # 5. FIX: Expanded column configurations to accommodate 5 buttons side-by-side
    btnframe.columnconfigure(0, weight=1)
    btnframe.columnconfigure(1, weight=1)
    btnframe.columnconfigure(2, weight=1)
    btnframe.columnconfigure(3, weight=1)
    btnframe.columnconfigure(4, weight=1)
    
    # 6. FIX: Unique grid columns for each button so they don't stack on top of each other
    btn1 = tk.Button(btnframe, text="1", font=("Arial", 18), bg="blue", fg="white", command=rat1)
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E, padx=5, pady=5)
    
    btn2 = tk.Button(btnframe, text="2", font=("Arial", 18), bg="blue", fg="white", command=rat2)
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E, padx=5, pady=5)
    
    btn3 = tk.Button(btnframe, text="3", font=("Arial", 18), bg="blue", fg="white", command=rat3)
    btn3.grid(row=0, column=2, sticky=tk.W+tk.E, padx=5, pady=5)
    
    btn4 = tk.Button(btnframe, text="4", font=("Arial", 18), bg="blue", fg="white", command=rat4)
    btn4.grid(row=0, column=3, sticky=tk.W+tk.E, padx=5, pady=5)
    
    btn5 = tk.Button(btnframe, text="5", font=("Arial", 18), bg="blue", fg="white", command=rat5)
    btn5.grid(row=0, column=4, sticky=tk.W+tk.E, padx=5, pady=5)

    # Indented this button so it lives inside the function scope
    tk.Button(rating_win, text="Close Ratings Menu", font=("Arial", 11), bg="white", fg="black",
              command=rating_win.destroy).pack(pady=15)
