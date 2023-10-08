import pygame
import os
import random
import sys

pygame.init()

# Initialize the window
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Animations
RUNNING = [
    pygame.image.load("Assets/Dino/DinoRun1.png"),
    pygame.image.load("Assets/Dino/DinoRun2.png"),
]

JUMPING = pygame.image.load("Assets/Dino/DinoJump.png")

BG = pygame.image.load("Assets/Other/Track.png")

FONT = pygame.font.Font('freesansbold.ttf', 220)

def main():
    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill((255, 255, 255))
        clock.tick(30)
        pygame.display.update()

main()