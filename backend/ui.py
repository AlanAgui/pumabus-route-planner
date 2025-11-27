import tkinter as tk
from tkinter import ttk, messagebox

from pumabus import construir_grafo_pumabus
from dijkstra import dijkstra


def construir_backend():
    """Construye el grafo del Pumabús y regresa el grafo y la lista de paradas."""
    grafo = construir_grafo_pumabus()
    paradas = sorted(grafo.list_adj.keys())
    return grafo, paradas


class AppPumabus(tk.Tk):
    def __init__(self, grafo, paradas):
        super().__init__()

        self.grafo = grafo
        self.paradas_completas = sorted(paradas)

        # Ventana principal
        self.title("Sistema de Rutas Pumabús - CU")
        self.geometry("800x500")
        self.minsize(700, 400)

        # Color de fondo
        self.configure(bg="#0f172a")

        # Estilo básico ttk
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except Exception:
            pass

        style.configure(
            "Titulo.TLabel",
            font=("Segoe UI", 18, "bold"),
            foreground="#e5e7eb"
        )
        style.configure(
            "Resultado.TLabel",
            font=("Segoe UI", 11),
            foreground="#e5e7eb"
        )
        style.configure(
            "TFrame",
            background="#0f172a"
        )
        style.configure(
            "TLabel",
            background="#0f172a",
            foreground="#e5e7eb"
        )
        style.configure(
            "TButton",
            padding=5
        )

        # Variables de la interfaz
        self.origen_var = tk.StringVar()
        self.destino_var = tk.StringVar()
        self.resultado_var = tk.StringVar()

        self._crear_widgets()

        # Enter = calcular ruta
        self.bind("<Return>", lambda event: self.calcular_ruta())

    def _crear_widgets(self):
        """Crea los controles de la interfaz gráfica."""

        frame_titulo = ttk.Frame(self, padding=(10, 10, 10, 5))
        frame_titulo.pack(fill="x")

        label_titulo = ttk.Label(
            frame_titulo,
            text="Sistema de Rutas Pumabús (CU)",
            style="Titulo.TLabel"
        )
        label_titulo.pack(anchor="center")

        frame_form = ttk.Frame(self, padding=10)
        frame_form.pack(fill="x")

        label_origen = ttk.Label(frame_form, text="Origen:")
        label_destino = ttk.Label(frame_form, text="Destino:")

        self.combo_origen = ttk.Combobox(
            frame_form,
            textvariable=self.origen_var,
            values=self.paradas_completas,
            state="readonly",
            cursor="hand2"
        )
        self.combo_destino = ttk.Combobox(
            frame_form,
            textvariable=self.destino_var,
            values=self.paradas_completas,
            state="readonly",
            cursor="hand2"
        )

        boton_calcular = ttk.Button(
            frame_form,
            text="Calcular ruta",
            command=self.calcular_ruta,
            cursor="hand2"
        )
        boton_intercambiar = ttk.Button(
            frame_form,
            text="Intercambiar origen/destino",
            command=self.intercambiar_paradas,
            cursor="hand2"
        )
        boton_limpiar = ttk.Button(
            frame_form,
            text="Limpiar",
            command=self.limpiar,
            cursor="hand2"
        )

        label_origen.grid(row=0, column=0, padx=5, pady=(5, 2), sticky="w")
        self.combo_origen.grid(row=0, column=1, padx=5, pady=(5, 2), sticky="ew")

        label_destino.grid(row=1, column=0, padx=5, pady=(5, 2), sticky="w")
        self.combo_destino.grid(row=1, column=1, padx=5, pady=(5, 2), sticky="ew")

        boton_calcular.grid(row=2, column=0, columnspan=2, pady=(10, 4))
        boton_intercambiar.grid(row=3, column=0, columnspan=2, pady=2)
        boton_limpiar.grid(row=4, column=0, columnspan=2, pady=(2, 5))

        frame_form.columnconfigure(1, weight=1)

        # Abrir lista al hacer clic
        self.combo_origen.bind(
            "<Button-1>",
            lambda e: self._abrir_dropdown_click(self.combo_origen)
        )
        self.combo_destino.bind(
            "<Button-1>",
            lambda e: self._abrir_dropdown_click(self.combo_destino)
        )

        # Cerrar lista al seleccionar
        self.combo_origen.bind(
            "<<ComboboxSelected>>",
            lambda e: self._cerrar_dropdown(self.combo_origen)
        )
        self.combo_destino.bind(
            "<<ComboboxSelected>>",
            lambda e: self._cerrar_dropdown(self.combo_destino)
        )

        frame_result = ttk.Frame(self, padding=(10, 0, 10, 10))
        frame_result.pack(fill="both", expand=True)

        label_resultado_titulo = ttk.Label(
            frame_result,
            text="Resultado:"
        )
        label_resultado_titulo.pack(anchor="w", pady=(5, 2))

        self.label_resultado = ttk.Label(
            frame_result,
            textvariable=self.resultado_var,
            style="Resultado.TLabel",
            justify="left",
            anchor="nw",
            wraplength=760
        )
        self.label_resultado.pack(fill="both", expand=True)

        self.resultado_var.set(
            "Selecciona una parada de origen y otra de destino.\n"
            "Después haz clic en 'Calcular ruta'."
        )

    def _abrir_dropdown_click(self, combobox):
        """Abre la lista de opciones del combobox al hacer clic."""
        try:
            combobox.tk.call("ttk::combobox::Post", combobox)
        except Exception:
            pass

    def _cerrar_dropdown(self, combobox):
        """Cierra la lista de opciones después de seleccionar."""
        combobox.selection_clear()
        self.focus()

    def calcular_ruta(self):
        """Calcula la ruta más corta entre origen y destino seleccionados."""
        origen = self.origen_var.get().strip()
        destino = self.destino_var.get().strip()

        if not origen or not destino:
            messagebox.showwarning(
                "Datos incompletos",
                "Selecciona tanto el origen como el destino."
            )
            return

        if origen not in self.grafo.list_adj:
            messagebox.showerror(
                "Parada no encontrada",
                f"La parada '{origen}' no está registrada en el sistema."
            )
            return

        if destino not in self.grafo.list_adj:
            messagebox.showerror(
                "Parada no encontrada",
                f"La parada '{destino}' no está registrada en el sistema."
            )
            return

        try:
            distancia, ruta = dijkstra(self.grafo, origen, destino)

            if ruta:
                texto_ruta = " → ".join(ruta)
                self.resultado_var.set(
                    f"Ruta más corta de {origen} a {destino}:\n\n"
                    f"{texto_ruta}\n\n"
                    f"Distancia total: {distancia:.2f} km"
                )
            else:
                self.resultado_var.set(
                    f"No existe ruta entre '{origen}' y '{destino}'."
                )
        except Exception as e:
            print("Error inesperado en calcular_ruta:", e)
            messagebox.showerror(
                "Error inesperado",
                f"Ocurrió un problema no contemplado:\n{e}"
            )

    def intercambiar_paradas(self):
        """Intercambia los valores de origen y destino."""
        origen_actual = self.origen_var.get()
        destino_actual = self.destino_var.get()
        self.origen_var.set(destino_actual)
        self.destino_var.set(origen_actual)

    def limpiar(self):
        """Limpia los campos y el resultado."""
        self.origen_var.set("")
        self.destino_var.set("")
        self.combo_origen["values"] = self.paradas_completas
        self.combo_destino["values"] = self.paradas_completas
        self.resultado_var.set(
            "Selecciona una parada de origen y otra de destino.\n"
            "Después haz clic en 'Calcular ruta'."
        )


def main():
    grafo, paradas = construir_backend()
    app = AppPumabus(grafo, paradas)
    app.mainloop()


if __name__ == "__main__":
    main()