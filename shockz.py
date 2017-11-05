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

monster = pygame.image.load("monster.bmp")


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

#setup monsters
monsternum = randint(0, 5)
def gen_monsters():
    monsters = []
    for i in range(0, monsternum):
        x_pos = 16*randint(0, 15)
        y_pos = 16*randint(0, 15)
        newmob = [x_pos, y_pos]
        monsters.append(newmob)
    return monsters
current_monsters = gen_monsters()
print current_floor

#run the game
clock = pygame.time.Clock()
tar_index = 0
target = current_monsters[tar_index]
gameover = False


while gameover == False:
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
                tar_index += 1
                if tar_index >= monsternum: 
                    tar_index = 0
            elif event.key == pygame.K_RETURN:
                player_floor_type = current_floor[playerrect[0]/16][playerrect[1]/16]
                mob_floor_type = current_floor[current_monsters[tar_index][0]/16][current_monsters[tar_index][1]/16]
                print player_floor_type
                print mob_floor_type
                if player_floor_type == mob_floor_type:
                    current_monsters.remove(current_monsters[tar_index])



    #turn and processing
    #player bounds
    if playerrect[0] < 0:
        playerrect[0] = 0
    elif playerrect[0] > 240:
        playerrect[0] = 240
    if playerrect[1] < 0:
        playerrect[1] = 0
    elif playerrect[1] > 240:
        playerrect[1] = 240

    #mob movement and bounds
    for mob in current_monsters:
        mob[0] += 16*randint(-1, 1)
        if mob[0] < 0:
            mob[0] = 0
        elif mob[0] > 240:
            mob[0] = 240
        mob[1] += 16*randint(-1, 1)
        if mob[1] < 0:
            mob[1] = 0
        elif mob[1] > 240:
            mob[1] = 240
        
        if mob[0] == playerrect[0]:
            if mob[1] == playerrect[1]:
                gameover = True

    target = current_monsters[tar_index]
    print target

    clock.tick(10)

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

    #monsters
    for mob in current_monsters:
        mobpos = (mob[0], mob[1])
        screen.blit(monster, mobpos)

    pygame.display.flip()

font = pygame.font.SysFont(None, 48)
deathmessage = font.render('You died!', True, (255, 0, 0))
textrect = deathmessage.get_rect()
textrect.centerx = screen.get_rect().centerx
textrect.centery = screen.get_rect().centery
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(deathmessage, textrect)

    pygame.display.flip()