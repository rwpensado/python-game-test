import pygame

def load_pause_menu(curr_settings):
    # Draw settings menu
    settings_menu_background = pygame.image.load("graphics/menus/settings_menu.png").convert()
    curr_settings.screen.blit(settings_menu_background, (curr_settings.SCREEN_WIDTH/2 - 200,curr_settings.SCREEN_HEIGHT/2 - 300))
    
    # Set font text
    resume_button_text = curr_settings.medium_font.render('RESUME' , True , curr_settings.blue)
    stats_button_text = curr_settings.medium_font.render('STATS' , True , curr_settings.blue)
    equip_button_text = curr_settings.medium_font.render('EQUIPMENT' , True , curr_settings.blue)
    settings_button_text = curr_settings.medium_font.render('SETTINGS' , True , curr_settings.blue)
    quit_button_text = curr_settings.medium_font.render('QUIT' , True , curr_settings.blue)
    
    # Set font locations
    resume_button_text_rect = resume_button_text.get_rect(center = (curr_settings.SCREEN_WIDTH/2,curr_settings.SCREEN_HEIGHT/2 - 225))
    stats_button_text_rect = stats_button_text.get_rect(center = (curr_settings.SCREEN_WIDTH/2,curr_settings.SCREEN_HEIGHT/2 - 100))
    equip_button_text_rect = equip_button_text.get_rect(center = (curr_settings.SCREEN_WIDTH/2,curr_settings.SCREEN_HEIGHT/2 + 25))
    settings_button_text_rect = settings_button_text.get_rect(center = (curr_settings.SCREEN_WIDTH/2,curr_settings.SCREEN_HEIGHT/2 + 150))
    quit_button_text_rect = quit_button_text.get_rect(center = (curr_settings.SCREEN_WIDTH/2,curr_settings.SCREEN_HEIGHT/2 + 275))
    
    # Draw settings menu buttons
    button_settings = pygame.image.load("graphics/menus/button_settings.png").convert()
    curr_settings.screen.blit(button_settings, (curr_settings.SCREEN_WIDTH/2 - 150,curr_settings.SCREEN_HEIGHT/2 - 250))
    curr_settings.screen.blit(button_settings, (curr_settings.SCREEN_WIDTH/2 - 150,curr_settings.SCREEN_HEIGHT/2 - 125))
    curr_settings.screen.blit(button_settings, (curr_settings.SCREEN_WIDTH/2 - 150,curr_settings.SCREEN_HEIGHT/2))
    curr_settings.screen.blit(button_settings, (curr_settings.SCREEN_WIDTH/2 - 150,curr_settings.SCREEN_HEIGHT/2 + 125))
    curr_settings.screen.blit(button_settings, (curr_settings.SCREEN_WIDTH/2 - 150,curr_settings.SCREEN_HEIGHT/2 + 250))
    
    # Draw menu text
    curr_settings.screen.blit(resume_button_text,resume_button_text_rect)
    curr_settings.screen.blit(stats_button_text,stats_button_text_rect)
    curr_settings.screen.blit(equip_button_text,equip_button_text_rect)
    curr_settings.screen.blit(settings_button_text,settings_button_text_rect)
    curr_settings.screen.blit(quit_button_text,quit_button_text_rect)