import pygame

def load_main_menu(curr_settings):
    # Disable other game state functions
    curr_settings.game_start = False
    curr_settings.settings_menu_load = False
    curr_settings.credits_menu_load = False
    
    # Place background image
    main_background = pygame.image.load("graphics/menus/main_screen_background.png").convert()
    curr_settings.screen.blit(main_background, (0,0))

    # Set font text
    title_text = curr_settings.big_font.render('PLACEHOLDER GAME' , True , curr_settings.green)
    company_name = curr_settings.small_font.render('Something-Or-Other Studios@' , True , curr_settings.green)
    start_button_text = curr_settings.medium_font.render('Start' , True , curr_settings.blue)
    settings_button_text = curr_settings.medium_font.render('Settings' , True , curr_settings.blue)
    credits_button_text = curr_settings.medium_font.render('Credits' , True , curr_settings.blue)
    quit_button_text = curr_settings.medium_font.render('Quit' , True , curr_settings.red)
    build_text = curr_settings.small_font.render('Build: ' + curr_settings.release_version , True , curr_settings.white)
    
    # Set font locations
    title_text_rect = title_text.get_rect(center = (curr_settings.SCREEN_WIDTH/2,curr_settings.SCREEN_HEIGHT/2 - 250))
    company_name_rect = company_name.get_rect(center = (curr_settings.SCREEN_WIDTH/2,curr_settings.SCREEN_HEIGHT - 100))
    start_button_text_rect = start_button_text.get_rect(center = (curr_settings.SCREEN_WIDTH/2,curr_settings.SCREEN_HEIGHT/2 - 25))
    settings_button_text_rect = settings_button_text.get_rect(center = (curr_settings.SCREEN_WIDTH/2,curr_settings.SCREEN_HEIGHT/2 + 100))
    credits_button_text_rect = credits_button_text.get_rect(center = (curr_settings.SCREEN_WIDTH/2,curr_settings.SCREEN_HEIGHT/2 + 225))
    quit_button_text_rect = quit_button_text.get_rect(center = (curr_settings.SCREEN_WIDTH/2,curr_settings.SCREEN_HEIGHT/2 + 350))
    build_text_rect = build_text.get_rect(center = (curr_settings.SCREEN_WIDTH - 650 ,curr_settings.SCREEN_HEIGHT - 50))
    
    # Draw menu buttons
    button = pygame.image.load("graphics/menus/button.png").convert()
    curr_settings.screen.blit(button, (curr_settings.SCREEN_WIDTH/2 - 125,curr_settings.SCREEN_HEIGHT/2 - 50,250,50))
    curr_settings.screen.blit(button, (curr_settings.SCREEN_WIDTH/2 - 125,curr_settings.SCREEN_HEIGHT/2 + 75,250,50))
    curr_settings.screen.blit(button, (curr_settings.SCREEN_WIDTH/2 - 125,curr_settings.SCREEN_HEIGHT/2 + 200,250,50))
    curr_settings.screen.blit(button, (curr_settings.SCREEN_WIDTH/2 - 125,curr_settings.SCREEN_HEIGHT/2 + 325,250,50))
    #pygame.draw.rect(curr_settings.screen,curr_settings.grey,(curr_settings.SCREEN_WIDTH/2 - 125,curr_settings.SCREEN_HEIGHT/2 - 25,250,50))
    #pygame.draw.rect(curr_settings.screen,curr_settings.grey,(curr_settings.SCREEN_WIDTH/2 - 125,curr_settings.SCREEN_HEIGHT/2 + 75,250,50))
    #pygame.draw.rect(curr_settings.screen,curr_settings.grey,(curr_settings.SCREEN_WIDTH/2 - 125,curr_settings.SCREEN_HEIGHT/2 + 175,250,50))
    #pygame.draw.rect(curr_settings.screen,curr_settings.grey,(curr_settings.SCREEN_WIDTH/2 - 125,curr_settings.SCREEN_HEIGHT/2 + 275,250,50))
    
    # Draw menu text
    curr_settings.screen.blit(title_text,title_text_rect)
    curr_settings.screen.blit(start_button_text,start_button_text_rect)
    curr_settings.screen.blit(settings_button_text,settings_button_text_rect)
    curr_settings.screen.blit(credits_button_text,credits_button_text_rect)
    curr_settings.screen.blit(quit_button_text,quit_button_text_rect)
    curr_settings.screen.blit(company_name,company_name_rect)
    curr_settings.screen.blit(build_text,build_text_rect)