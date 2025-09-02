import pygame
import random
#inicializar
pygame.init()
pygame.display.set_caption("Snake Python")

#criando tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()

#cores

preta = (0, 0, 0,)
branca = (255, 255, 255)
vermelha =(255, 0 , 0 ) 
verde = (0, 255, 0)

# parametros cobrinha

tamanho_cobrinha = 10
velocidade_cobrinha = 15


def rodar_jogo():
    fim_jogo = False

    while not fim_jogo:
        tela.fill(preta)
        

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True

rodar_jogo()
