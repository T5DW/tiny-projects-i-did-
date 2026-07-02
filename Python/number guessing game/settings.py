import tkinter as tk

# Keep a global reference to the window object
settings_win = None


def open_settings(root_window):
    global settings_win

    # If window already exists, bring it to front
    if settings_win is not None and settings_win.winfo_exists():
        settings_win.lift()
        return

    # Create settings window
    settings_win = tk.Toplevel(root_window)
    settings_win.geometry("500x600")
    settings_win.title("Number Guessing Game Settings")

    label = tk.Label(settings_win, text="Settings:", font=("Arial", 18))
    label.pack(pady=10)

    btnframe = tk.Frame(settings_win)

    for i in range(3):
        btnframe.columnconfigure(i, weight=1)

    # Theme functions
    def darkmode():
        root_window.configure(bg="black")

    def normal():
        root_window.configure(bg="white")

    def purplemode():
        root_window.configure(bg="purple")

    def pinkmode():
        root_window.configure(bg="pink")

    def alicebluemode():
        root_window.configure(bg="#f0f8ff")

    def aquamode():
        root_window.configure(bg="aqua")

    def chocolatemode():
        root_window.configure(bg="#8b4513")

    def darkbluemode():
        root_window.configure(bg="#00008b")

    def darkcyanmode():
        root_window.configure(bg="#008b8b")

    def darkgreenmode():
        root_window.configure(bg="#006400")

    def yellowmode():
        root_window.configure(bg="yellow")

    def brickmode():
        root_window.configure(bg="#b22222")

    def darkredmode():
        root_window.configure(bg="#8b0000")

    def goldmode():
        root_window.configure(bg="gold")

    def lightslatebluemode():
        root_window.configure(bg="#8470ff")

    def indigomode():
        root_window.configure(bg="#4b0082")

    # Buttons
    tk.Button(
        btnframe,
        text="Black Mode",
        font=("Arial", 18),
        command=darkmode,
        bg="black",
        fg="white"
    ).grid(row=1, column=1, sticky=tk.W + tk.E, pady=5)

    tk.Button(
        btnframe,
        text="Indigo Mode",
        font=("Arial", 18),
        command=indigomode,
        bg="#4b0082",
        fg="white"
    ).grid(row=2, column=1, sticky=tk.W + tk.E, pady=5)

    tk.Button(
        btnframe,
        text="Pink Mode",
        font=("Arial", 18),
        command=pinkmode,
        bg="pink",
        fg="white"
    ).grid(row=3, column=1, sticky=tk.W + tk.E, pady=5)

    tk.Button(
        btnframe,
        text="Purple Mode",
        font=("Arial", 18),
        command=purplemode,
        bg="purple",
        fg="white"
    ).grid(row=4, column=1, sticky=tk.W + tk.E, pady=5)

    tk.Button(
        btnframe,
        text="Yellow Mode",
        font=("Arial", 18),
        command=yellowmode,
        bg="yellow",
        fg="black"
    ).grid(row=5, column=1, sticky=tk.W + tk.E, pady=5)

    tk.Button(
        btnframe,
        text="Normal",
        font=("Arial", 18),
        command=normal
    ).grid(row=6, column=1, sticky=tk.W + tk.E, pady=5)

    tk.Button(
        btnframe,
        text="Alice Blue Mode",
        font=("Arial", 18),
        command=alicebluemode,
        bg="#f0f8ff",
        fg="black"
    ).grid(row=1, column=2, sticky=tk.W + tk.E, pady=5)

    tk.Button(
        btnframe,
        text="Aqua Mode",
        font=("Arial", 18),
        command=aquamode,
        bg="aqua",
        fg="black"
    ).grid(row=2, column=2, sticky=tk.W + tk.E, pady=5)

    tk.Button(
        btnframe,
        text="Chocolate Mode",
        font=("Arial", 18),
        command=chocolatemode,
        bg="chocolate",
        fg="white"
    ).grid(row=3, column=2, sticky=tk.W + tk.E, pady=5)

    tk.Button(
        btnframe,
        text="Dark Blue Mode",
        font=("Arial", 18),
        command=darkbluemode,
        bg="#00008b",
        fg="white"
    ).grid(row=4, column=2, sticky=tk.W + tk.E, pady=5)

    tk.Button(
        btnframe,
        text="Dark Cyan Mode",
        font=("Arial", 18),
        command=darkcyanmode,
        bg="#008b8b",
        fg="white"
    ).grid(row=5, column=2, sticky=tk.W + tk.E, pady=5)

    tk.Button(
        btnframe,
        text="Dark Green Mode",
        font=("Arial", 18),
        command=darkgreenmode,
        bg="#006400",
        fg="white"
    ).grid(row=6, column=2, sticky=tk.W + tk.E, pady=5)

    tk.Button(
        btnframe,
        text="Dark Red Mode",
        font=("Arial", 18),
        command=darkredmode,
        bg="#8b0000",
        fg="white"
    ).grid(row=7, column=1, sticky=tk.W + tk.E, pady=5)

    tk.Button(
        btnframe,
        text="Brick Mode",
        font=("Arial", 18),
        command=brickmode,
        bg="#b22222",
        fg="white"
    ).grid(row=7, column=2, sticky=tk.W + tk.E, pady=5)

    tk.Button(
        btnframe,
        text="Gold Mode",
        font=("Arial", 18),
        command=goldmode,
        bg="gold",
        fg="black"
    ).grid(row=8, column=1, sticky=tk.W + tk.E, pady=5)

    tk.Button(
        btnframe,
        text="Light Slate Blue Mode",
        font=("Arial", 18),
        command=lightslatebluemode,
        bg="#8470ff",
        fg="white"
    ).grid(row=8, column=2, sticky=tk.W + tk.E, pady=5)

    btnframe.pack(fill="x", padx=20)
