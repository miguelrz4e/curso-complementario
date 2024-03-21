import tkinter as tk

class CafeteriaApp:
    def __init__(self, master):
        self.master = master
        master.title("babaria")

        self.label = tk.Label(master, text="¡Bienvenido a babaria!")
        self.label.pack()

        self.nombre_label = tk.Label(master, text="Ingrese su nombre:")
        self.nombre_label.pack()

        self.nombre_entry = tk.Entry(master)
        self.nombre_entry.pack()

        self.menu_items = {
            "poker",
            "aguila",
            "poni malta",
            "costeña",
            "corona"
        }

        self.selected_items = {}

        self.menu_frame = tk.Frame(master)
        self.menu_frame.pack()

        for item in self.menu_items:
            item_label = tk.Label(self.menu_frame, text=item)
            item_label.pack()

            add_button = tk.Button(self.menu_frame, text="Agregar", command=lambda i=item: self.agregar_item(i))
            add_button.pack()

        self.seleccionados_label = tk.Label(master, text="Artículos seleccionados:")
        self.seleccionados_label.pack()

        self.seleccionados_text = tk.Text(master, height=10, width=50)
        self.seleccionados_text.pack()

        self.boton_salir = tk.Button(master, text="Salir", command=master.quit)
        self.boton_salir.pack()

    def agregar_item(self, item):
        if item in self.selected_items:
            self.selected_items[item] += 1
        else:
            self.selected_items[item] = 1

        self.actualizar_seleccionados_text()

    def actualizar_seleccionados_text(self):
        nombre_usuario = self.nombre_entry.get()
        self.seleccionados_text.delete(1.0, tk.END)
        for item, cantidad in self.selected_items.items():
            self.seleccionados_text.insert(tk.END, f"{nombre_usuario}: {item}: {cantidad}\n")

root = tk.Tk()
app = CafeteriaApp(root)
root.mainloop()

