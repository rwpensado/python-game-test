import pygame

# Move highlighted main menu options
def main_menu_update(pressed_keys,curr_settings):
    if pressed_keys[pygame.K_w]:
        count = 0
    if pressed_keys[pygame.K_s]:
        count = 0
    if pressed_keys[pygame.K_a]:
        count = 0
    if pressed_keys[pygame.K_d]:  
        count = 0
        
# Move highlighted settings menu options
def pause_menu_update(pressed_keys,curr_settings):
    if pressed_keys[pygame.K_w]:
        count = 0
    if pressed_keys[pygame.K_s]:
        count = 0
    if pressed_keys[pygame.K_a]:
        count = 0
    if pressed_keys[pygame.K_d]:  
        count = 0

# Move the sprite based on user keypresses
def game_play_update(player,pressed_keys,curr_settings):
    if player.dash_used == False:
        if pressed_keys[pygame.K_w]:
            player.rect.move_ip(0, -1 * player.walk_speed)
            player.y_pos -= player.walk_speed
            player.facing = 'UP'
            player.surf = pygame.image.load("graphics/sprites/player_back.png").convert()
        if pressed_keys[pygame.K_s]:
            player.rect.move_ip(0, player.walk_speed)
            player.y_pos += player.walk_speed
            player.facing = 'DOWN'
            player.surf = pygame.image.load("graphics/sprites/player_front.png").convert()
        if pressed_keys[pygame.K_a]:
            player.rect.move_ip(-1 * player.walk_speed, 0)
            player.x_pos -= player.walk_speed
            player.facing = 'LEFT'
            player.surf = pygame.image.load("graphics/sprites/player_left.png").convert()
        if pressed_keys[pygame.K_d]:
            player.rect.move_ip(player.walk_speed, 0)
            player.x_pos += player.walk_speed
            player.facing = 'RIGHT'
            player.surf = pygame.image.load("graphics/sprites/player_right.png").convert()
        
    # Check run input
    if player.curr_stamina >= 0:
        if player.stamina_lockout == False:
            if player.dash_used == False:
                if pressed_keys[pygame.K_UP] and pressed_keys[pygame.K_w]:
                    player.rect.move_ip(0, -1 * player.run_speed * player.walk_speed)
                    player.y_pos -= player.run_speed * player.walk_speed
                    if pressed_keys[pygame.K_s] == False:
                        player.curr_stamina -= 2
                if pressed_keys[pygame.K_UP] and pressed_keys[pygame.K_s]:
                    player.rect.move_ip(0, player.run_speed * player.walk_speed)
                    player.y_pos += player.run_speed * player.walk_speed
                    if pressed_keys[pygame.K_w] == False:
                        player.curr_stamina -= 2
                if pressed_keys[pygame.K_UP] and pressed_keys[pygame.K_a]:
                    player.rect.move_ip(-1 * player.run_speed * player.walk_speed, 0)
                    player.x_pos -= player.run_speed * player.walk_speed
                    if pressed_keys[pygame.K_s] == False and pressed_keys[pygame.K_w] == False and pressed_keys[pygame.K_d] == False:
                        player.curr_stamina -= 2
                if pressed_keys[pygame.K_UP] and pressed_keys[pygame.K_d]:
                    player.rect.move_ip(player.run_speed * player.walk_speed, 0)
                    player.x_pos += player.run_speed * player.walk_speed
                    if pressed_keys[pygame.K_s] == False and pressed_keys[pygame.K_w] == False and pressed_keys[pygame.K_a] == False:
                        player.curr_stamina -= 2
    
    '''# Check attack input
    if pressed_keys[pygame.K_SPACE]:
        if player.facing == 'UP':
            player.rect.move_ip(0, -1 * player.run_speed * player.walk_speed)
            player.y_pos -= player.run_speed * player.walk_speed
        if player.facing == 'DOWN':
            player.rect.move_ip(0, player.run_speed * player.walk_speed)
            player.y_pos += player.run_speed * player.walk_speed
        if player.facing == 'LEFT':
            player.rect.move_ip(-1 * player.run_speed * player.walk_speed, 0)
            player.x_pos -= player.run_speed * player.walk_speed
        if player.facing == 'RIGHT':
            player.rect.move_ip(player.run_speed * player.walk_speed, 0)
            player.x_pos += player.run_speed * player.walk_speed'''
    
    # Check dash input
    if player.curr_stamina > 0:
        if player.stamina_lockout == False:
            if pressed_keys[pygame.K_DOWN]:
                if player.dash_cooldown == False:
                    player.dash_used = True
    