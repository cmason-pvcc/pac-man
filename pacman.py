import pygame
import sys
import os

#setting variables
playerScore = 0
startPos = pygame.Vector2(225, 435)
black = (0, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
validItemSpaces = [[(45, 45) , (75, 45) , (105, 45) , (135, 45) , (165, 45) , (195, 45) , None      , None      , (285, 45) , (315, 45) , (345, 45) , (375, 45) , (405, 45) , (435, 45)],
                  [(45, 75) , None     , None      , (135, 75) , None      , (195, 75) , None      , None      , (285, 75) , None      , (345, 75) , None      , None      , (435, 75)],
                  [(45, 105), (75, 105), (105, 105), (135, 105), None      , (195, 105), None      , None      , (285, 105), None      , (345, 105), (375, 105), (405, 105), (435, 105)],
                  [None     , None     , (105, 135), None      , (165, 135), (195, 135), (225, 135), (255, 135), (285, 135), (315, 135), None      , (375, 135), None      , None],
                  [None     , None     , (105, 165), (135, 165), (165, 165), None      , None      , None      , None      , (315, 165), (345, 165), (375, 165), None      , None],
                  [None     , None     , (105, 195), None      , (165, 195), (195, 195), None      , None      , (285, 195), (315, 195), None      , (375, 195), None      , None],
                  [None     , None     , (105, 225), None      , (165, 225), (195, 225), (225, 225), (255, 225), (285, 225), (315, 225), None      , (375, 225), None      , None],
                  [None     , None     , (105, 255), None      , (165, 255), (195, 255), None      , None      , (285, 255), (315, 255), None      , (375, 255), None      , None],
                  [None     , None     , (105, 285), (135, 285), (165, 285), (195, 285), (225, 285), (255, 285), (285, 285), (315, 285), (345, 285), (375, 285), None      , None],
                  [None     , None     , (105, 315), (135, 315), (165, 315), None      , None      , None      , None      , (315, 315), (345, 315), (375, 315), None      , None],
                  [None     , None     , (105, 345), None      , (165, 345), (195, 345), None      , None      , (285, 345), (315, 345), None      , (375, 345), None      , None],
                  [(45, 375), (75, 375), (105, 375), None      , (165, 375), (195, 375), (225, 375), (255, 375), (285, 375), (315, 375), None      , (375, 375), (405, 375), (435, 375)],
                  [(45, 405), None     , None      , None      , None      , None      , (225, 405), (255, 405), None      , None      , None      , None      , None      , (435, 405)],
                  [(45, 435), (75, 435), (105, 435), (135, 435), (165, 435), (195, 435), (225, 435), (255, 435), (285, 435), (315, 435), (345, 435), (375, 435), (405, 435), (435, 435)]]
validDotSpaces = validItemSpaces
dots = []

#initializing pygame
pygame.init()
screen = pygame.display.set_mode((480, 480))
clock = pygame.time.Clock()
pygame.font.init()
pygame.display.init()
startButtonPressed = False
running = True

def DrawDots(spaces):
    dots.clear()
    for i in range(len(spaces)):
        for j in range(len(spaces[i])):
            if spaces[i][j] != None:
                dots.append(pygame.draw.circle(screen, white, spaces[i][j], 5))

#pre-game loop
while (not startButtonPressed) and running:
    #rendering
    screen.fill(black)
    startButton = pygame.draw.rect(screen, white, (140, 215, 200, 50))
    startButtonText = pygame.font.Font.render(pygame.font.Font(None, 50), "START", False, black)
    screen.blit(startButtonText, (240 - startButtonText.get_rect().centerx, 240 - startButtonText.get_rect().centery))

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] < 340 and pygame.mouse.get_pos()[0] > 140 and pygame.mouse.get_pos()[1] < 265 and pygame.mouse.get_pos()[1] > 215:
                startButtonPressed = True
                print("pressed")

    pygame.display.flip()

playerPos = startPos
vInput = 0
hInput = 0
dt = 0

#game loop
while running:
    #draw objects
    screen.fill(black)
    maze = [pygame.draw.rect(screen, blue, (0, 0, 30, 150)), pygame.draw.rect(screen, blue, (30, 0, 420, 30)), pygame.draw.rect(screen, blue, (450, 0, 30, 150)), pygame.draw.rect(screen, blue, (210, 30, 60, 90)), pygame.draw.rect(screen, blue, (30, 120, 60, 30)), pygame.draw.rect(screen, blue, (60, 150, 30, 60)), pygame.draw.rect(screen, blue, (0, 180, 60, 30)), pygame.draw.rect(screen, blue, (0, 270, 60, 30)), pygame.draw.rect(screen, blue, (60, 270, 30, 60)), pygame.draw.rect(screen, blue, (30, 330, 60, 30)), pygame.draw.rect(screen, blue, (0, 330, 30, 150)), pygame.draw.rect(screen, blue, (30, 450, 420, 30)), pygame.draw.rect(screen, blue, (450, 330, 30, 150)), pygame.draw.rect(screen, blue, (390, 330, 60, 30)), pygame.draw.rect(screen, blue, (390, 270, 30, 60)), pygame.draw.rect(screen, blue, (420, 270, 60, 30)), pygame.draw.rect(screen, blue, (420, 180, 60, 30)), pygame.draw.rect(screen, blue, (390, 150, 30, 60)), pygame.draw.rect(screen, blue, (390, 120, 60, 30)), pygame.draw.rect(screen, blue, (60, 60, 60, 30)), pygame.draw.rect(screen, blue, (150, 60, 30, 60)), pygame.draw.rect(screen, blue, (120, 120, 30, 30)), pygame.draw.rect(screen, blue, (180, 150, 120, 30)), pygame.draw.rect(screen, blue, (210, 180, 60, 30)), pygame.draw.rect(screen, blue, (120, 180, 30, 90)), pygame.draw.rect(screen, blue, (210, 240, 60, 30)), pygame.draw.rect(screen, blue, (180, 300, 120, 30)), pygame.draw.rect(screen, blue, (210, 330, 60, 30)), pygame.draw.rect(screen, blue, (120, 330, 30, 60)), pygame.draw.rect(screen, blue, (60, 390, 150, 30)), pygame.draw.rect(screen, blue, (330, 330, 30, 60)), pygame.draw.rect(screen, blue, (270, 390, 150, 30)), pygame.draw.rect(screen, blue, (330, 180, 30, 90)), pygame.draw.rect(screen, blue, (360, 60, 60, 30)), pygame.draw.rect(screen, blue, (300, 60, 30, 60)), pygame.draw.rect(screen, blue, (330, 120, 30, 30))]
    DrawDots(validDotSpaces)
    
    oldPos = playerPos.copy()

    #make sure game closes properly
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #detect input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        vInput = -1
        hInput = 0
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        vInput = 1
        hInput = 0
    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        hInput = -1
        vInput = 0
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        hInput = 1
        vInput = 0

    #move player
    playerPos.x += 150 * hInput * dt
    playerPos.y += 150 * vInput * dt
    player = pygame.draw.circle(screen, yellow, playerPos, 13)

    #detect and handle dot collision
    for dot in range(len(dots)):
        if player.colliderect(dots[dot]):
            validDotSpaces[int((dots[dot].y - 25)/30)][int((dots[dot].x - 25)/30)] = None
            dots[dot] = None
            playerScore += 10
    if dots.__contains__(None):
        dots.remove(None)
    if dots == []:
        running = False

    if player.collidelist(maze) != -1:
        while player.collidelist(maze) != -1:
            playerPos += pygame.Vector2(-1 * hInput, -1 * vInput)
            player = pygame.draw.circle(screen, yellow, playerPos, 13)
            print(playerPos)
        hInput = 0
        vInput = 0

    pygame.display.flip()

    dt = clock.tick(60) / 1000

print(playerScore)
pygame.quit()