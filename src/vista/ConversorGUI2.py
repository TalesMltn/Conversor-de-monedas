import tkinter as tk
from tkinter import ttk, messagebox
from src.logica.conversor import ConversorMoneda

class ConversorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Monedas")
        self.root.geometry("400x250")
        self.root.configure(bg="#f2f2f2")  # Color de fondo de la ventana principal
        self.conversor = ConversorMoneda()

        # Configuración de estilo
        style = ttk.Style(self.root)
        style.theme_use("clam")  # Usa el tema 'clam' que es moderno y limpio

        # Personalizar colores y fuentes de los widgets
        style.configure("TFrame", background="#f2f2f2")
        style.configure("TLabel", background="#f2f2f2", font=("Arial", 12))
        style.configure("TButton", background="#4CAF50", foreground="white", font=("Arial", 10, "bold"))
        style.map("TButton", background=[("active", "#45a049")])
        style.configure("TEntry", font=("Arial", 12))

        # Frame principal con padding
        self.frame = ttk.Frame(root, padding="20 20 20 20")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Etiqueta y entrada de monto
        ttk.Label(self.frame, text="Monto:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.monto_entry = ttk.Entry(self.frame, width=15)
        self.monto_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

        # Etiqueta y selección de moneda de origen
        ttk.Label(self.frame, text="De:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.origen_combo = ttk.Combobox(self.frame, values=['USD', 'EUR', 'JPY'], width=13, font=("Arial", 12))
        self.origen_combo.grid(row=1, column=1, sticky=tk.W, pady=5)
        self.origen_combo.current(0)

        # Etiqueta y selección de moneda de destino
        ttk.Label(self.frame, text="A:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.destino_combo = ttk.Combobox(self.frame, values=['USD', 'EUR', 'JPY'], width=13, font=("Arial", 12))
        self.destino_combo.grid(row=2, column=1, sticky=tk.W, pady=5)
        self.destino_combo.current(1)

        # Botón de conversión
        self.convertir_btn = ttk.Button(self.frame, text="Convertir", command=self.convertir)
        self.convertir_btn.grid(row=3, column=1, sticky=tk.W, pady=20)

        # Etiqueta de resultado
        self.resultado_label = ttk.Label(self.frame, text="Resultado: ", font=("Arial", 12, "italic"))
        self.resultado_label.grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=10)

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
