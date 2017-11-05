import sys, pygame
pygame.init()

size = width, height = [1024, 768]
screen = pygame.display.set_mode(size)

black = 0, 0, 0

player = pygame.image.load("player.bmp")
playerrect = player.get_rect()

while 1:
    #user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #turn and processing
    print playerrect
    
    #draw
    screen.fill(black)
    screen.blit(player, playerrect)
    pygame.display.flip()
