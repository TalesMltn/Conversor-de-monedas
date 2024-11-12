import tkinter as tk
from tkinter import ttk, messagebox
from src.logica.conversor import ConversorMoneda


class ConversorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Monedas")
        self.root.geometry("400x300")

        # Fondo degradado
        self.background = tk.Canvas(root, width=400, height=300)
        self.background.pack(fill="both", expand=True)
        self.background.create_rectangle(0, 0, 400, 300, outline="", fill="#d1e8e2")
        self.background.create_rectangle(0, 150, 400, 300, outline="", fill="#89c9b8")

        # Marco principal
        self.frame = ttk.Frame(root, padding="20 20 20 20", style="Custom.TFrame")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Configuración de estilo
        style = ttk.Style()
        style.theme_use("clam")

        # Estilo personalizado
        style.configure("Custom.TFrame", background="#f4f6f7")
        style.configure("Custom.TLabel", background="#f4f6f7", font=("Helvetica", 12))
        style.configure("Custom.TButton", background="#57a773", foreground="white", font=("Helvetica", 10, "bold"),
                        padding=5)
        style.map("Custom.TButton", background=[("active", "#45a049")])

        # Etiqueta de título
        self.title_label = ttk.Label(self.frame, text="Conversor de Monedas", font=("Helvetica", 16, "bold"),
                                     background="#f4f6f7", foreground="#4b6584")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Etiqueta y entrada de monto
        ttk.Label(self.frame, text="Monto:", style="Custom.TLabel").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.monto_entry = ttk.Entry(self.frame, width=15, font=("Helvetica", 12))
        self.monto_entry.grid(row=1, column=1, pady=5)

        # Etiqueta y selección de moneda de origen
        ttk.Label(self.frame, text="De:", style="Custom.TLabel").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.origen_combo = ttk.Combobox(self.frame, values=['USD', 'EUR', 'JPY'], width=13, font=("Helvetica", 12))
        self.origen_combo.grid(row=2, column=1, pady=5)
        self.origen_combo.current(0)

        # Etiqueta y selección de moneda de destino
        ttk.Label(self.frame, text="A:", style="Custom.TLabel").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.destino_combo = ttk.Combobox(self.frame, values=['USD', 'EUR', 'JPY'], width=13, font=("Helvetica", 12))
        self.destino_combo.grid(row=3, column=1, pady=5)
        self.destino_combo.current(1)

        # Botón de conversión
        self.convertir_btn = ttk.Button(self.frame, text="Convertir", command=self.convertir, style="Custom.TButton")
        self.convertir_btn.grid(row=4, column=0, columnspan=2, pady=(15, 10))

        # Etiqueta de resultado
        self.resultado_label = ttk.Label(self.frame, text="Resultado: ", font=("Helvetica", 12, "italic"),
                                         style="Custom.TLabel")
        self.resultado_label.grid(row=5, column=0, columnspan=2, sticky=tk.W, pady=(10, 0))

    def convertir(self):
        try:
            monto = float(self.monto_entry.get())
            moneda_origen = self.origen_combo.get()
            moneda_destino = self.destino_combo.get()
            resultado = self.conversor.convertir(monto, moneda_origen, moneda_destino)
            self.resultado_label.config(text=f"Resultado: {resultado:.2f} {moneda_destino}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorApp(root)
    root.mainloop()
