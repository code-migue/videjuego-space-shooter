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

#  para Mover la nave
def mover_nave(event):
    if event.keysym == "Left":
        canvas.move(nave, -velocidad_nave, 0)
    elif event.keysym == "Right":
        canvas.move(nave, velocidad_nave, 0)

# Mover el enemigo
def mover_enemigo():
    canvas.move(enemigo, 0, velocidad_enemigo)
    x1, y1, x2, y2 = canvas.coords(enemigo)
    
    # Si el enemigo sale de la pantalla, reinicia arriba
    if y2 > ALTO:
        nuevo_x = random.randint(50, ANCHO-50)
        canvas.coords(enemigo, nuevo_x, 50, nuevo_x+40, 80)
    
    ventana.after(50, mover_enemigo)

# Controles
ventana.bind("<Left>", mover_nave)
ventana.bind("<Right>", mover_nave)

# Iniciar movimiento del enemigo
mover_enemigo()

# Texto puntaje
texto_puntaje = canvas.create_text(10, 10, anchor="nw", fill="white", font=("Arial", 14),
                                   text=f"Puntaje: {puntaje}")

# Mover nave
def mover_nave(event):
    if event.keysym == "Left":
        canvas.move(nave, -velocidad_nave, 0)
    elif event.keysym == "Right":
        canvas.move(nave, velocidad_nave, 0)

# Disparar
def disparar(event):
    x1, y1, x2, y2 = canvas.coords(nave)
    bala = canvas.create_rectangle((x1+x2)//2 - 2, y1-10, (x1+x2)//2 + 2, y1, fill="yellow")
    balas.append(bala)

# Actualizar juego
def actualizar():
    global puntaje

    # Mover balas
    for bala in balas[:]:
        canvas.move(bala, 0, velocidad_bala)
        x1, y1, x2, y2 = canvas.coords(bala)
        if y2 < 0:
            canvas.delete(bala)
            balas.remove(bala)

    # Mover enemigos
    for enemigo in enemigos:
        canvas.move(enemigo, 0, velocidad_enemigo)
        ex1, ey1, ex2, ey2 = canvas.coords(enemigo)

        # Si enemigo llega abajo → reaparece arriba
        if ey2 > ALTO:
            nuevo_x = random.randint(50, ANCHO-50)
            canvas.coords(enemigo, nuevo_x, 50, nuevo_x+30, 80)

        # Detectar colisión con balas
        for bala in balas[:]:
            bx1, by1, bx2, by2 = canvas.coords(bala)
            if (bx1 < ex2 and bx2 > ex1 and by1 < ey2 and by2 > ey1):
                # Eliminar enemigo y bala
                canvas.delete(bala)
                balas.remove(bala)

                nuevo_x = random.randint(50, ANCHO-50)
                canvas.coords(enemigo, nuevo_x, 50, nuevo_x+30, 80)

                puntaje += 10
                canvas.itemconfig(texto_puntaje, text=f"Puntaje: {puntaje}")

    ventana.after(50, actualizar)

# Controles
ventana.bind("<Left>", mover_nave)
ventana.bind("<Right>", mover_nave)
ventana.bind("<space>", disparar)

# Iniciar loop
actualizar()
ventana.mainloop()

 
