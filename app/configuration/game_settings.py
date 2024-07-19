import pygame

# Initialize fonts
pygame.font.init()

# Define constants for the game settings
class game_settings():
    # Game version
    release_version = 'v0.0'
    
    # Resolution settings
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    
    # Screen definition
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Font settings
    small_font = pygame.font.Font('text/fonts/Jacquard12Charted-Regular.ttf',25)
    medium_font = pygame.font.Font('text/fonts/Jacquard12Charted-Regular.ttf',50)
    big_font = pygame.font.Font('text/fonts/Jacquard12Charted-Regular.ttf',75)
    font_pos = pygame.font.Font('text/fonts/Jacquard12Charted-Regular.ttf', 25)
    font_dc = pygame.font.Font('text/fonts/Jacquard12Charted-Regular.ttf', 25)
    
    # Color presets
    white = (255, 255, 255)
    green = (0, 100, 0)
    blue = (0, 0, 100)
    light_green = (0, 200, 0)
    red = (150, 0, 0)
    black = (0, 0, 0)
    grey = (100,100,100)
    
    # Runitme settings
    fps = 120
    collision_cooldown = 10
    running = True
    main_menu_load = True
    game_start = False
    settings_menu_load = False
    credits_menu_load = False
    add_enemy = False
    cycle_count = 0
    cycle_max = 1000
    game_pause = False