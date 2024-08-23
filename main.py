import pygame
from config import WIDTH, HEIGHT, SPACESHIP_WIDTH, SPACESHIP_HEIGHT, FPS, MAX_BULLETS, YELLOW_HIT, RED_HIT
from assets import BULLET_FIRE_SOUND, BULLET_HIT_SOUND
from handler import yellow_movement_handler, red_movement_handler, bullets_handler
from utils import draw_window, draw_winner


def main():
    # Set up the game window
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Battle Game")

    # Initialize positions for spaceships
    red = pygame.Rect(950, (HEIGHT - SPACESHIP_HEIGHT) //
                      2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(200, (HEIGHT - SPACESHIP_HEIGHT) //
                         2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    # Set up clock, bullets, and health
    clock = pygame.time.Clock()
    red_bullets = []
    yellow_bullets = []
    red_health = 10
    yellow_health = 10
    run = True

    # Main game loop
    while run:
        clock.tick(FPS)  # Control the game's frame rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # Shooting bullets
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height // 2 - 3, 10, 6)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height // 2 - 3, 10, 6)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            # Handle bullet hits
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        # Check for a winner
        winner_text = ""
        if red_health == 0:
            winner_text = "Yellow Wins!"
        if yellow_health == 0:
            winner_text = "Red Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            break

        # Update the display
        draw_window(red, yellow, red_bullets, yellow_bullets,
                    red_health, yellow_health)
        keys_pressed = pygame.key.get_pressed()
        yellow_movement_handler(keys_pressed, yellow)
        red_movement_handler(keys_pressed, red)
        bullets_handler(yellow_bullets, red_bullets, yellow, red)

    main()  # Restart the game


if __name__ == "__main__":
    main()  # Run the game
