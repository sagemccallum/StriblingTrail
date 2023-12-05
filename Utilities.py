import pygame
import random
import sys


def make_background(screen):
    # loading images and classic colors
    brick = pygame.image.load('sprites/brick.png').convert_alpha()
    white = (255, 255, 255)
    black = (0, 0, 0)
    brown = (98, 58, 0)

    # Drawing images on the screen

    for x in range(0, screen.get_width(), brick.get_width()):
        for y in range(0, 200, brick.get_height()):
            screen.blit(brick, (x, screen.get_height() - 450))



    rect_color = brown
    rect_position = (0, 262)
    rect_size = (screen.get_width(), 150)
    pygame.draw.rect(screen, rect_color, pygame.Rect(rect_position, rect_size))

    rect_color = white
    rect_position = (0, 412)
    rect_size = (screen.get_width(), 200)
    pygame.draw.rect(screen, rect_color, pygame.Rect(rect_position, rect_size))

    rect_color = black
    rect_position = (0, 610)
    rect_size = (screen.get_width(), 100)
    pygame.draw.rect(screen, rect_color, pygame.Rect(rect_position, rect_size))\

    rect_color = black
    rect_position = (0, 372)
    rect_size = (screen.get_width(), 40)
    pygame.draw.rect(screen, rect_color, pygame.Rect(rect_position, rect_size))


def make_homepage(screen):
    # Screen dimensions
    screen_width = 1152
    screen_height = 648
    cowboy = "Cowboy.ttf"
    font_size1 = 100
    font_size2 = 30
    font_size3 = 60
    font4 = pygame.font.Font(cowboy, 100)

    title_font = pygame.font.Font(cowboy, font_size1)
    sub_font = pygame.font.Font(cowboy, font_size2)
    med_font = pygame.font.Font(cowboy, font_size3)

    white = (255, 255, 255)
    black = (0, 0, 0)
    button_color = white
    # loading images and classic colors
    motherb = pygame.image.load('sprites/motherb.png').convert_alpha()

    # Drawing images on the screen

    for x in range(0, screen.get_width(), motherb.get_width()):
        for y in range(0, screen.get_height(), motherb.get_height()):
            screen.blit(motherb, (x, y))

    # Draw the "Start Game" button
    start_button_rect = pygame.Rect(300, 400, 200, 50)
    pygame.draw.rect(screen, white, start_button_rect)

    font = pygame.font.Font(None, 36)
    text = font.render("Start Game", True, black)
    text_rect = text.get_rect(center=start_button_rect.center)
    screen.blit(text, text_rect)

    return start_button_rect

def homepage():
    screen_width = 1152
    screen_height = 648
    cowboy = "Cowboy.ttf"
    font_size1 = 30
    font_size2 = 20
    font_size3 = 15
    font_size4 = 50
    font1 = pygame.font.Font(cowboy, font_size1)
    font2 = pygame.font.Font(cowboy, font_size2)
    font3 = pygame.font.Font(cowboy, font_size3)
    font4 = pygame.font.Font(cowboy, font_size4)
    white = (255, 255, 255)
    black = (0, 0, 0)
    navy = (11, 25, 119)

    # Creating the screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    home_background = screen.copy()
    make_background(home_background)
    motherb = pygame.image.load('sprites/motherb.png').convert_alpha()

    # Drawing images on the screen
    for x in range(0, screen.get_width(), motherb.get_width()):
        for y in range(0, screen.get_height(), motherb.get_height()):
            screen.blit(motherb, (x, y))

    home_font = pygame.font.Font(cowboy, 60)
    home_title = Text("Welcome to Stribling Trail", home_font, navy, (230, 70))
    home_title.draw(screen)

    start_button_rect = pygame.Rect((screen_width // 2 - 210, 570), (400, 70))
    pygame.draw.rect(screen, white, start_button_rect)
    start_button_text = Text("Start Game", font1, black, (490, 585))
    start_button_text.draw(screen)

    pygame.display.flip()

    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Left mouse click
                mouse_x, mouse_y = event.pos
                if start_button_rect.collidepoint(mouse_x, mouse_y):
                    waiting_for_click = False


def player_choices():
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

    # Screen dimensions
    screen_width = 1152
    screen_height = 648
    screen = pygame.display.set_mode((screen_width, screen_height))

    choices_surface = pygame.Surface((screen_width, screen_height))
    choices_surface.fill(black)
    # loading images and classic colors
    pleber = pygame.image.load('sprites/pleber.png').convert_alpha()
    # Drawing images on the screen

    for x in range(0, 300, pleber.get_width()):
        for y in range(0, 300, pleber.get_height()):
            screen.blit(pleber, (x, y))

    text1 = med_font.render("Choose Your Character:", True, white)
    text2 = sub_font.render("1. Slimy Plebe", True, white)
    text3 = sub_font.render("2. Helmet ", True, white)
    text4 = sub_font.render("3. 'Yeah I'll probably end up going SEALs'", True, white)

    choices_surface.blit(text1, (10, 160))
    choices_surface.blit(text2, (10, 200))
    choices_surface.blit(text3, (10, 240))
    choices_surface.blit(text4, (10, 280))

    return choices_surface


def choose_player():
    screen_width = 1152
    screen_height = 648
    screen = pygame.display.set_mode((screen_width, screen_height))

    cowboy = "Cowboy.ttf"
    font_size1 = 30
    font_size2 = 20
    font_size3 = 15
    font_size4 = 50
    font1 = pygame.font.Font(cowboy, font_size1)
    font2 = pygame.font.Font(cowboy, font_size2)
    font3 = pygame.font.Font(cowboy, font_size3)
    font4 = pygame.font.Font(cowboy, font_size4)
    white = (255, 255, 255)
    black = (0, 0, 0)
    screen.fill(black)

    choose_text = Text("Choose your character:", font1, white, (200, 50))
    choose_text.draw(screen)
    instruct_text = Text("(Press number on keyboard)", font1, white, (200, 100))
    instruct_text.draw(screen)
    options = [
        "1. Slimy Plebe",
        "2. 'What's your alpha?' guy",
        "3. Group 1 Major",
        "4. The Hospital Point Enthusiast"
    ]

    y_offset = 150
    for option in options:
        option_text = Text(option, font1, white, (300, y_offset))
        option_text.draw(screen)
        y_offset += 40

    pygame.display.flip()

    selected_choice = None
    while selected_choice not in ["1", "2", "3", "4"]:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_4:
                    selected_choice = chr(event.key)

    return int(selected_choice)

def update_player_frames(player_choice):
    character_data = {
        1: {"sheet": pygame.image.load('sprites/slime.png'), "frames": 8},
        2: {"sheet": pygame.image.load('sprites/alpha.png'), "frames": 7},
        3: {"sheet": pygame.image.load('sprites/zombie.png'), "frames": 10},
        4: {"sheet": pygame.image.load('sprites/hp.png'), "frames": 11},

    }
    selected_player_frames = character_data[player_choice]["sheet"]
    frame_count = character_data[player_choice]["frames"]
    frame_width = selected_player_frames.get_width() // frame_count
    frame_height = selected_player_frames.get_height()
    return [selected_player_frames.subsurface((i * frame_width, 0, frame_width, frame_height)) for i in
            range(frame_count)]

class Text:
    def __init__(self, text, font, color, position, center=False):
        self.text = text
        self.font = font
        self.color = color
        self.position = position
        self.center = center
        self.rendered_text = self.render()

        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect()

        if self.center:
            self.rect.center = self.position
        else:
            self.rect.topleft = self.position


    def render(self):
        return self.font.render(self.text, True, self.color)

    def update(self, new_text):
        self.text = new_text
        self.rendered_text = self.render()

    def draw(self, surface):
        lines = self.text.split('\n')  # Split the text into lines using '\n'
        for i, line in enumerate(lines):
            text_surface = self.font.render(line, True, self.color)
            rect = text_surface.get_rect()

            if self.center:
                rect.center = self.position[0], self.position[1] + i * rect.height
            else:
                rect.topleft = self.position[0], self.position[1] + i * rect.height

            surface.blit(text_surface, rect.topleft)

def update_texts(date, weather, health, food, bricks_traveled):
    # Fonts and colors
    cowboy = "Cowboy.ttf"
    font_size1 = 30
    font_size2 = 20
    font_size3 = 15
    font_size4 = 100
    font1 = pygame.font.Font(cowboy, font_size1)
    font2 = pygame.font.Font(cowboy, font_size2)
    font3 = pygame.font.Font(cowboy, font_size3)
    font4 = pygame.font.Font(cowboy, font_size4)

    white = (255, 255, 255)
    black = (0, 0, 0)
    main_texts = [
        Text(f"Date: {date}", font1, black, (497, 410)),
        Text(f"Weather: {weather}", font1, black, (448, 450)),
        Text(f"Health: {health}", font1, black, (475, 490)),
        Text(f"Food: {food}", font1, black, (495, 530)),
        Text(f"Bricks traveled: {bricks_traveled}", font1, black, (360, 570))
    ]
    return main_texts


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, frames, initial_position):
        super().__init__()
        self.frames = frames
        self.image = self.frames[-1]  # Start with the last frame
        self.rect = self.image.get_rect(topleft=initial_position)
        self.current_frame = len(self.frames) - 1  # Start with the last frame index

    def update(self):
        # Decrement the current_frame index
        self.current_frame -= 1
        if self.current_frame < 0:
            self.current_frame = len(self.frames) - 1  # Reset to the last frame if reached the first frame

        self.image = self.frames[self.current_frame]

    def reset_animation(self):
        self.current_frame = 0
        self.image = self.frames[self.current_frame]

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 8

    def update(self):
        self.rect.y -= self.speed