import tkinter as tk
import random

# Cree la ventana
ventana = tk.Tk()
ventana.title("Space Shooter")
ventana.resizable(False, False)

# Cree el canvas
ANCHO = 400
ALTO = 500
canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO, bg="black")
canvas.pack()

# aqui cree la nave
nave = canvas.create_rectangle(180, 450, 220, 480, fill="cyan")

# aqui cree el enemigo
enemigo = canvas.create_rectangle(180, 50, 220, 80, fill="red")

# aqui le di las Velocidades al enemigo y a la nave
velocidad_nave = 20
velocidad_enemigo = 5



 