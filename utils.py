import pygame
from config import WIDTH, HEIGHT, WHITE, BLACK
from assets import SPACE, HEALTH_FONT, WINNER_FONT, YELLOW_SPACESHIP, RED_SPACESHIP, BORDER


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    """Draws the game window with all elements (spaceships, bullets, health, etc.)."""
    WIN = pygame.display.get_surface()  # Get the current display surface

    WIN.blit(SPACE, (0, 0))  # Draw background
    pygame.draw.rect(WIN, BLACK, BORDER)  # Draw the border

    # Draw health text
    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    # Draw spaceships
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    # Draw bullets
    for bullet in red_bullets:
        pygame.draw.rect(WIN, (255, 0, 0), bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, (255, 255, 0), bullet)

    pygame.display.update()  # Refresh the display


def draw_winner(text):
    """Displays the winning text."""
    WIN = pygame.display.get_surface()  # Get the current display surface
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH // 2 - draw_text.get_width() //
             2, HEIGHT // 2 - draw_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(5000)  # Pause for 5 seconds
