import pygame
import sys
import os
import random
import copy

#setting variables
playerScore = 0
startPos = pygame.Vector2(225, 435)
black = (0, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
validItemSpaces = [[(45, 45) , (75, 45) , (105, 45) , (135, 45) , (165, 45) , (195, 45) , None      , None      , (285, 45) , (315, 45) , (345, 45) , (375, 45) , (405, 45) , (435, 45)],
                  [(45, 75) , None     , None      , (135, 75) , None      , (195, 75) , None      , None      , (285, 75) , None      , (345, 75) , None      , None      , (435, 75)],
                  [(45, 105), (75, 105), (105, 105), (135, 105), None      , (195, 105), None      , None      , (285, 105), None      , (345, 105), (375, 105), (405, 105), (435, 105)],
                  [None     , None     , (105, 135), None      , (165, 135), (195, 135), (225, 135), (255, 135), (285, 135), (315, 135), None      , (375, 135), None      , None],
                  [None     , None     , (105, 165), None      , (165, 165), None      , None      , None      , None      , (315, 165), None      , (375, 165), None      , None],
                  [None     , None     , (105, 195), (135, 195), (165, 195), (195, 195), None      , None      , (285, 195), (315, 195), (345, 195), (375, 195), None      , None],
                  [None     , None     , (105, 225), None      , None      , (195, 225), (225, 225), (255, 225), (285, 225), None      , None      , (375, 225), None      , None],
                  [None     , None     , (105, 255), None      , None      , (195, 255), None      , None      , (285, 255), None      , None      , (375, 255), None      , None],
                  [None     , None     , (105, 285), (135, 285), (165, 285), (195, 285), (225, 285), (255, 285), (285, 285), (315, 285), (345, 285), (375, 285), None      , None],
                  [None     , None     , (105, 315), None      , (165, 315), None      , None      , None      , None      , (315, 315), None      , (375, 315), None      , None],
                  [None     , None     , (105, 345), None      , (165, 345), (195, 345), None      , None      , (285, 345), (315, 345), None      , (375, 345), None      , None],
                  [(45, 375), (75, 375), (105, 375), None      , None      , (195, 375), (225, 375), (255, 375), (285, 375), None      , None      , (375, 375), (405, 375), (435, 375)],
                  [(45, 405), None     , None      , None      , None      , None      , (225, 405), None      , None      , None      , None      , None      , None      , (435, 405)],
                  [(45, 435), (75, 435), (105, 435), (135, 435), (165, 435), (195, 435), (225, 435), (255, 435), (285, 435), (315, 435), (345, 435), (375, 435), (405, 435), (435, 435)]]
validDotSpaces = copy.deepcopy(validItemSpaces)
dots = []

#initializing pygame
pygame.init()
screen = pygame.display.set_mode((480, 480))
clock = pygame.time.Clock()
pygame.font.init()
pygame.display.init()
startButtonPressed = False
running = True
gameRunning = False

def DrawDots(spaces):
    dots.clear()
    for i in range(len(spaces)):
        for j in range(len(spaces[i])):
            if spaces[i][j] != None:
                dots.append(pygame.draw.circle(screen, white, spaces[i][j], 5))

def SpawnFruit():
    fruitPos = validItemSpaces[random.randint(0, 13)][random.randint(0, 13)]
    if fruitPos == None:
        while fruitPos == None:
            fruitPos = validItemSpaces[random.randint(0, 13)][random.randint(0, 13)]
    return fruitPos

#pre-game loop
while (not startButtonPressed) and running:
    #rendering
    screen.fill(black)
    startButton = pygame.draw.rect(screen, white, (140, 215, 200, 50))
    startButtonText = pygame.font.Font.render(pygame.font.Font(None, 50), "START", False, black)
    screen.blit(startButtonText, (startButton.centerx - startButtonText.get_rect().centerx, startButton.centery - startButtonText.get_rect().centery))

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] < startButton.right and pygame.mouse.get_pos()[0] > startButton.left and pygame.mouse.get_pos()[1] < startButton.bottom and pygame.mouse.get_pos()[1] > startButton.top:
                startButtonPressed = True
                gameRunning = True

    pygame.display.flip()

while running:
    playerPos = startPos.copy()
    vInput = 0
    hInput = 0
    hDir = 0
    vDir = 0
    oldHDir = 0
    oldVDir = 0
    dt = 0
    showFruit = False
    fruitDelay = random.randint(2000, 5000)/1000
    fruitPos = SpawnFruit()
    fruit = [pygame.draw.rect(screen, green, (-100, 0, 1, 1))]

    #game loop
    while gameRunning and running:
        #draw objects
        screen.fill(black)
        maze = [pygame.draw.rect(screen, blue, (0, 0, 30, 150)), pygame.draw.rect(screen, blue, (30, 0, 420, 30)), pygame.draw.rect(screen, blue, (450, 0, 30, 150)), pygame.draw.rect(screen, blue, (210, 30, 60, 90)), pygame.draw.rect(screen, blue, (30, 120, 60, 30)), pygame.draw.rect(screen, blue, (60, 150, 30, 60)), pygame.draw.rect(screen, blue, (0, 180, 60, 30)), pygame.draw.rect(screen, blue, (0, 240, 60, 30)), pygame.draw.rect(screen, blue, (60, 240, 30, 90)), pygame.draw.rect(screen, blue, (30, 330, 60, 30)), pygame.draw.rect(screen, blue, (0, 330, 30, 150)), pygame.draw.rect(screen, blue, (30, 450, 420, 30)), pygame.draw.rect(screen, blue, (450, 330, 30, 150)), pygame.draw.rect(screen, blue, (390, 330, 60, 30)), pygame.draw.rect(screen, blue, (390, 240, 30, 90)), pygame.draw.rect(screen, blue, (420, 240, 60, 30)), pygame.draw.rect(screen, blue, (420, 180, 60, 30)), pygame.draw.rect(screen, blue, (390, 150, 30, 60)), pygame.draw.rect(screen, blue, (390, 120, 60, 30)), pygame.draw.rect(screen, blue, (60, 60, 60, 30)), pygame.draw.rect(screen, blue, (150, 60, 30, 60)), pygame.draw.rect(screen, blue, (120, 120, 30, 60)), pygame.draw.rect(screen, blue, (180, 150, 120, 30)), pygame.draw.rect(screen, blue, (210, 180, 60, 30)), pygame.draw.rect(screen, blue, (120, 210, 60, 60)), pygame.draw.rect(screen, blue, (210, 240, 60, 30)), pygame.draw.rect(screen, blue, (180, 300, 120, 30)), pygame.draw.rect(screen, blue, (210, 330, 60, 30)), pygame.draw.rect(screen, blue, (120, 300, 30, 90)), pygame.draw.rect(screen, blue, (60, 390, 150, 30)), pygame.draw.rect(screen, blue, (330, 300, 30, 90)), pygame.draw.rect(screen, blue, (240, 390, 180, 30)), pygame.draw.rect(screen, blue, (300, 210, 60, 60)), pygame.draw.rect(screen, blue, (360, 60, 60, 30)), pygame.draw.rect(screen, blue, (300, 60, 30, 60)), pygame.draw.rect(screen, blue, (330, 120, 30, 60)), pygame.draw.rect(screen, blue, (150, 360, 30, 30)), pygame.draw.rect(screen, blue, (300, 360, 30, 30))]
        leftTP = pygame.draw.rect(screen, black, (0, 210, 1, 30))
        rightTP = pygame.draw.rect(screen, black, (479, 210, 1, 30))
        DrawDots(validDotSpaces)
        if fruitDelay <= 0:
            showFruit = True
        if showFruit:
            fruit = [pygame.draw.rect(screen, white, (fruitPos[0], fruitPos[1] - 12, 2, 4)), pygame.draw.rect(screen, green, (fruitPos[0] - 6, fruitPos[1] - 10, 6, 2)), pygame.draw.rect(screen, green, (fruitPos[0] + 2, fruitPos[1] - 10, 6, 2)), pygame.draw.rect(screen, green, (fruitPos[0] - 4, fruitPos[1] - 8, 10, 2)), pygame.draw.rect(screen, green, (fruitPos[0], fruitPos[1] - 6, 2, 2)), pygame.draw.rect(screen, red, (fruitPos[0] - 10, fruitPos[1] - 6, 2, 8)), pygame.draw.rect(screen, red, (fruitPos[0] - 8, fruitPos[1] - 8, 2, 14)), pygame.draw.rect(screen, red, (fruitPos[0] - 6, fruitPos[1] - 8, 2, 16)), pygame.draw.rect(screen, red, (fruitPos[0] - 4, fruitPos[1] - 6, 4, 16)), pygame.draw.rect(screen, red, (fruitPos[0], fruitPos[1] - 4, 2, 16)), pygame.draw.rect(screen, red, (fruitPos[0] + 2, fruitPos[1] - 6, 4, 16)), pygame.draw.rect(screen, red, (fruitPos[0] + 6, fruitPos[1] - 8, 4, 14)), pygame.draw.rect(screen, red, (fruitPos[0] + 10, fruitPos[1] - 6, 2, 8)), pygame.draw.rect(screen, white, (fruitPos[0] - 8, fruitPos[1] - 4, 2, 2)), pygame.draw.rect(screen, white, (fruitPos[0] - 6, fruitPos[1] + 2, 2, 2)), pygame.draw.rect(screen, white, (fruitPos[0] - 4, fruitPos[1] - 2, 2, 2)), pygame.draw.rect(screen, white, (fruitPos[0] - 2, fruitPos[1] + 6, 2, 2)), pygame.draw.rect(screen, white, (fruitPos[0], fruitPos[1] - 2, 2, 2)), pygame.draw.rect(screen, white, (fruitPos[0], fruitPos[1] + 2, 2, 2)), pygame.draw.rect(screen, white, (fruitPos[0] + 4, fruitPos[1] - 4, 2, 2)), pygame.draw.rect(screen, white, (fruitPos[0] + 4, fruitPos[1] + 6, 2, 2)), pygame.draw.rect(screen, white, (fruitPos[0] + 6, fruitPos[1], 2, 2)), pygame.draw.rect(screen, white, (fruitPos[0] + 8, fruitPos[1] - 6, 2, 2))]

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
        player = pygame.draw.circle(screen, yellow, playerPos, 14)

        #detect and handle dot collision
        for dot in range(len(dots)):
            if player.colliderect(dots[dot]):
                validDotSpaces[int((dots[dot].y - 25)/30)][int((dots[dot].x - 25)/30)] = None
                dots[dot] = None
                playerScore += 10
        if dots.__contains__(None):
            dots.remove(None)
        if dots == []:
            gameRunning = False

        #fruit collision
        if player.collidelist(fruit) != -1 and showFruit:
            showFruit = False
            playerScore += 50
            fruitPos = SpawnFruit()
            fruitDelay = random.randint(2000, 5000)/1000

        #wall collision
        if player.collidelist(maze) != -1:
            playerPos = oldPos.copy()
            if oldHDir != hInput and oldVDir != vInput and vInput + hInput != 0:
                screen.fill(black, player)
                playerPos.x += 150 * oldHDir * dt
                playerPos.y += 150 * oldVDir * dt
                player = pygame.draw.circle(screen, yellow, playerPos, 14)
                if player.collidelist(maze) != -1:
                    screen.fill(black, player)
                    playerPos = oldPos.copy()
                    hInput = 0
                    vInput = 0
                    player = pygame.draw.circle(screen, yellow, playerPos, 14)
            else:
                hInput = 0
                vInput = 0
        else:
            oldHDir = hInput
            oldVDir = vInput

        #teleportation
        if player.colliderect(leftTP):
            playerPos = pygame.Vector2(466, 225)
        if player.colliderect(rightTP):
            playerPos = pygame.Vector2(14, 225)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        fruitDelay -= dt
    
    restartButtonPressed = False

    #post-game loop
    while (not restartButtonPressed) and running:
        #rendering
        screen.fill(black)
        restartButton = pygame.draw.rect(screen, white, (140, 215, 200, 50))
        restartButtonText = pygame.font.Font.render(pygame.font.Font(None, 50), "RESTART", False, black)
        screen.blit(restartButtonText, (restartButton.centerx - restartButtonText.get_rect().centerx, restartButton.centery - restartButtonText.get_rect().centery))
        quitButton = pygame.draw.rect(screen, white, (140, 315, 200, 50))
        quitButtonText = pygame.font.Font.render(pygame.font.Font(None, 50), "QUIT", False, black)
        screen.blit(quitButtonText, (quitButton.centerx - quitButtonText.get_rect().centerx, quitButton.centery - quitButtonText.get_rect().centery))
        scoreText = pygame.font.Font.render(pygame.font.Font(None, 50), "SCORE: " + str(playerScore), False, white)
        screen.blit(scoreText, (240 - scoreText.get_rect().centerx, 140 - scoreText.get_rect().centery))

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] < restartButton.right and pygame.mouse.get_pos()[0] > restartButton.left and pygame.mouse.get_pos()[1] < restartButton.bottom and pygame.mouse.get_pos()[1] > restartButton.top:
                    validDotSpaces = copy.deepcopy(validItemSpaces)
                    playerScore = 0
                    restartButtonPressed = True
                    gameRunning = True
                    print("pressed")
                elif pygame.mouse.get_pos()[0] < quitButton.right and pygame.mouse.get_pos()[0] > quitButton.left and pygame.mouse.get_pos()[1] < quitButton.bottom and pygame.mouse.get_pos()[1] > quitButton.top:
                    running = False
                    print("pressed")

        pygame.display.flip()
        dt = clock.tick(60) / 1000

pygame.quit()