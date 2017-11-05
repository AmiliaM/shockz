import sys, pygame
pygame.init()

size = width, height = [1024, 768]
screen = pygame.display.set_mode(size)

black = 0, 0, 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
