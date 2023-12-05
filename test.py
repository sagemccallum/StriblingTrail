

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Enter key
                # Toggle between paused and running states
                paused = not paused
            elif event.key == pygame.K_h and not paused:
                # Enter hunting mode with the initial player's position
                hunting_mode = not hunting_mode
                if hunting_mode:
                    current_player_choice = initial_player_choice  # Use the initial player choice
                    # Update sprite sheet and frame information based on user's choice
                    selected_player_frames = character_data[current_player_choice]["sheet"]
                    frame_count = character_data[current_player_choice]["frames"]
                    frame_width = selected_player_frames.get_width() // frame_count
                    frame_height = selected_player_frames.get_height()
                    player_frames = [selected_player_frames.subsurface((i * frame_width, 0, frame_width, frame_height))
                                     for i in range(frame_count)]
                    current_frame = 0
                    # Individual appear times and movement durations for each animal
                    squirrel_appear_time = pygame.time.get_ticks() + random.randint(4000, 10000)
                    rat_appear_time = pygame.time.get_ticks() + random.randint(4000, 10000)
                    bird_appear_time = pygame.time.get_ticks() + random.randint(4000, 10000)

    if not paused and not hunting_mode:
        # Draw the background onto the screen
        screen.blit(background, (0, 0))

        # Update the sprite animation based on the frame delay
        current_time = pygame.time.get_ticks()

        for animal in animated_animals:
            screen.blit(animal.frames[animal.current_frame], animal.position)

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
                    selected_event = random.choice(event_messages)

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
                    game_weather += selected_event.get("weather_effect", "Sunny")

                    # Update specific Text objects in the list based on the new game state
                    texts[2].update(f"Health: {game_health}")
                    texts[3].update(f"Food: {game_food}")
                    texts[1].update(f"Weather: {game_weather}")

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
                movement_counter += 1

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

        screen.fill(black)  # Clear the screen

        hunt_text.draw(screen)

        stop_walking_text.draw(screen)

        current_time = pygame.time.get_ticks()

        if current_time - last_frame_time > frame_delay:
            current_frame = (current_frame + 1) % len(player_frames)

            last_frame_time = current_time

        screen.blit(player_frames[current_frame], hunting_player_position)

        # Handle player input for movement

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            hunting_player_position[1] -= 1

        if keys[pygame.K_DOWN]:
            hunting_player_position[1] += 1

        if keys[pygame.K_LEFT]:
            hunting_player_position[0] -= 1

        if keys[pygame.K_RIGHT]:
            hunting_player_position[0] += 1

        # Check for collisions with animals

        for animal in animated_animals:

            if animal.position[0] > screen_width:
                # Create a new instance of the animal

                new_animal = create_new_animal(animal.sheet, animal.frames, animal.speed)

                animated_animals.remove(animal)

                animated_animals.append(new_animal)

        # Draw Image 1 at random positions

        for position in autumn_tree_positions:
            screen.blit(autumn_tree, position)

        for position in broken_tree_positions:
            screen.blit(broken_tree, position)

        for position in broken_tree2_positions:
            screen.blit(broken_tree2, position)

        for position in tree_positions:
            screen.blit(tree, position)

        # Draw and update animals

        for animal in animated_animals:
            animal.update([], 0, 0, screen_width, screen_height)

            screen.blit(animal.frames[animal.current_frame], animal.position)

        pygame.display.flip()

    # If the game is paused, display a pause message
    else:
        pause_text = Text("Paused", font1, white, (screen_width // 2, screen_height // 2), center=True)
        pause_text.draw(screen)
        pygame.display.flip()

# Quit the game outside the loop
pygame.mixer.music.stop()
pygame.quit()
sys.exit()