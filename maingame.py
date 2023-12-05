import pygame
import sys
import random
import math

from Utilities import make_background, homepage, update_texts, choose_player, update_player_frames
from Utilities import Text, AnimatedSprite, Bullet

pygame.init()
pygame.mixer.init()

# Clear the terminal output
for ii in range(0, 10):
    print()

print('\nRunning maingame.py')
print('-----------------------------------------------------------------------')

# Screen dimensions
screen_width = 1152
screen_height = 648

# Creating the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Stribling Trail")
background = screen.copy()
make_background(background)

# Fonts and colors
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
#Alllllll the music
kazoo_music = pygame.mixer.music.load('sprites\kazoo.mp3')  # Replace with your music file path
pygame.mixer.music.set_volume(.5)  # between 0.0. and 1.0

background_music = pygame.mixer.music.load('sprites\Background_music.mp3')  # Replace with your music file path
pygame.mixer.music.set_volume(.5)  # between 0.0. and 1.0

squirrel_death_sound = pygame.mixer.Sound('sprites\dying.mp3')  # Replace with your sound file
pygame.mixer.music.set_volume(.5)  # between 0.0. and 1.0


# Main game loop
clock = pygame.time.Clock()
slime_moving = False
start_time = pygame.time.get_ticks()  # starts the timer when the game begins

# Initial game state
game_date = "August 15"
game_weather = "Sunny"
game_health = 100
game_food = 50
game_bricks_traveled = 0

kazoo_music = pygame.mixer.music.load('sprites\kazoo.mp3')  # Replace with your music file path
pygame.mixer.music.set_volume(.5)  # between 0.0. and 1.0
pygame.mixer.music.play(-1)

# homepage function from Utilities
homepage()


pygame.mixer.music.stop()

# the duration I want the character to move for
move_duration = random.randint(2000, 3000)  # moves between 2-3 seconds (milliseconds)

# Initial game texts
texts = update_texts(game_date, game_weather, game_health, game_food, game_bricks_traveled)

# Dictionary for loading in the characters and their sprite frames
character_data = {
    1: {"sheet": pygame.image.load('sprites/slime.png'), "frames": 8},
    2: {"sheet": pygame.image.load('sprites/alpha.png'), "frames": 7},
    3: {"sheet": pygame.image.load('sprites/zombie.png'), "frames": 10},
    4: {"sheet": pygame.image.load('sprites/hp.png'), "frames": 11},

}

# Get user's choice for player character
player_choice = choose_player()

initial_player_choice = choose_player()


# Update sprite sheet and frame information based on user's choice
slime_sheet = character_data[player_choice]["sheet"]
frame_count = character_data[player_choice]["frames"]
frame_width = slime_sheet.get_width() // frame_count
frame_height = slime_sheet.get_height()
player_frames = [slime_sheet.subsurface((i * frame_width, 0, frame_width, frame_height)) for i in range(frame_count)]
current_frame = 0

sprite_position = (1000, 72)

# adjusts where certain characters sit on the screen
if player_choice == 2:  # Alpha character
    sprite_position = (1000, 102)  # Adjust the vertical position as needed
elif player_choice == 3:  # Zombie character
    sprite_position = (1000, 102)  # Adjust the vertical position as needed

slime_sprite = AnimatedSprite(player_frames, sprite_position)

# Adjust the speed of the sprite animation
frame_delay = 70  # Set the delay in milliseconds
last_frame_time = pygame.time.get_ticks()

# initialize the counter
movement_counter = 0
num_stops = 0

# List of different event messages
all_event_messages = [
    {"message": "A plebe throws a sock at you! \n-5 health", "health_effect": -5,"special": False},
    {"message": "King Hall served expired fish today :(  \n-15 health due to extended toilet time",
     "health_effect": -5, "special": False},
    {"message": "You had 5 briefs today and \ndidn't get lunch. -10 food", "food_effect": -10, "special": False},
    {"message": "Your cover got blown off in the wind \n(how embarrassing). -5 health", "health_effect": -5, "special": False},
    {"message": "You've gotten dysentery. \n-20 health", "health_effect": -10, "special": False},
    {"message": "They had cake pops in King Hall!!! \nYou ate all of them. +10 food", "food_effect": +10, "special": False},
    {"message": "BMU gave you 30 different \npills for your cough. Your pumped up on adrenaline all day, +10 health",
     "health_effect": +10},
    {"message": "You got socked today in boxing, \n-5 health", "health_effect": -5},
    {"message": "You saluted a chief, -5 health", "health_effect": -5},
    {"message": "You got 6 hours of sleep instead of 5! \n +10 health", "health_effect": +10},
    {"message": "You didn't have to hold a single door open on \nyour way to class, +5 health", "health_effect": +5},
]

stop_walking_text = Text("Press ENTER to stop walking", font2, white, (50, 20))
hunt_text = Text("Press H to hunt", font2, white, (50, 40))
game_over = Text("YOU'VE BEEN SEPARATED", font4, white, (320, 280))

slime_moving = False
running = True
move_duration = random.randint(2000, 3000)  # Initial movement duration
pause_duration = 1000  # Initial pause duration in milliseconds

event_trigger_threshold = random.randint(1, 4)  # Random threshold for triggering events
event_counter = 0  # Counter to keep track of pauses

paused = False
hunting_mode = False

hunting_player_position = [screen_width // 2, screen_height // 2]

player_choice = 1  # Default player choice
current_player_choice = initial_player_choice

selected_player_frames = character_data[player_choice]["sheet"]
frame_count = character_data[player_choice]["frames"]
frame_width = selected_player_frames.get_width() // frame_count
frame_height = selected_player_frames.get_height()
player_frames = [selected_player_frames.subsurface((i * frame_width, 0, frame_width, frame_height)) for i in
                 range(frame_count)]
current_frame = 0

# Assuming you have the static image loaded
autumn_tree = pygame.image.load('sprites\Autumn_tree.png').convert_alpha()
broken_tree = pygame.image.load('sprites\Broken_tree.png').convert_alpha()
broken_tree2 = pygame.image.load('sprites\Broken_tree2.png').convert_alpha()
tree = pygame.image.load('sprites\Tree.png').convert_alpha()

# Define the number of trees and the spacing between them
num_trees = 20
tree_spacing = 100

# Define the starting position for the first tree
start_x = 0
start_y = 400

# Create positions for each tree in a line
autumn_tree_positions = [(start_x + i * tree_spacing, start_y) for i in range(num_trees)]


def update_player_frames(sheet, frames_count):
    frame_width = sheet.get_width() // frames_count
    frame_height = sheet.get_height()
    return [sheet.subsurface((i * frame_width, 0, frame_width, frame_height)) for i in range(frames_count)]
def update_game_data():
    global game_date, game_weather, game_health, game_food, game_bricks_traveled
    texts = update_texts(game_date, game_weather, game_health, game_food, game_bricks_traveled)

    if not paused:  # Check if the game is not paused
        # Update game state
        game_date = "August 15"
        game_weather = "Sunny"
        game_health -= 5
        game_food -= 5

        # Ensure health and food do not go below 0
        game_health = max(0, game_health)
        game_food = max(0, game_food)

        # Update specific Text objects in the list
        texts[1].update(f"Weather: {game_weather}")
        texts[2].update(f"Health: {game_health}")
        texts[3].update(f"Food: {game_food}")
        texts[4].update(f"Bricks traveled: {game_bricks_traveled}")
paused = False

# Load sprite sheets for squirrel
squirrel = pygame.image.load('sprites/squirrel.png')
# Define squirrel
squirrel_frames = update_player_frames(squirrel, 5)

num_squirrels = 5
squirrel_positions = [(i * (screen_width // (num_squirrels - 1)), 150) for i in range(num_squirrels)]
squirrel_velocities = [2 for _ in range(num_squirrels)]  # Initial horizontal velocities

# List to store active bullets
bullets = pygame.sprite.Group()

squirrel_sprites = pygame.sprite.Group()
for i, position in enumerate(squirrel_positions):
    squirrel_sprite = pygame.sprite.Sprite()
    squirrel_sprite.rect = pygame.Rect(position[0], position[1], 100, 50)
    squirrel_sprites.add(squirrel_sprite)


player_width = 30
player_height = 80
player_spawned = False

killed_squirrels = 0
killed_squirrels_text = Text(f"Killed Squirrels: {killed_squirrels}", font2, white, (180, 20), True)
go_to_main_text = Text("Press h again to return to main game", font2, white, (180,50),True)

# Play background music when entering the main game loop
pygame.mixer.music.load('sprites\Background_music.mp3')
pygame.mixer.music.play(-1)

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Toggle between paused and running states
                paused = not paused
            elif event.key == pygame.K_h and not paused:
                # Enter hunting mode with the initial player's position
                hunting_mode = not hunting_mode
                if hunting_mode:
                    current_player_choice = initial_player_choice
                    selected_player_frames = character_data[current_player_choice]["sheet"]
                    frame_count = character_data[current_player_choice]["frames"]
                    frame_width = selected_player_frames.get_width() // frame_count
                    frame_height = selected_player_frames.get_height()
                    player_frames = [selected_player_frames.subsurface((i * frame_width, 0, frame_width, frame_height))
                                     for i in range(frame_count)]
                    current_frame = 0
                    squirrel_appear_time = pygame.time.get_ticks() + random.randint(4000, 10000)
            elif event.key == pygame.K_SPACE and hunting_mode:
                # Create a new bullet at the player's position
                new_bullet = Bullet(hunting_player_position[0] + player_width, hunting_player_position[1] + player_height // 2)
                bullets.add(new_bullet)

    if not paused and not hunting_mode:
        # Draw the background onto the screen
        screen.blit(background, (0, 0))

        # Update the sprite animation based on the frame delay
        current_time = pygame.time.get_ticks()

        if slime_moving:
            elapsed_time = current_time - start_time
            if elapsed_time >= move_duration:
                slime_moving = False
                update_game_data()

                start_time = current_time
                move_duration = random.randint(2000, 3000)

                # Increment the movement counter
                movement_counter += 1

                # Check if the counter has reached the desired threshold
                if movement_counter >= event_trigger_threshold:
                    # Randomly select an event
                    selected_event = random.choice(all_event_messages)

                    # Get the event message
                    event_message = selected_event.get("message", "")

                    # Set up the box dimensions
                    box_width = 400
                    box_height = 150

                    # Create a rectangle for the background
                    event_box_rect = pygame.Rect(
                        (screen_width // 2 - box_width // 2, screen_height // 2 - box_height // 2),
                        (box_width, box_height))
                    event_box_rect_black = pygame.Rect((350, 225), (450, 200))

                    # Draw the background rectangle
                    pygame.draw.rect(screen, black, event_box_rect_black)
                    pygame.draw.rect(screen, white, event_box_rect)

                    # Display the event text inside the box
                    event_text = Text(event_message, font3, black, (screen_width // 2, screen_height // 2), center=True)
                    event_text.draw(screen)

                    pygame.display.flip()
                    pygame.time.delay(2500)  # Display the text for 2 seconds

                    # Apply the effects of the event to game variables
                    game_health += selected_event.get("health_effect", 0)
                    game_food += selected_event.get("food_effect", 0)


                    # Reset the counters after triggering the event
                    movement_counter = 0
                    event_counter += 1

                    # Check if the event counter has reached the threshold
                    if event_counter >= event_trigger_threshold:
                        # Reset the event counter and randomly select a new threshold
                        event_counter = 0
                        event_trigger_threshold = random.randint(2, 4)

            if current_time - last_frame_time > frame_delay:
                slime_sprite.update()
                last_frame_time = current_time

        # Automatically start the movement cycle if not already moving
        if not slime_moving:
            elapsed_time = current_time - start_time
            if elapsed_time >= pause_duration:
                slime_moving = True
                start_time = current_time
                move_duration = random.randint(2000, 3000)
                # Calculate the distance moved in bricks (adjust multiplier as needed)
                distance_moved = movement_counter * 1

                # Increment the bricks traveled counter
                game_bricks_traveled += distance_moved

                # Increment the movement counter
                movement_counter += 1

                # Check if food level is below 0 and adjust health accordingly
                if game_food < 0:
                    game_health -= 10

                if game_health <= 0:
                    # Display game over page (replace this with your actual game over logic)
                    screen.fill((0, 0, 0))
                    game_over.draw(screen)
                    pygame.display.flip()
                    pygame.time.delay(100000)  # Display the game over page for 5 seconds
                    pygame.quit()
                    sys.exit()

                # Update specific Text objects in the list based on the new game state
                texts[2].update(f"Health: {game_health}")
                texts[3].update(f"Food: {game_food}")
                texts[4].update(f"Bricks traveled: {game_bricks_traveled}")

        # Draw the sprite on the screen
        screen.blit(slime_sprite.image, slime_sprite.rect.topleft)

        # Input texts
        for text in texts:
            text.draw(screen)

        hunt_text.draw(screen)
        stop_walking_text.draw(screen)

        # Update the display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(30)

    elif hunting_mode:

        if not player_spawned:
            hunting_player_position = [500, 500]
            player_spawned = True
        screen.fill((0, 0, 0))

        bullets.update()
        bullets.draw(screen)

        for position in autumn_tree_positions:
            screen.blit(autumn_tree, position)

        # Iterate over tree positions for collision detection
        for position in autumn_tree_positions:
            # Check for collisions between bullets and trees
            bullet_tree_collisions = pygame.sprite.spritecollide(
                Bullet(position[0] + autumn_tree.get_width() // 2, position[1] + autumn_tree.get_height() // 2),
                bullets,
                True
            )
            if bullet_tree_collisions:
                # Handle bullet hit tree (remove bullet, play sound, etc.)
                print("Bullet hit tree")

        # Update and draw the remaining squirrels onto the screen
        for i, squirrel in enumerate(squirrel_sprites.sprites()):
            squirrel_positions[i] = (
                squirrel_positions[i][0] + squirrel_velocities[i],
                squirrel_positions[i][1] + 10 * math.sin(squirrel_positions[i][0] * 0.1)
            )
            squirrel.rect.topleft = squirrel_positions[i]
            screen.blit(squirrel_frames[current_frame % len(squirrel_frames)], squirrel.rect.topleft)

        # Check for collisions between bullets and squirrels
        for i, squirrel in enumerate(squirrel_sprites.sprites()):
            collisions = pygame.sprite.spritecollide(squirrel, bullets, True)
            if collisions:
                # Handle squirrel hit
                killed_squirrels += 1
                game_food += 15
                squirrel_sprites.remove(squirrel)  # Remove the hit squirrel from the group

                # Play the death sound
                squirrel_death_sound.play()

                break

        # Update and draw the remaining squirrels onto the screen
        for i, squirrel in enumerate(squirrel_sprites.sprites()):
            squirrel_positions[i] = (
                squirrel_positions[i][0] + squirrel_velocities[i],
                squirrel_positions[i][1]
            )

            # Check if the squirrel is going out of the screen boundaries
            if squirrel_positions[i][0] < 0 or squirrel_positions[i][0] > screen_width - squirrel.rect.width:
                # Reverse the velocity to change direction
                squirrel_velocities[i] = -squirrel_velocities[i]

            squirrel.rect.topleft = squirrel_positions[i]
            screen.blit(squirrel_frames[current_frame % len(squirrel_frames)], squirrel.rect.topleft)

        # Check if any bullet hit a squirrel and remove that specific squirrel
        for bullet in bullets.sprites():
            squirrel_hit_list = pygame.sprite.spritecollide(bullet, squirrel_sprites, True)
            for squirrel in squirrel_hit_list:
                # Handle squirrel hit (remove squirrel, increase score, etc.)
                killed_squirrels += 1
                game_food += 15

        # Update the food variable in the main game
        texts[3].update(f"Food: {game_food}")
        keys = pygame.key.get_pressed()

        # Save the player's current position before potential movement
        new_player_position = hunting_player_position.copy()

        movement_speed = 3  # Adjust the movement speed as needed

        if keys[pygame.K_UP]:
            new_player_position[1] -= movement_speed

        if keys[pygame.K_DOWN]:
            new_player_position[1] += movement_speed

        if keys[pygame.K_LEFT]:
            new_player_position[0] -= movement_speed

        if keys[pygame.K_RIGHT]:
            new_player_position[0] += movement_speed

        # Ensure the player stays within the screen boundaries
        new_player_position[0] = max(0, min(new_player_position[0], screen_width - player_width))
        new_player_position[1] = max(0, min(new_player_position[1], screen_height - player_height))

        # Check for collision with trees
        player_rect = pygame.Rect(new_player_position[0], new_player_position[1], player_width, player_height)
        for tree_position in autumn_tree_positions:
            tree_rect = pygame.Rect(tree_position[0], tree_position[1], tree.get_width(), tree.get_height())
            if player_rect.colliderect(tree_rect):
                # If there is a collision, do not update the player's position
                new_player_position = hunting_player_position.copy()
                break

        hunting_player_position = new_player_position

        # Draw the selected player onto the screen
        screen.blit(player_frames[current_frame], new_player_position)

        killed_squirrels_text.update(f"Killed Squirrels(+15 food): {killed_squirrels}")
        killed_squirrels_text.draw(screen)
        go_to_main_text.draw(screen)
        pygame.display.flip()

        clock.tick(30)

# Quit the game outside the loop
pygame.mixer.music.stop()
pygame.quit()
sys.exit()

if __name__ == "__main__":
    # If the module is run directly, it means it's not imported as a module.
    # In this case, execute the main_game function with a default character for testing.
    main_game(1)
