import pygame
import random

# Inicialización
pygame.init()
pantalla = pygame.display.set_mode((800, 600))
reloj = pygame.time.Clock()

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
