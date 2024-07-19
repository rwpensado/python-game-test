import pygame
from entities import characters, stat_tracking
from configuration import game_settings, game_state, game_play, animations
from menus import menu_main, settings_window

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Set window title and icon
pygame.display.set_caption('PLACEHOLDER GAME')
window_icon_location = 'graphics/sprites/player.png'
window_icon = pygame.image.load(window_icon_location).convert()
pygame.display.set_icon(window_icon)

# Initialize variables
curr_settings = game_settings.game_settings()

# Instantiate player and enemies
player = characters.player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Main loop
while curr_settings.running:      
    # Load main menu
    if curr_settings.main_menu_load == True:
        menu_main.load_main_menu(curr_settings)
        pygame.display.update()
        # Check main menu events
        game_state.check_main_menu_events(pygame.event.get(),curr_settings)
    
    # Load game play
    if curr_settings.game_start == True:
        game_play.start_game(curr_settings,player,all_sprites)
        pygame.display.update()
        # Check game play events
        game_state.check_game_play_events(pygame.event.get(),curr_settings,player)   
        
    # Check windows
    if curr_settings.game_pause == True:
        settings_window.load_pause_menu(curr_settings)
        pygame.display.update()
    while curr_settings.game_pause:
        game_state.check_pause_events(pygame.event.get(),curr_settings)
    
    # Ensure program maintains fps
    clock.tick(curr_settings.fps)
    
    # Check max cycle count and tick counters
    curr_settings.cycle_count += 1
    if curr_settings.cycle_count >= curr_settings.cycle_max:
        curr_settings.cycle_count = 0
    if player.dash_used == True:
        player.dash_counter += 1
        
    # Check animations
    animations.player_dash(player)
    animations.player_quick_attack(player)
    animations.player_held_attack(player)
    
    # Check cooldowns
    # Dash
    if player.dash_cooldown_counter >= player.dash_cooldown_duration:
        player.dash_cooldown = False
        player.dash_cooldown_counter = 0
        player.dash_counter = 0
    if player.dash_cooldown == True:
        player.dash_cooldown_counter += 1
    # Stamina
    if player.curr_stamina <= 0:
        player.stamina_lockout = True
    if player.stamina_lockout == True:
        player.stamina_cooldown_counter += 1
        if player.stamina_cooldown_counter >= player.stamina_cooldown_duration:
            player.stamina_lockout = False
            player.stamina_cooldown_counter = 0
    if player.curr_stamina <= player.max_stamina:
        if player.stamina_lockout == False:
            player.curr_stamina += 1