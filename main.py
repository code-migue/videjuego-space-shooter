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

Melo
velocidad_enemigo = 5



 
