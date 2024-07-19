import pygame

# Assign player attributes
class player(pygame.sprite.Sprite):
    def __init__(self):
        super(player, self).__init__()
        # Graphics
        self.surf = pygame.image.load("graphics/sprites/player_right.png").convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(center=(50,540))
        self.facing = 'RIGHT'
        # Positioning
        self.x_pos = 0
        self.y_pos = 0
        # Attributes
        self.max_health = 300
        self.curr_health = 300
        self.max_stamina = 300
        self.curr_stamina = 300
        self.invincibilty = False
        # Regeneration
        self.stamina_cooldown_duration = 250
        self.stamina_cooldown_counter = 0
        self.stamina_lockout = False
        #self.dc = 0
        #self.dc_cd = 0
        #self.lives = 3
        # Movement
        self.walk_speed = 2
        self.run_speed = 2
        self.running_used = False
        self.character_running = False
        # Dash
        self.dash_speed = 4
        self.dash_duration = 7
        self.dash_cooldown_duration = 150
        self.dash_cooldown_counter = 0
        self.dash_counter = 0
        self.dash_used = False
        self.dash_cooldown = False
        
# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class enemy_1(pygame.sprite.Sprite):
    def __init__(self,curr_settings):
        self.surf = pygame.image.load("graphics/sprites/enemy_1.png").convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.speed = 10
        
    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update_enemy_1_pos(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()