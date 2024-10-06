import tkinter as ui

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.result = ui.StringVar()

        self.display = ui.Entry(master, textvariable=self.result, font=('Arial', 16), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)

    
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            ui.Button(master, text=button, padx=20, pady=20, command=action, font=('Arial', 16)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                self.result.set(eval(self.result.get()))
            except Exception as e:
                self.result.set("Error")
        else:
            current_text = self.result.get()
            self.result.set(current_text + char)

if __name__ == "__main__":
    root = ui.Tk()
    calculator = Calculator(root)
    root.mainloop()
