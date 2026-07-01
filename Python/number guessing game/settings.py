import tkinter as tk

# Keep a global reference to the window object
settings_win = None

def open_settings(root_window):
    global settings_win
    
    if settings_win is not None and settings_win.winfo_exists():
        settings_win.lift()  
        return

    # 2. Create the window since it does not exist yet
    settings_win = tk.Toplevel(root_window)
    settings_win.geometry("500x600")
    settings_win.title("Number Guessing Game Settings")

    label = tk.Label(settings_win, text="Settings:", font=("Arial", 18))
    label.pack(pady=10)
    
    btnframe = tk.Frame(settings_win)
    btnframe.columnconfigure(0, weight=1)
    btnframe.columnconfigure(1, weight=1)
    btnframe.columnconfigure(2, weight=1)
    
    def darkmode():
        settings_win.configure(bg="black")
        label.configure(bg="black", fg="white")
        btnframe.configure(bg="black")
        # Changes your main app window to black
        root_window.configure(bg="black") 

    def normal():
        settings_win.configure(bg="white")
        label.configure(bg="white", fg="black")
        btnframe.configure(bg="white")
        # Changes your main app window to white
        root_window.configure(bg="white") 

    btn1setting = tk.Button(btnframe, text="Dark Mode", font=("Arial", 18), command=darkmode)
    btn1setting.grid(row=1, column=1, sticky=tk.W+tk.E, pady=5)
    
    btn2setting = tk.Button(btnframe, text="Normal", font=("Arial", 18), command=normal)
    btn2setting.grid(row=2, column=1, sticky=tk.W+tk.E, pady=5)
    
    btnframe.pack(fill='x', padx=20)
