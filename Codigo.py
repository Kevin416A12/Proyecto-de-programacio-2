import pygame

pygame.init()

screen_width = 800
screen_heigt = 600

screen = pygame.display.set_mode((screen_width , screen_heigt))
run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()