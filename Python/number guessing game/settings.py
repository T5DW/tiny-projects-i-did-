import tkinter as tk

settings_win = None

def open_settings(root_window, change_bg_callback=None):
    global settings_win

    if settings_win is not None and settings_win.winfo_exists():
        settings_win.lift()
        return

    settings_win = tk.Toplevel(root_window)
    settings_win.geometry("500x650")
    settings_win.title("Number Guessing Game Settings")

    tk.Label(settings_win, text="Settings", font=("Arial", 20, "bold")).pack(pady=10)

    btnframe = tk.Frame(settings_win)
    btnframe.pack(fill="x", padx=20, pady=10)

    for i in range(2):
        btnframe.columnconfigure(i, weight=1)

    # Improved color change function
    def set_color(color):
        if change_bg_callback:
            change_bg_callback(color)   # This will update everything in main window
        else:
            root_window.config(bg=color)


    colors = [
        ("Black Mode", "black", "white"),
        ("Indigo Mode", "#4b0082", "white"),
        ("Purple Mode", "purple", "white"),
        ("Pink Mode", "pink", "black"),
        ("Yellow Mode", "yellow", "black"),
        ("Aqua Mode", "aqua", "black"),
        ("Dark Blue", "#00008b", "white"),
        ("Dark Cyan", "#008b8b", "white"),
        ("Dark Green", "#006400", "white"),
        ("Dark Red", "#8b0000", "white"),
        ("Gold Mode", "gold", "black"),
        ("Normal / White", "white", "black"),
    ]

    row = 0
    col = 0
    for text, color, fg in colors:
        tk.Button(
            btnframe,
            text=text,
            font=("Arial", 16),
            bg=color,
            fg=fg,
            command=lambda c=color: set_color(c),
            height=2
        ).grid(row=row, column=col, sticky=tk.W+tk.E, padx=5, pady=5)
        
        col += 1
        if col > 1:
            col = 0
            row += 1

    # Close button
    tk.Button(settings_win, text="Close Settings", font=("Arial", 14), 
              command=settings_win.destroy).pack(pady=15)
