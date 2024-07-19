import pygame
from entities import characters
from configuration import input_tracking

# Main menu event processing
def check_main_menu_events(events,curr_settings):
    # Get the set of keys pressed, check for user input, and process accordingly
    pressed_keys = pygame.key.get_pressed()
    input_tracking.main_menu_update(pressed_keys,curr_settings) 
    
    # Cycle through events    
    for event in events:
        # Check for KEYDOWN event
        if event.type == pygame.KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == pygame.K_ESCAPE:
                curr_settings.running = False
        
        # Check main menu click events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if curr_settings.SCREEN_WIDTH/2-125 <= mouse[0] <= curr_settings.SCREEN_WIDTH/2+125 and curr_settings.SCREEN_HEIGHT/2-50 <= mouse[1] <= curr_settings.SCREEN_HEIGHT/2:
                curr_settings.game_start = True
                curr_settings.main_menu_load = False
                curr_settings.settings_menu_load = False
                curr_settings.credits_menu_load = False
            if curr_settings.SCREEN_WIDTH/2-125 <= mouse[0] <= curr_settings.SCREEN_WIDTH/2+125 and curr_settings.SCREEN_HEIGHT/2+75 <= mouse[1] <= curr_settings.SCREEN_HEIGHT/2+125:
                curr_settings.main_menu_load = False
                curr_settings.settings_menu_load = True
                curr_settings.credits_menu_load = False
            if curr_settings.SCREEN_WIDTH/2-125 <= mouse[0] <= curr_settings.SCREEN_WIDTH/2+125 and curr_settings.SCREEN_HEIGHT/2+200 <= mouse[1] <= curr_settings.SCREEN_HEIGHT/2+250:
                curr_settings.main_menu_load = False
                curr_settings.credits_menu_load = False
                curr_settings.settings_menu_load = True
            if curr_settings.SCREEN_WIDTH/2-125 <= mouse[0] <= curr_settings.SCREEN_WIDTH/2+125 and curr_settings.SCREEN_HEIGHT/2+325 <= mouse[1] <= curr_settings.SCREEN_HEIGHT/2+375:
                curr_settings.running = False
        
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == pygame.QUIT:
            curr_settings.running = False

# Game play event processing            
def check_game_play_events(events,curr_settings,player):
    # Get the set of keys pressed, check for user input, and process accordingly
    pressed_keys = pygame.key.get_pressed()
    input_tracking.game_play_update(player,pressed_keys,curr_settings)
    
    # Cycle through events    
    for event in events:
        # Check for KEYDOWN event
        if event.type == pygame.KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == pygame.K_ESCAPE:
                curr_settings.game_pause = True
            
        '''# Check player position
        if player.x_pos >= curr_settings.SCREEN_WIDTH/2:
            # Create a custom event for adding a new enemy
            curr_settings.add_enemy = True '''  

# Settings menu event processing            
def check_pause_events(events,curr_settings):
    # Get the set of keys pressed, check for user input, and process accordingly
    pressed_keys = pygame.key.get_pressed()
    input_tracking.pause_menu_update(pressed_keys,curr_settings)
    
    # Cycle through events    
    for event in events:
        # Check for KEYDOWN event
        if event.type == pygame.KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == pygame.K_ESCAPE:
                curr_settings.game_pause = False
                curr_settings.running = False
        
        # Check main menu click events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if curr_settings.SCREEN_WIDTH/2-150 <= mouse[0] <= curr_settings.SCREEN_WIDTH/2+150 and curr_settings.SCREEN_HEIGHT/2-250 <= mouse[1] <= curr_settings.SCREEN_HEIGHT/2-200:
                curr_settings.game_pause = False
            if curr_settings.SCREEN_WIDTH/2-150 <= mouse[0] <= curr_settings.SCREEN_WIDTH/2+150 and curr_settings.SCREEN_HEIGHT/2-125 <= mouse[1] <= curr_settings.SCREEN_HEIGHT/2-75:
                hold_val = 0
            if curr_settings.SCREEN_WIDTH/2-150 <= mouse[0] <= curr_settings.SCREEN_WIDTH/2+150 and curr_settings.SCREEN_HEIGHT/2 <= mouse[1] <= curr_settings.SCREEN_HEIGHT/2+50:
                hold_val = 0
            if curr_settings.SCREEN_WIDTH/2-150 <= mouse[0] <= curr_settings.SCREEN_WIDTH/2+150 and curr_settings.SCREEN_HEIGHT/2+100 <= mouse[1] <= curr_settings.SCREEN_HEIGHT/2+150:
                hold_val = 0
            if curr_settings.SCREEN_WIDTH/2-150 <= mouse[0] <= curr_settings.SCREEN_WIDTH/2+150 and curr_settings.SCREEN_HEIGHT/2+250 <= mouse[1] <= curr_settings.SCREEN_HEIGHT/2+300:
                curr_settings.running = False
                curr_settings.game_pause = False
    
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == pygame.QUIT:
            curr_settings.running = False  

def enemy_events(curr_settings,enemies,all_sprites):
    # Add a new enemy
    if curr_settings.add_enemy == True:
        # Create the new enemy and add it to sprite groups
        new_enemy = characters.enemy_1(curr_settings)
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)
