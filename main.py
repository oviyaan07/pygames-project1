import pygame
pygame.init()

screen=pygame.display.set_mode((720,657))

pygame.display.set_caption("aye it's RR")

rr=pygame.image.load("RR.png")

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    screen.fill((126,87,123))
    screen.blit(rr,(257,359))
    pygame.display.update()

pygame.quit()