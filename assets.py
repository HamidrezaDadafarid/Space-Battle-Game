import os
import pygame
from config import WIDTH, HEIGHT, SPACESHIP_WIDTH, SPACESHIP_HEIGHT

# Initialize Pygame mixer and fonts
pygame.mixer.init()
pygame.font.init()

# Load sounds
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Grenade+1.mp3"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(
    os.path.join("Assets", "Gun+Silencer.mp3"))

# Load fonts
HEALTH_FONT = pygame.font.SysFont("Calibri", 40)
WINNER_FONT = pygame.font.SysFont("Calibri", 100)

# Load spaceship images and resize them
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

# Load background image and resize it
SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "space2.png")), (WIDTH, HEIGHT))

# Define border
BORDER = pygame.Rect((WIDTH - 10) // 2, 0, 10, HEIGHT)
