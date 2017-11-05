# File: shockz.py
# Author: Amilia
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

#setup keys
but_inv = "K_s"
but_cycle = "K_TAB"
but_fire = "K_RETURN"
but_mv_n = "K_w"
but_mv_s = "K_x"
but_mv_e = "K_d"
but_mv_w = "K_a"
but_mv_ne = "K_e"
but_mv_nw = "K_q"
but_mv_se = "K_c"
but_mv_sw = "K_z"


#run the game
while 1:
    #user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


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
    #screen.blit(player, playerrect)

    pygame.display.flip()
