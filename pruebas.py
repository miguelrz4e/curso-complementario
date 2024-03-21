import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.display = tk.Entry(master, width=20, borderwidth=3, font=("Arial", 12))
        self.display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
            ("0", 4, 1),
            ("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3),
            ("C", 4, 0), ("=", 4, 2)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(master, text=text, padx=15, pady=15, font=("Arial", 10), command=lambda t=text: self.click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        self.valor_actual = ""

    def click(self, valor):
        if valor.isdigit():
            self.valor_actual += valor
            self.actualizar_display()
        elif valor in ("+", "-", "*", "/"):
            self.valor_actual += " " + valor + " "
            self.actualizar_display()
        elif valor == "=":
            try:
                resultado = eval(self.valor_actual)
                self.valor_actual = str(resultado)
                self.actualizar_display()
            except:
                self.valor_actual = "Error"
                self.actualizar_display()
        elif valor == "C":
            self.valor_actual = ""
            self.actualizar_display()

    def actualizar_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.valor_actual)


root = tk.Tk()
app = Calculadora(root)
root.mainloop()
