import pygame

def player_dash(player):
    if player.dash_used == True:
        if player.dash_counter < player.dash_duration:
            if player.facing == 'UP':
                player.rect.move_ip(0, -1 * player.dash_speed * player.walk_speed)
                player.y_pos -= player.dash_speed * player.walk_speed
                player.rect.move_ip(0, -1 * player.dash_speed * player.walk_speed)
                player.y_pos -= player.dash_speed * player.walk_speed
                player.rect.move_ip(0, -1 * player.dash_speed * player.walk_speed)
                player.y_pos -= player.dash_speed * player.walk_speed
                player.rect.move_ip(0, -1 * player.dash_speed * player.walk_speed)
                player.y_pos -= player.dash_speed * player.walk_speed
                player.rect.move_ip(0, -1 * player.dash_speed * player.walk_speed)
                player.y_pos -= player.dash_speed * player.walk_speed
            if player.facing == 'DOWN':
                player.rect.move_ip(0, player.dash_speed * player.walk_speed)
                player.y_pos += player.dash_speed * player.walk_speed
                player.rect.move_ip(0, player.dash_speed * player.walk_speed)
                player.y_pos += player.dash_speed * player.walk_speed
                player.rect.move_ip(0, player.dash_speed * player.walk_speed)
                player.y_pos += player.dash_speed * player.walk_speed
                player.rect.move_ip(0, player.dash_speed * player.walk_speed)
                player.y_pos += player.dash_speed * player.walk_speed
                player.rect.move_ip(0, player.dash_speed * player.walk_speed)
                player.y_pos += player.dash_speed * player.walk_speed
            if player.facing == 'LEFT':
                player.rect.move_ip(-1 * player.dash_speed * player.walk_speed, 0)
                player.x_pos -= player.dash_speed * player.walk_speed
                player.rect.move_ip(-1 * player.dash_speed * player.walk_speed, 0)
                player.x_pos -= player.dash_speed * player.walk_speed
                player.rect.move_ip(-1 * player.dash_speed * player.walk_speed, 0)
                player.x_pos -= player.dash_speed * player.walk_speed
                player.rect.move_ip(-1 * player.dash_speed * player.walk_speed, 0)
                player.x_pos -= player.dash_speed * player.walk_speed
                player.rect.move_ip(-1 * player.dash_speed * player.walk_speed, 0)
                player.x_pos -= player.dash_speed * player.walk_speed
            if player.facing == 'RIGHT':
                player.rect.move_ip(player.dash_speed * player.walk_speed, 0)
                player.x_pos += player.dash_speed * player.walk_speed
                player.rect.move_ip(player.dash_speed * player.walk_speed, 0)
                player.x_pos += player.dash_speed * player.walk_speed
                player.rect.move_ip(player.dash_speed * player.walk_speed, 0)
                player.x_pos += player.dash_speed * player.walk_speed
                player.rect.move_ip(player.dash_speed * player.walk_speed, 0)
                player.x_pos += player.dash_speed * player.walk_speed
                player.rect.move_ip(player.dash_speed * player.walk_speed, 0)
                player.x_pos += player.dash_speed * player.walk_speed
        elif player.dash_counter >= player.dash_duration:
            player.curr_stamina -= 100
            player.dash_used = False
            player.dash_cooldown = True
            
def player_quick_attack(player):
    count = 0
        
def player_held_attack(player):
    count = 0