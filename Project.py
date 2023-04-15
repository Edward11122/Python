import os
import random
import pygame

###############################################################################################################################################################################################################################
# Initialize game
pygame.init()

# Set screen
screen_width = 1024
screen_height = 320
screen = pygame.display.set_mode((screen_width, screen_height))

# Set game title
pygame.display.set_caption("Edward")

# FPS (Frame per Second)
clock = pygame.time.Clock()
###############################################################################################################################################################################################################################

# User game initialize
current_path = os.path.dirname(__file__) # Position of file
image_path = os.path.join(current_path, "images") 

background = pygame.image.load(os.path.join(image_path, "P_background.png"))

# Character
character = pygame.image.load(os.path.join(image_path, "P_character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 8) - (character_width /2)
character_y_pos = screen_height - character_height

character_to_y = 0

character_speed = 0.6

#Bullet
bullet = pygame.image.load(os.path.join(image_path, "P_bullet.png"))
bullet_size = bullet.get_rect().size
bullet_width = bullet_size[0]
bullet_height = bullet_size[1]

bullets = []

bullet_speed = 1.6

# Enemy
enemy = pygame.image.load(os.path.join(image_path, "P_enemy.png"))
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) + enemy_width
enemy_y_pos = (screen_height/2) - (enemy_height)
enemy_speed = 5

# Remove bullets
bullet_to_remove = -1


# Config
game_font = pygame.font.Font(None, 40)

total_time = 100

start_ticks = pygame.time.get_ticks()

running = True
while running:
    frame = clock.tick(240)  #10~240

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_w:
                character_to_y -= character_speed
            elif event.key == pygame.K_SPACE:
                bullet_x_position = character_x_pos + (character_width)
                bullet_y_pos = character_y_pos - (character_height / 2)
                bullets.append([bullet_x_position, bullet_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                character_to_y =0

    # Character position
    character_to_y += 0.01
    character_y_pos += character_to_y * frame

    # Bullets position
    bullets = [[b[0] + bullet_speed, b[1]] for b in bullets]
    bullets = [[b[0], b[1]] for b in bullets if b[0] < 1024]

    # Enemy position
    enemy_x_pos -= enemy_speed

    if enemy_x_pos < 0 :
        enemy_x_pos = screen_width + enemy_width

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_width

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("Collider !")
        running = False

    screen.blit(background, (0,0))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(character, (character_x_pos, character_y_pos))

    for bullet_x_pos, bullet_y_pos in bullets :
        screen.blit(bullet, (bullet_x_pos, bullet_y_pos))

    past_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(round((total_time-past_time),2)), True, (255, 255, 255))

    screen.blit(timer, (10,10))

    if total_time - past_time <= 0:
        print("time out")
        running = False

    pygame.display.update()

pygame.time.delay(2000)         
pygame.quit()