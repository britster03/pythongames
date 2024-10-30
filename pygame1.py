import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# setting up the screen dimensions
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# colors are defined using RGB tuples
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# properties of paddle
paddle_width = 100  #dimension of paddle
paddle_height = 20   #dimension of paddle
paddle_x = (WIDTH - paddle_width) // 2   # the horizontal starting pos of paddle - subtracting the paddles width with screen widht and div it by 2
paddle_y = HEIGHT - paddle_height - 10 # the vertical starting pos of paddle ( near the bottom part of screen) - subtracting the paddle's height and an additional 10 pixels from screen's height
paddle_speed = 7  # the number of pixels the paddle moves per frame when a key is pressed

# Ball properties
ball_radius = 15
ball_x = random.randint(ball_radius, WIDTH - ball_radius) # the horizontal starting pos of the ball
ball_y = -ball_radius # the vertical pos is set to negative the balls radius so that it falls from top of the screen
ball_speed = 5  # the number of pixel the ball moves per second

# Score
score = 0   # keeps track of the players score
font = pygame.font.SysFont(None, 36) 

# Game loop flag
running = True  # to control the main game loop, if set to false then the game exits the loop

clock = pygame.time.Clock() 

while running:
    screen.fill(WHITE)


    for event in pygame.event.get():  # retrieving the list of all events in event queue
        if event.type == pygame.QUIT: # if event is of type QUIT then game exits
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()  # here we get the dictionary of all the keyboard keys pressed
    if keys[pygame.K_LEFT] and paddle_x > 0: # if the left arrow key is pressed , we need to ensure that it doesnt go out of screen
        paddle_x -= paddle_speed # moving the paddle to left by subtracting the speed from the horizontal position
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width: # if the right arrow key is pressed , we need to ensure that it doesnt go out of screen>
        paddle_x += paddle_speed # moving the paddle to right by subtracting the speed from the horizontal position

    # Draw paddle
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height) # pygame.rect creates a rect obj rep paddles pos and size
    pygame.draw.rect(screen, BLACK, paddle_rect) 

    # Move ball
    ball_y += ball_speed  # incrementing the vertical pos to make it move downward

    # Draw ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius) # draw circle using pygame


    if ball_y + ball_radius >= paddle_y:   # if the bottom of the ball reaches the top of the paddle 
        if paddle_x <= ball_x <= paddle_x + paddle_width: # checking if the ball is above the paddle
            score += 1 # if the ball is caught by the paddle then we will inc the score by 1
            ball_x = random.randint(ball_radius, WIDTH - ball_radius) # now ball will fall from a different pos from above
            ball_y = -ball_radius 
            ball_speed += 0.5  # with each inc in score the difficult of game will also inc with inc speed
        elif ball_y > HEIGHT: # if ball goes out of the bottom part of screen 
            running = False  # then endgame


    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))


    pygame.display.flip()
    clock.tick(60) # max 50 frames per sec

# after game over
screen.fill(WHITE)
game_over_text = font.render(f"Game Over! Final Score: {score}", True, RED)
screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()

