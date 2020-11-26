# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:41:06 2020

@author: User
"""

import pygame
import random
UP= 0
RIGHT= 1
DOWN= 2
LEFT= 3

pygame.init()
altura= 600
largura= 800
tela= pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo final')
comida= pygame.Surface((10,10))
comida.fill((0,0,255))
lugar_comida= (random.randint(0,590),random.randint(0,590))
cobra= [(200,200), (210,200), (220,200)]
cobrinha= pygame.Surface((10,10))
cobrinha.fill((0,255,0))
direcao= LEFT

clock= pygame.time.Clock()
while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direcao= UP
            if event.key == pygame.K_RIGHT:
                direcao= RIGHT
            if event.key == pygame.K_DOWN:
                direcao= DOWN
            if event.key == pygame.K_LEFT:
                direcao= LEFT
    if direcao  == UP:
        cobra[0]= (cobra[0] [0], cobra[0] [1] -10)
    if direcao  == DOWN:
        cobra[0]= (cobra[0] [0], cobra[0] [1] +10)
    if direcao  == RIGHT:
        cobra[0]= (cobra[0] [0] +10, cobra[0] [1])
    if direcao  == LEFT:
        cobra[0]= (cobra[0] [0] -10, cobra[0] [1])
     
    for i in range(len(cobra) -1, 0, -1):
        cobra[i]= (cobra[i-1][0], cobra[i-1][1])
    
    tela.fill((0,0,0))
    tela.blit(comida, lugar_comida)
    for posicao in cobra:
        tela.blit(cobrinha,posicao)
    pygame.display.update()        