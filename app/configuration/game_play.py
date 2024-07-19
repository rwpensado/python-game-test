import pygame
from text import text_processing
from configuration import game_state
from menus import settings_window

def start_game(curr_settings,player,all_sprites):
    # Enable disable other game state functions
    curr_settings.game_start = True
    curr_settings.main_menu_load = False
    curr_settings.settings_menu_load = False
    curr_settings.credits_menu_load = False
    
    # Health and stamina bar scaling
    stamina_bar_width = 750 - 750 * (1 - player.curr_stamina/player.max_stamina)
    
    # Fill the screen with green
    curr_settings.screen.fill(curr_settings.light_green)
    
    # Heath and stamina bar
    pygame.draw.rect(curr_settings.screen,curr_settings.black,(curr_settings.SCREEN_WIDTH/2 - 905,curr_settings.SCREEN_HEIGHT/2 - 535,760,35))
    pygame.draw.rect(curr_settings.screen,curr_settings.grey,(curr_settings.SCREEN_WIDTH/2 - 900,curr_settings.SCREEN_HEIGHT/2 - 530,750,25))
    pygame.draw.rect(curr_settings.screen,curr_settings.red,(curr_settings.SCREEN_WIDTH/2 - 900,curr_settings.SCREEN_HEIGHT/2 - 530,750,25))
    pygame.draw.rect(curr_settings.screen,curr_settings.black,(curr_settings.SCREEN_WIDTH/2 - 905,curr_settings.SCREEN_HEIGHT/2 - 495,760,35))
    pygame.draw.rect(curr_settings.screen,curr_settings.grey,(curr_settings.SCREEN_WIDTH/2 - 900,curr_settings.SCREEN_HEIGHT/2 - 490,750,25)) 
    pygame.draw.rect(curr_settings.screen,curr_settings.green,(curr_settings.SCREEN_WIDTH/2 - 900,curr_settings.SCREEN_HEIGHT/2 - 490,stamina_bar_width,25))
    
    # Update all entities
    #x_coord = text_processing.update_player_coord_x(player,curr_settings)
    #x_pos = text_processing.update_player_pos_x(x_coord,curr_settings)
    #y_coord = text_processing.update_player_coord_y(player,curr_settings)
    #y_pos = text_processing.update_player_pos_y(y_coord,curr_settings)
    #dc = text_processing.update_player_dc_text(player,curr_settings)
        
    # Pause for open menu settings
    while curr_settings.game_pause == True:
        game_state.check_events(pygame.event.get(),curr_settings,player)
                      
    # Keep player on the screen
    if player.rect.left < 0:
        player.rect.left = 0
        player.x_pos = 0
    if player.rect.right > curr_settings.SCREEN_WIDTH:
        player.rect.right = curr_settings.SCREEN_WIDTH 
        player.x_pos = curr_settings.SCREEN_WIDTH
    if player.rect.top <= 0:
        player.rect.top = 0
        player.y_pos = 0
    if player.rect.bottom >= curr_settings.SCREEN_HEIGHT:
        player.rect.bottom = curr_settings.SCREEN_HEIGHT
        player.y_pos = curr_settings.SCREEN_HEIGHT
    
    # Draw all sprites
    for entity in all_sprites:
        curr_settings.screen.blit(entity.surf, entity.rect)
    
    # Draw all screen text
    #curr_settings.screen.blit(x_coord,x_pos)
    #curr_settings.screen.blit(y_coord,y_pos)
    #curr_settings.screen.blit(dc[0], dc[1])