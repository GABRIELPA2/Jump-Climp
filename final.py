import pygame
import random
UP= 0
RIGHT= 1
DOWN= 2
LEFT= 3
icon= pygame.image.load('icon.jpg')
def posicaocomida():
    x= random.randint(0,590)
    y= random.randint(0,590)
    return (x//10 * 10, y//10 * 10)
def colisao(com,cob):
    return (com[0] == cob[0] and com[1] == cob[1])

pygame.init()
altura= 600
largura= 800
tela= pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo final')
comida= pygame.Surface((10,10))
comida.fill((255,0,0))
lugar_comida= posicaocomida()
cobra= [(200,200), (210,200), (220,200)]
cobrinha= pygame.Surface((10,10))
cobrinha.fill((0,255,0))
direcao= LEFT
Game= True
a=10
clock= pygame.time.Clock()
while Game:
    clock.tick(a)
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
    if colisao(cobra[0],lugar_comida):
        lugar_comida= posicaocomida()
        cobra.append((0,0))
        a+=1
        
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
        
    for per in cobra:
        if cobra[0][0] == per:
            pygame.quit()
            Game= False
    if cobra[0][0] == tela.get_width():
        pygame.quit()
        Game= False
    if cobra[0][0] == tela.get_height():
        pygame.quit()
        Game= False
        
    tela.fill((0,0,0))
    tela.blit(icon,(0,0))
    tela.blit(comida, lugar_comida)
    for posicao in cobra:
        tela.blit(cobrinha,posicao)
    pygame.display.update()
print('Fim')
###Baseado em alguma referencia de videos de youtube e codigos da net        