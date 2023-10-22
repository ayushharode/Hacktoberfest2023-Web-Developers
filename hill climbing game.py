import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
HILL_HEIGHT = 100
PLAYER_SIZE = 20
PLAYER_COLOR = (255, 0, 0)
HILL_COLOR = (0, 255, 0)
GRAVITY = 1

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hill Climbing Game")

# Initialize player
player_x = WIDTH // 2
player_y = HEIGHT - HILL_HEIGHT - PLAYER_SIZE

# Initialize hill
hill_x = 0
hill_height = HILL_HEIGHT

# Player velocity
player_velocity = 0

# Game Loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += 5

    # Gravity logic
    if player_y < HEIGHT - HILL_HEIGHT - PLAYER_SIZE:
        player_velocity += GRAVITY
    else:
        player_velocity = 0
        player_y = HEIGHT - HILL_HEIGHT - PLAYER_SIZE

    # Check if the player is climbing the hill
    if player_x >= hill_x and player_x <= hill_x + hill_height:
        if player_y + PLAYER_SIZE > HEIGHT - hill_height + hill_x:
            player_y = HEIGHT - hill_height + hill_x - PLAYER_SIZE

    # Draw the screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, HILL_COLOR, (hill_x, HEIGHT - hill_height, hill_height, hill_height))
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))
    pygame.display.update()

    clock.tick(30)
