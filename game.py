import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAR_WIDTH = 50
CAR_HEIGHT = 100
OBSTACLE_WIDTH = 10
OBSTACLE_HEIGHT = 100
SPEED = 7
OBSTACLE_SPEED = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racing Car Game")

# Load car image
car_image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
car_image.fill(GREEN)

# Function to draw the car
def draw_car(x, y):
    screen.blit(car_image, (x, y))

# Function to draw obstacles
def draw_obstacle(obstacle_x, obstacle_y):
    pygame.draw.rect(screen, RED, [obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT])

# Main game loop
def game_loop():
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT - CAR_HEIGHT - 10
    x_change = 0

    obstacles = []
    score = 0
    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            x_change = -SPEED
        elif keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - CAR_WIDTH:
            x_change = SPEED
        else:
            x_change = 0

        x += x_change

        # Add new obstacles
        if random.randint(1, 20) == 1:
            obstacle_x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
            obstacles.append([obstacle_x, 0])

        # Move obstacles down
        for obstacle in obstacles:
            obstacle[1] += OBSTACLE_SPEED
            if obstacle[1] > SCREEN_HEIGHT:
                obstacles.remove(obstacle)
                score += 1

        # Check for collisions
        for obstacle in obstacles:
            if (obstacle[0] < x < obstacle[0] + OBSTACLE_WIDTH or
                obstacle[0] < x + CAR_WIDTH < obstacle[0] + OBSTACLE_WIDTH) and \
               (obstacle[1] < y < obstacle[1] + OBSTACLE_HEIGHT or
                obstacle[1] < y + CAR_HEIGHT < obstacle[1] + OBSTACLE_HEIGHT):
                game_over = True

        # Draw everything
        screen.fill(WHITE)
        draw_car(x, y)
        for obstacle in obstacles:
            draw_obstacle(obstacle[0], obstacle[1])

        # Display score
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Start the game
if __name__ == "__main__":
    game_loop()
