import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle properties
paddle_width = 10
paddle_height = 100
paddle_speed = 7

# Left paddle
left_paddle_x = 10
left_paddle_y = (HEIGHT - paddle_height) // 2

# Right paddle
right_paddle_x = WIDTH - paddle_width - 10
right_paddle_y = (HEIGHT - paddle_height) // 2

# Ball properties
ball_size = 15
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

# Scores
score_left = 0
score_right = 0
font = pygame.font.SysFont(None, 36)

# Game loop flag
running = True

clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()
    # Left paddle (W and S keys)
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - paddle_height:
        left_paddle_y += paddle_speed
    # Right paddle (Up and Down arrow keys)
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - paddle_height:
        right_paddle_y += paddle_speed

    # Draw paddles
    left_paddle = pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height)
    right_paddle = pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y >= HEIGHT - ball_size:
        ball_speed_y *= -1

    # Ball collision with paddles
    ball_rect = pygame.Rect(ball_x, ball_y, ball_size, ball_size)
    if ball_rect.colliderect(left_paddle) or ball_rect.colliderect(right_paddle):
        ball_speed_x *= -1

    # Ball goes out of bounds
    if ball_x <= 0:
        score_right += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    if ball_x >= WIDTH - ball_size:
        score_left += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2

    # Draw ball
    pygame.draw.rect(screen, WHITE, ball_rect)

    # Display scores
    score_text = font.render(f"{score_left} : {score_right}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)
