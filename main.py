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

tamanho_quadrado = 20
velocidade_cobra = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0)* 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0)* 20.0
    return comida_x, comida_y


def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0 

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerarcomida()

    while not fim_jogo:
        tela.fill(preta)
        

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True

rodar_jogo()
