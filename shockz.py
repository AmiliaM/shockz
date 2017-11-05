# File: shockz.py
# Author: AmiliaM
# Created November 5, 2017, at 12:00 PM

import sys, pygame, pygame.locals
from random import randint
pygame.init()



#setup display
s_size = s_width, s_height = [256, 256]
screen = pygame.display.set_mode(s_size)

#setup colors
black = 0, 0, 0
white = 255, 255, 255

#setup assets
player = pygame.image.load("player.bmp")
playerrect = player.get_rect()

ground = pygame.image.load("ground.bmp")
metal = pygame.image.load("metal.bmp")


#generate floor
def gen_floor(width, height):
    floor = []
    for x in range(0, width):
        row = []
        for y in range(0, height):
            row.append(randint(0,1))
        floor.append(row)
    return floor
current_floor = gen_floor(16, 16)


#run the game
while 1:
    #user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                print "inv"
            elif event.key == pygame.K_q:
                playerrect = playerrect.move(-16, -16)
            elif event.key == pygame.K_w:
                playerrect = playerrect.move(0, -16)
            elif event.key == pygame.K_e:
                playerrect = playerrect.move(16, -16)
            elif event.key == pygame.K_a:
                playerrect = playerrect.move(-16, 0)
            elif event.key == pygame.K_d:
                playerrect = playerrect.move(16, 0)
            elif event.key == pygame.K_z:
                playerrect = playerrect.move(-16, 16)
            elif event.key == pygame.K_x:
                playerrect = playerrect.move(0, 16)
            elif event.key == pygame.K_c:
                playerrect = playerrect.move(16, 16)
            elif event.key == pygame.K_TAB:
                print "cycle"
            elif event.key == pygame.K_RETURN:
                print "fire"


    #turn and processing
    #print playerrect
    

    #draw
    screen.fill(white)

    #ground
    d_pos_y = 0
    for x in current_floor:
        d_pos_x = 0
        for y in x:
            if y:
                screen.blit(ground, (d_pos_x, d_pos_y))
            else:
                screen.blit(metal, (d_pos_x, d_pos_y))
            d_pos_x += 16
        d_pos_y += 16

    #player
    screen.blit(player, playerrect)

    pygame.display.flip()
