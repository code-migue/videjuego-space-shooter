import tkinter as tk
import random

# Inicialización
pygame.init()
pantalla = pygame.display.set_mode((800, 600))
reloj = pygame.time.Clock()

# Cree la ventana
ventana = tk.Tk()
ventana.title("Space Shooter")
ventana.resizable(False, False)

# Objetos
jugador_rect = pygame.Rect(400, 550, 50, 40)
enemigo_rect = pygame.Rect(random.randrange(800), 50, 30, 30)
enemigo_velocidad = 2

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
            
    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador_rect.x -= 5
    if teclas[pygame.K_RIGHT]:
        jugador_rect.x += 5
    jugador_rect.clamp_ip(pantalla.get_rect())

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

ventana.mainloop()



 
