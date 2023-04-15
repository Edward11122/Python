import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Edward")

background = pygame.image.load("C:\\Users\\edwar\\Vision Coding\\Game\\images\\Background.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0,0))

    pygame.display.update()
            
pygame.quit()