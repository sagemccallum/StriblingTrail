import pygame
import sys
from Utilities import make_homepage

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 1152
screen_height = 648

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Home Screen")
homepage = screen.copy()
make_homepage(homepage)

# Fonts and colors
cowboy = "Cowboy.ttf"
font_size1 = 100
font_size2 = 30
font_size3 = 60
title_font = pygame.font.Font(cowboy, font_size1)
sub_font = pygame.font.Font(cowboy, font_size2)
med_font = pygame.font.Font(cowboy, font_size3)

white = (255, 255, 255)
black = (0, 0, 0)
button_color = white

class StartButton:
    def __init__(self, text, position, size):
        self.text = text
        self.rect = pygame.Rect(position, size)

    def draw(self, surface):
        pygame.draw.rect(surface, button_color, self.rect)
        text_surface = sub_font.render(self.text, True, black)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def player_choices():
    choices_surface = pygame.Surface((screen_width, screen_height))
    choices_surface.fill(black)
    pleber = pygame.image.load('sprites/pleber.png').convert_alpha()

    for x in range(0, 300, pleber.get_width()):
        for y in range(0, 300, pleber.get_height()):
            choices_surface.blit(pleber, (x, y))

    text1 = med_font.render("Choose Your Character:", True, white)
    text2 = sub_font.render("1. The Slimy Plebe", True, white)
    text3 = sub_font.render("2. 'What's your alpha?' guy", True, white)
    text4 = sub_font.render("3. The Group 1 Major", True, white)
    text5 = sub_font.render("4. The Hospital Point Enthusiast", True, white)
    text6 = sub_font.render("Press the number on your keyboard for your desired character", True, white)

    choices_surface.blit(text1, (300, 160))
    choices_surface.blit(text2, (300, 240))
    choices_surface.blit(text3, (300, 300))
    choices_surface.blit(text4, (300, 360))
    choices_surface.blit(text5, (300, 420))
    choices_surface.blit(text6, (180, 550))

    return choices_surface  # Ensure that the choices are rendered before waiting for input

    selected_character = None
    choosing = True

    while choosing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_character = "Slimy Plebe"
                    choosing = False
                elif event.key == pygame.K_2:
                    selected_character = "'What's your alpha?' guy"
                    choosing = False
                elif event.key == pygame.K_3:
                    selected_character = "Group 1 Major"
                    choosing = False
                elif event.key == pygame.K_4:
                    selected_character = "The Hospital Point Enthusiast"
                    choosing = False

    return selected_character

# Home screen text
title_text = title_font.render("The Stribling Trail", True, black)
# Create a start button
start_button = StartButton("Start Game", (screen_width // 2 - 210, 570), (400, 70))

selected_character = None
show_player_choices = False
start_game = False  # Initialize the start_game flag

# Main game loop for the home screen
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.is_clicked(mouse_pos):
                    print("Left-click detected on 'Start Game'")
                    show_player_choices = True  # Set the flag to show player choices screen
        elif event.type == pygame.KEYDOWN and show_player_choices:
            # Handle key presses for player selection if the flag is set
            if event.key == pygame.K_1:
                selected_character = "Slimy Plebe"
            elif event.key == pygame.K_2:
                selected_character = "'What's your alpha?' guy"
            elif event.key == pygame.K_3:
                selected_character = "Group 1 Major"
            elif event.key == pygame.K_4:
                selected_character = "The Hospital Point Enthusiast"
                start_game = True  # Set the flag to transition to the main game

    # Draw the home screen
    screen.blit(homepage, (0, 0))
    screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 60))
    start_button.draw(screen)

    # If the flag is set, display the player choices screen
    if show_player_choices:
        # Draw the player choices screen
        player_choices_surface = player_choices()
        screen.blit(player_choices_surface, (0, 0))

        # Check if a character is selected
        if selected_character:
            print(f"Selected character: {selected_character}")
            show_player_choices = False  # Reset the flag to exit the player selection screen
            start_game = True  # Set the flag to transition to the main game

    # If the flag is set, transition to the main game
    if start_game:
        # Reset the flag and start the main game
        start_game = False
        from maingame import main_game  # Import the main game function

        main_game(selected_character)  # Pass the selected character to the main game function

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()