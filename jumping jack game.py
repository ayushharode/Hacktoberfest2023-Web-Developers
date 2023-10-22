import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
JACK_WIDTH, JACK_HEIGHT = 50, 100
JACK_COLOR = (255, 0, 0)
GROUND_HEIGHT = 50
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50
OBSTACLE_COLOR = (0, 255, 0)
JUMP_HEIGHT = 200
GRAVITY = 1

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping Jack Game")

# Initialize Jumping Jack
jack_x = WIDTH // 2 - JACK_WIDTH // 2
jack_y = HEIGHT - GROUND_HEIGHT - JACK_HEIGHT
jumping = False
jump_height = 0

# Create obstacles
obstacles = []

# Game Loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not jumping:
        jumping = True
        jump_height = 0

    if jumping:
        jack_y -= 5
        jump_height += 5
        if jump_height == JUMP_HEIGHT:
            jumping = False

    if not jumping and jack_y < HEIGHT - GROUND_HEIGHT - JACK_HEIGHT:
        jack_y += 5

    # Generate obstacles
    if len(obstacles) == 0 or obstacles[-1][1] > 100:
        obstacles.append([WIDTH, HEIGHT - GROUND_HEIGHT - OBSTACLE_HEIGHT])

    # Move obstacles
    new_obstacles = []
    for obstacle in obstacles:
        obstacle[0] -= 5
        if obstacle[0] + OBSTACLE_WIDTH > 0:
            new_obstacles.append(obstacle)
    obstacles = new_obstacles

    # Check for collision with obstacles
    for obstacle in obstacles:
        if (
            jack_x < obstacle[0] + OBSTACLE_WIDTH
            and jack_x + JACK_WIDTH > obstacle[0]
            and jack_y < obstacle[1] + OBSTACLE_HEIGHT
            and jack_y + JACK_HEIGHT > obstacle[1]
        ):
            pygame.quit()
            sys.exit()

    # Draw the screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))
    pygame.draw.rect(screen, JACK_COLOR, (jack_x, jack_y, JACK_WIDTH, JACK_HEIGHT))

    for obstacle in obstacles:
        pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle[0], obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    pygame.display.update()
    clock.tick(30)
