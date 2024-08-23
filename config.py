import pygame

# Screen dimensions
WIDTH, HEIGHT = 1200, 700

# Spaceship dimensions
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Game settings
FPS = 90
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3

# Custom events
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
