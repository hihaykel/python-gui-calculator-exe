import tkinter as tk

# ---------- Colors (modern dark theme) ----------
BG_COLOR = "#1e1e2e"
SCREEN_COLOR = "#282a3a"
TEXT_COLOR = "#ffffff"
NUM_BUTTON_COLOR = "#3b3f5c"
NUM_BUTTON_HOVER = "#4b4f6c"
OP_BUTTON_COLOR = "#f5a623"
OP_BUTTON_HOVER = "#ffb84d"
EQUAL_BUTTON_COLOR = "#00c896"
EQUAL_BUTTON_HOVER = "#00e0ac"
CLEAR_BUTTON_COLOR = "#e74c3c"
CLEAR_BUTTON_HOVER = "#ff6b5b"

SCREEN_FONT = ("Segoe UI", 32, "bold")
BUTTON_FONT = ("Segoe UI", 16, "bold")


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("360x520")
        self.resizable(False, False)
        self.configure(bg=BG_COLOR)

        self.expression = ""
        self.create_screen()
        self.create_buttons()

    # ---------- Display screen ----------
    def create_screen(self):
        screen_frame = tk.Frame(self, bg=SCREEN_COLOR, height=120)
        screen_frame.pack(fill="both", padx=15, pady=(20, 10))

        self.screen_var = tk.StringVar(value="0")
        screen_label = tk.Label(
            screen_frame,
            textvariable=self.screen_var,
            anchor="e",
            bg=SCREEN_COLOR,
            fg=TEXT_COLOR,
            font=SCREEN_FONT,
            padx=15,
            pady=25,
        )
        screen_label.pack(fill="both")

    # ---------- Buttons ----------
    def create_buttons(self):
        buttons_frame = tk.Frame(self, bg=BG_COLOR)
        buttons_frame.pack(expand=True, fill="both", padx=15, pady=10)

        # Button layout (text, row, column, colspan, color, hover_color)
        buttons = [
            ("C", 0, 0, 1, CLEAR_BUTTON_COLOR, CLEAR_BUTTON_HOVER),
            ("⌫", 0, 1, 1, CLEAR_BUTTON_COLOR, CLEAR_BUTTON_HOVER),
            ("%", 0, 2, 1, OP_BUTTON_COLOR, OP_BUTTON_HOVER),
            ("÷", 0, 3, 1, OP_BUTTON_COLOR, OP_BUTTON_HOVER),

            ("7", 1, 0, 1, NUM_BUTTON_COLOR, NUM_BUTTON_HOVER),
            ("8", 1, 1, 1, NUM_BUTTON_COLOR, NUM_BUTTON_HOVER),
            ("9", 1, 2, 1, NUM_BUTTON_COLOR, NUM_BUTTON_HOVER),
            ("×", 1, 3, 1, OP_BUTTON_COLOR, OP_BUTTON_HOVER),

            ("4", 2, 0, 1, NUM_BUTTON_COLOR, NUM_BUTTON_HOVER),
            ("5", 2, 1, 1, NUM_BUTTON_COLOR, NUM_BUTTON_HOVER),
            ("6", 2, 2, 1, NUM_BUTTON_COLOR, NUM_BUTTON_HOVER),
            ("-", 2, 3, 1, OP_BUTTON_COLOR, OP_BUTTON_HOVER),

            ("1", 3, 0, 1, NUM_BUTTON_COLOR, NUM_BUTTON_HOVER),
            ("2", 3, 1, 1, NUM_BUTTON_COLOR, NUM_BUTTON_HOVER),
            ("3", 3, 2, 1, NUM_BUTTON_COLOR, NUM_BUTTON_HOVER),
            ("+", 3, 3, 1, OP_BUTTON_COLOR, OP_BUTTON_HOVER),

            ("0", 4, 0, 2, NUM_BUTTON_COLOR, NUM_BUTTON_HOVER),
            (".", 4, 2, 1, NUM_BUTTON_COLOR, NUM_BUTTON_HOVER),
            ("=", 4, 3, 1, EQUAL_BUTTON_COLOR, EQUAL_BUTTON_HOVER),
        ]

        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)
        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)

        for (text, row, column, colspan, color, hover_color) in buttons:
            self.create_button(buttons_frame, text, row, column, colspan, color, hover_color)

    def create_button(self, parent, text, row, column, colspan, color, hover_color):
        button = tk.Button(
            parent,
            text=text,
            font=BUTTON_FONT,
            fg=TEXT_COLOR,
            bg=color,
            activebackground=hover_color,
            activeforeground=TEXT_COLOR,
            relief="flat",
            bd=0,
            command=lambda t=text: self.handle_click(t),
        )
        button.grid(
            row=row, column=column, columnspan=colspan,
            sticky="nsew", padx=6, pady=6, ipady=10
        )

        # Simple hover effect
        button.bind("<Enter>", lambda e, b=button, c=hover_color: b.config(bg=c))
        button.bind("<Leave>", lambda e, b=button, c=color: b.config(bg=c))

    # ---------- Calculator logic ----------
    def handle_click(self, value):
        if value == "C":
            self.expression = ""
        elif value == "⌫":
            self.expression = self.expression[:-1]
        elif value == "=":
            self.calculate()
            return
        else:
            symbols = {"×": "*", "÷": "/", "%": "/100*"}
            self.expression += symbols.get(value, value)

        self.update_screen()

    def update_screen(self):
        display = self.expression.replace("*", "×").replace("/", "÷")
        self.screen_var.set(display if display else "0")

    def calculate(self):
        try:
            result = eval(self.expression) if self.expression else 0
            self.screen_var.set(str(result))
            self.expression = str(result)
        except (SyntaxError, ZeroDivisionError, ValueError):
            self.screen_var.set("Error")
            self.expression = ""


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()