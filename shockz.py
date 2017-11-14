# File: shockz.py
# Author: AmiliaM
# Created November 5, 2017, at 12:00 PM

import sys, pygame, pygame.locals
from random import randint
pygame.init()

# ---------------> Launch Settings <--------------- #
#Size settings
boardWidth = 16
boardHeight = 16
tileWidth = 16
tileHeight = 16

#Colors
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0


tickRate = 10

# ---------------> Function Defs <--------------- #
#def checkPlayerInput():

def gameover():
    font = pygame.font.SysFont(None, 48)
    deathmessage = font.render('You died!', True, red)
    textrect = deathmessage.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return
        screen.fill(black)
        screen.blit(deathmessage, textrect)
        pygame.display.flip()

def win():
    font = pygame.font.SysFont(None, 48)
    winmessage = font.render('You win', True, red)
    textrect = winmessage.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return
        screen.fill(black)
        screen.blit(winmessage, textrect)
        pygame.display.flip()

def gen_floor(width, height):
    floor = []
    for x in range(0, width):
        row = []
        for y in range(0, height):
            row.append(randint(0, 1))
        floor.append(row)
    return floor

def gen_monsters():
    monsters = []
    for i in range(0, monsternum):
        x_pos = tileWidth*randint(0, boardWidth-1)
        y_pos = tileHeight*randint(0, boardHeight-1)
        newmob = [x_pos, y_pos]
        monsters.append(newmob)
    return monsters



# ---------------> Game Setup <--------------- #

#setup display
s_size = s_width, s_height = [boardWidth*tileWidth, boardHeight*tileHeight]
screen = pygame.display.set_mode(s_size)


#setup assets
player = pygame.image.load("player.bmp")
playerrect = player.get_rect()

ground = pygame.image.load("ground.bmp")
ground2 = pygame.image.load("ground2.bmp")

monster = pygame.image.load("monster.bmp")


#generate floor
current_floor = gen_floor(boardWidth, boardHeight)

#setup monsters
monsternum = randint(1, 5)
current_monsters = gen_monsters()

# ---------------> Run Game <--------------- #
clock = pygame.time.Clock()
tarIndex = 0
target = current_monsters[tarIndex]

while 1:
    #user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                print "inv"
            elif event.key == pygame.K_q:
                playerrect = playerrect.move(-tileWidth, -tileHeight)
            elif event.key == pygame.K_w:
                playerrect = playerrect.move(0, -tileHeight)
            elif event.key == pygame.K_e:
                playerrect = playerrect.move(tileWidth, -tileHeight)
            elif event.key == pygame.K_a:
                playerrect = playerrect.move(-tileWidth, 0)
            elif event.key == pygame.K_d:
                playerrect = playerrect.move(tileWidth, 0)
            elif event.key == pygame.K_z:
                playerrect = playerrect.move(-tileWidth, tileHeight)
            elif event.key == pygame.K_x:
                playerrect = playerrect.move(0, tileHeight)
            elif event.key == pygame.K_c:
                playerrect = playerrect.move(tileWidth, tileHeight)
            elif event.key == pygame.K_TAB:
                print "cycle"
                tarIndex += 1
                if tarIndex >= monsternum: 
                    tarIndex = 0
            elif event.key == pygame.K_RETURN:
                player_floor_type = current_floor[playerrect[0]/16][playerrect[1]/16]
                mob_floor_type = current_floor[current_monsters[tarIndex][0]/16][current_monsters[tarIndex][1]/16]
                print player_floor_type
                print mob_floor_type
                if player_floor_type == mob_floor_type:
                    current_monsters.remove(current_monsters[tarIndex])

    #turn and processing
    if len(current_monsters) < 1:
        win()
        break
    #player bounds
    if playerrect[0] < 0:
        playerrect[0] = 0
    elif playerrect[0] > boardWidth*(tileWidth-1):
        playerrect[0] = boardWidth*(tileWidth-1)
    if playerrect[1] < 0:
        playerrect[1] = 0
    elif playerrect[1] > boardHeight*(tileHeight-1):
        playerrect[1] = boardHeight*(tileHeight-1)

    #mob movement and bounds
    for mob in current_monsters:
        mob[0] += tileWidth*randint(-1, 1)
        if mob[0] < 0:
            mob[0] = 0
        elif mob[0] > boardWidth*(tileWidth-1):
            mob[0] = boardWidth*(tileWidth-1)
        mob[1] += tileHeight*randint(-1, 1)
        if mob[1] < 0:
            mob[1] = 0
        elif mob[1] > boardHeight*(tileHeight-1):
            mob[1] = boardHeight*(tileHeight-1)

        if mob[0] == playerrect[0]:
            if mob[1] == playerrect[1]:
                gameover()
                pass

    target = current_monsters[tarIndex]
    print target

    clock.tick(tickRate)

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
                screen.blit(ground2, (d_pos_x, d_pos_y))
            d_pos_x += 16
        d_pos_y += 16

    #player
    screen.blit(player, playerrect)

    #monsters
    for mob in current_monsters:
        mobpos = (mob[0], mob[1])
        screen.blit(monster, mobpos)

    pygame.display.flip()

