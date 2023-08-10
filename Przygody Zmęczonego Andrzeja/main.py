import pygame
import function
import time
#parameters of the window
WIDTH = 800
HEIGHT = 600
#starting pygame
pygame.init()
#building a window
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#strings
bg0 = pygame.image.load("images/backgrounds/bg0.png")
bg1 = pygame.image.load("images/backgrounds/bg1.png")
an = pygame.image.load("images/characters/andrzej.png")
fn = function
font = pygame.font.SysFont("Cascadia", 26)
cl = pygame.time.Clock()
running = True
scene = 1
an_x = 20
an_y = 480
move_speed = 15
energy = 100
move = False
pygame.time.set_timer(pygame.USEREVENT, 5000)
#intro
screen.fill((0,0,0))
fn.text("Jesteś Andrzej, masz 42 lata",font,(300,300),screen)
pygame.display.flip()
time.sleep(5)
screen.fill((0,0,0))
fn.text("Właśnie wracasz do domu, jednak nie wiesz gdzie jest",font,(240,260),screen)
pygame.display.flip()
time.sleep(5)
screen.fill((0,0,0))
fn.text("Twoim celem jest odnalezienie mieszkania w jednym z bloków",font,(200,280),screen)
pygame.display.flip()
time.sleep(5)

#loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                scene += 1
            if event.key == pygame.K_w:
                an_y = an_y - move_speed
                move = True
            if event.key == pygame.K_s:
                an_y += move_speed
                move = True
            if event.key == pygame.K_d:
                an_x += move_speed
                move = True
            if event.key == pygame.K_a:
                an_x -= move_speed
                move = True
            if event.key == pygame.K_r:
                scene = 1
                move = True
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT & move == True:
            energy -= 5
    if scene == 1:
        screen.blit(bg1,(0,0))
        screen.blit(an,(an_x,an_y))
        fn.text("Wejdź do bloku:[f]",font,(40,40), screen)
        fn.text(f"Energia:{energy}",font,(650,40),screen)
        pygame.display.flip()
    elif scene == 2:
        screen.blit(bg0,(0,0))
        screen.blit(an,(an_x,an_y))
        fn.text("Wejdź do mieszkania:[f]",font,(20,20), screen)
        fn.text("Wróc na podwórko:[r]",font,(20,40), screen)
        pygame.display.flip()
    cl.tick(30)

pygame.quit()
