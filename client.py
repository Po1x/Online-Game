import socket
import time

import pygame

WIDTH = 700
HEIGHT = 500
FPS = 60
RADIUS = 50

def ball():
    pygame.draw.circle(screen, "red",(WIDTH / 2, HEIGHT / 2), RADIUS, width = 100)

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
main_socket.connect(('127.0.0.1', 51889))

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Agar.io")
clock = pygame.time.Clock()

old = (0,0)

run = True
while run:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            vector = pos[0] - WIDTH // 2, pos[1] - HEIGHT // 2

            if vector != old:
                old = vector
                main_socket.send(f"{vector[0]},{vector[1]}".encode())
    screen.fill('white')
    ball()
    pygame.display.flip()