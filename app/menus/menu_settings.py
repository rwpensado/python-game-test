import pygame

def load_settings_menu(curr_settings):
    # Fill the screen with black
    curr_settings.screen.fill((0, 0, 0))

    # Set font text
    title_text = curr_settings.big_font.render('PLACEHOLDER GAME' , True , curr_settings.green)
    company_name = curr_settings.small_font.render('Something-Or-Other Studios@' , True , curr_settings.green)
    start_button_text = curr_settings.medium_font.render('Start' , True , curr_settings.blue)
    quit_button_text = curr_settings.medium_font.render('Quit' , True , curr_settings.red)
    
    # Set font locations
    title_text_rect = title_text.get_rect(center = (curr_settings.SCREEN_WIDTH/2,curr_settings.SCREEN_HEIGHT/2 - 250))
    company_name_rect = company_name.get_rect(center = (curr_settings.SCREEN_WIDTH/2,curr_settings.SCREEN_HEIGHT - 50))
    start_button_text_rect = start_button_text.get_rect(center = (curr_settings.SCREEN_WIDTH/2,curr_settings.SCREEN_HEIGHT/2))
    quit_button_text_rect = quit_button_text.get_rect(center = (curr_settings.SCREEN_WIDTH/2,curr_settings.SCREEN_HEIGHT/2 + 100))
    
    # Draw menu buttons
    pygame.draw.rect(curr_settings.screen,curr_settings.grey,(curr_settings.SCREEN_WIDTH/2 - 100,curr_settings.SCREEN_HEIGHT/2 - 25,200,50))
    pygame.draw.rect(curr_settings.screen,curr_settings.grey,(curr_settings.SCREEN_WIDTH/2 - 100,curr_settings.SCREEN_HEIGHT/2 + 75,200,50)) 
    
    # Draw menu text
    curr_settings.screen.blit(title_text,title_text_rect)
    curr_settings.screen.blit(start_button_text,start_button_text_rect)
    curr_settings.screen.blit(quit_button_text,quit_button_text_rect)
    curr_settings.screen.blit(company_name,company_name_rect)