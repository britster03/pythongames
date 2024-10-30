import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click the Moving Object")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Object properties
obj_size = 50
obj_x = random.randint(0, WIDTH - obj_size)
obj_y = random.randint(0, HEIGHT - obj_size)
obj_speed_x = random.choice([-5, 5])
obj_speed_y = random.choice([-5, 5])

# Score and time
score = 0
start_time = pygame.time.get_ticks()
game_duration = 30000  # 30 seconds
font = pygame.font.SysFont(None, 36)

# Game loop flag
running = True

clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Time check
    elapsed_time = pygame.time.get_ticks() - start_time
    if elapsed_time >= game_duration:
        running = False

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            obj_rect = pygame.Rect(obj_x, obj_y, obj_size, obj_size)
            if obj_rect.collidepoint(mouse_pos):
                score += 1
                # Move object to a new random position
                obj_x = random.randint(0, WIDTH - obj_size)
                obj_y = random.randint(0, HEIGHT - obj_size)
                obj_speed_x = random.choice([-5, 5])
                obj_speed_y = random.choice([-5, 5])

    # Move object
    obj_x += obj_speed_x
    obj_y += obj_speed_y

    # Bounce off walls
    if obj_x <= 0 or obj_x >= WIDTH - obj_size:
        obj_speed_x *= -1
    if obj_y <= 0 or obj_y >= HEIGHT - obj_size:
        obj_speed_y *= -1

    # Draw object
    pygame.draw.rect(screen, BLUE, (obj_x, obj_y, obj_size, obj_size))

    # Display score and time
    score_text = font.render(f"Score: {score}", True, BLUE)
    time_left = max(0, (game_duration - elapsed_time) // 1000)
    time_text = font.render(f"Time Left: {time_left}s", True, BLUE)
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 50))

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Game over screen
screen.fill(WHITE)
game_over_text = font.render(f"Game Over! Final Score: {score}", True, BLUE)
screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
