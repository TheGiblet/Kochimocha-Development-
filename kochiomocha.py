import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Kochiomocha AI Pet")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Load Kochiomocha images (replace with your actual image files)
kochiomocha_img = pygame.image.load("kochiomocha.png")
kochiomocha_width = 100
kochiomocha_height = 100
kochiomocha_x = screen_width // 2 - kochiomocha_width // 2
kochiomocha_y = screen_height // 2 - kochiomocha_height // 2

# Animation variables
animation_speed = 0.1  # Adjust for animation speed
animation_frame = 0

# FPS (Frames Per Second)
fps = 60
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                kochiomocha_x -= 5
            if event.key == pygame.K_RIGHT:
                kochiomocha_x += 5
            if event.key == pygame.K_UP:
                kochiomocha_y -= 5
            if event.key == pygame.K_DOWN:
                kochiomocha_y += 5
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # You can use mouse position for interactions later

    # Keep Kochiomocha within screen bounds
    kochiomocha_x = max(0, min(kochiomocha_x, screen_width - kochiomocha_width))
    kochiomocha_y = max(0, min(kochiomocha_y, screen_height - kochiomocha_height))

    # Clear the screen
    screen.fill(white)

    # Basic animation (replace with your animation logic)
    animation_frame += animation_speed
    if animation_frame >= 4:  # Assuming you have 4 frames
        animation_frame = 0

    # Draw Kochiomocha (replace with your drawing logic)
    screen.blit(kochiomocha_img, (kochiomocha_x, kochiomocha_y),
                (int(animation_frame) * kochiomocha_width, 0, kochiomocha_width, kochiomocha_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)

pygame.quit()
