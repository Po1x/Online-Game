import socket
import time

import pygame

WIDTH = 700
HEIGHT = 500
FPS = 60


main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
main_socket.connect(('127.0.0.1', 51889))

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Agar.io")
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False