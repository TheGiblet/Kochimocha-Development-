import pygame

# Import the response logic from response_logic.py
from response_logic import get_kochiomocha_response 

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

# Load Kochiomocha image (replace with your actual image file)
kochiomocha_img = pygame.image.load("kochiomocha.jpg")  # Replace with your image
kochiomocha_width = 600
kochiomocha_height = 400
kochiomocha_x = screen_width // 2 - kochiomocha_width // 2
kochiomocha_y = screen_height // 2 - kochiomocha_height // 2

# FPS (Frames Per Second)
fps = 60
clock = pygame.time.Clock()

# --- Text input variables ---
font = pygame.font.Font(None, 36)  # Default font, size 36
input_box = pygame.Rect(100, 500, 600, 50)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''

# --- Response display variables ---
response_font = pygame.font.Font(None, 30)
response_text = ""  # Store Kochiomocha's response
response_color = black
response_x = 100
response_y = 450

# --- NLTK setup (if not already downloaded in response_logic.py) ---
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')


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
            # --- Text input handling ---
            if active:
                if event.key == pygame.K_RETURN:
                    response_text = get_kochiomocha_response(text)  # Get response from response_logic.py
                    print("Kochiomocha says:", response_text)  # Print response to console
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            # --- Text input handling ---
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive

    # Keep Kochiomocha within screen bounds
    kochiomocha_x = max(0, min(kochiomocha_x, screen_width - kochiomocha_width))
    kochiomocha_y = max(0, min(kochiomocha_y, screen_height - kochiomocha_height))

    # Clear the screen
    screen.fill(white)

    # Draw Kochiomocha
    screen.blit(kochiomocha_img, (kochiomocha_x, kochiomocha_y))

    # --- Draw text input box ---
    txt_surface = font.render(text, True, color)
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(screen, color, input_box, 2)

    # --- Display Kochiomocha's response ---
    response_surface = response_font.render(response_text, True, response_color)
    screen.blit(response_surface, (response_x, response_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)

pygame.quit()