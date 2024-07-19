import pygame

def update_player_coord_x(player,curr_settings):
    x_co_val = "x_pos: " + str(player.x_pos)
    text_x = curr_settings.small_font.render(x_co_val, True, curr_settings.green, curr_settings.black)
    return text_x

def update_player_pos_x(text_x,curr_settings):
    text_rect_x = text_x.get_rect()
    text_rect_x.center = (curr_settings.SCREEN_WIDTH - 100, curr_settings.SCREEN_HEIGHT - 75)
    return text_rect_x

def update_player_coord_y(player,curr_settings):
    y_co_val = "y_pos: " + str(player.y_pos)
    text_y = curr_settings.small_font.render(y_co_val, True, curr_settings.green, curr_settings.black)
    return text_y

def update_player_pos_y(text_y,curr_settings): 
    text_rect_y = text_y.get_rect()
    text_rect_y.center = (curr_settings.SCREEN_WIDTH - 100, curr_settings.SCREEN_HEIGHT - 50)
    return text_rect_y
    
def update_player_dc_text(player,curr_settings):
    death_count_val = "Lives: " + str(player.lives)
    text_dc = curr_settings.medium_font.render(death_count_val, True, curr_settings.red, curr_settings.black)
    text_rect_dc = text_dc.get_rect()
    text_rect_dc.center = (100, curr_settings.SCREEN_HEIGHT - 50)
    return text_dc,text_rect_dc