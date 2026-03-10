## Importamos la librería tkinter para crear la ventana
import tkinter as tk

# Importamos la clase AppGaraje desde la carpeta ui
from ui.app_tkinter import AppGaraje


# Función principal que inicia la aplicación
def main():

    # Crear la ventana principal del programa
    root = tk.Tk()

    # Crear la aplicación pasando la ventana como parámetro
    app = AppGaraje(root)

    # Ejecutar el bucle principal de la interfaz gráfica
    root.mainloop()


# Verifica que este archivo se está ejecutando directamente
if __name__ == "__main__":
    main()