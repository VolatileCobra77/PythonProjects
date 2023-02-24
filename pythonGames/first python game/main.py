import pygame

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Apple Game")

# Load the apple image
apple_image = pygame.image.load("Apple.png")

# Set up the initial position of the apple
apple_x = WIDTH // 2
apple_y = HEIGHT // 2

# Set up the speed of the apple
apple_speed = 5

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Check for arrow key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        apple_x -= apple_speed
    if keys[pygame.K_RIGHT]:
        apple_x += apple_speed
    if keys[pygame.K_UP]:
        apple_y -= apple_speed
    if keys[pygame.K_DOWN]:
        apple_y += apple_speed

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the apple
    screen.blit(apple_image, (apple_x, apple_y))

    # Update the display
    pygame.display.update()
