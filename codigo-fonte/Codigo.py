'''
Caçada ao Uirapuru - Jogo para o SMAUG - FATEC 1º semestre de 2020, Jogos de Digitais
Programador: Murillo Fagundes
Artista: Rafael Oliveira
'''

import pygame
pygame.init()

# Variáveis e definições da tela
Weith = 800
Hight = 640
Metade_Weith = Weith / 2
Metade_Hight = Hight / 2

# Cores
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Definições da Tela
tela = pygame.display.set_mode((Weith, Hight), 0, 32)
pygame.display.set_caption('CAÇADA AO UIRAPURU')
relogio = pygame.time.Clock()
fps = 10

# Load de Imagens
character = pygame.image.load('player3.png').convert_alpha()
vermelho = pygame.image.load('planta.png').convert_alpha()
azul = pygame.image.load('guarana.png').convert_alpha()
pedra = pygame.image.load('mao.png').convert_alpha()
verde = pygame.image.load('plataforma2.png').convert_alpha()
verde2 = pygame.image.load('plataforma1.png').convert_alpha()
chao1 = pygame.image.load('chao1.png').convert_alpha()
chao2 = pygame.image.load('chao2.png').convert_alpha()
madeira1 = pygame.image.load('madeira1.png').convert_alpha()
madeira2 = pygame.image.load('madeira2.png').convert_alpha()
madeira3 = pygame.image.load('madeira3.png').convert_alpha()
bg = pygame.image.load('bg4.jpg').convert_alpha()
menu = pygame.image.load('Capa.jpg').convert_alpha()
tutorial = pygame.image.load('tutorial.jpeg').convert_alpha()
hud = pygame.image.load('hud.jpg').convert_alpha()

# Variáveis e definições dos personagens
tamanhoPersonagem = (96, 96)
originalPersonagem = (128, 128)
tamanhoInimigo = (96, 96)
originalInimigo = (128, 144)

gravidade = 0.4

# Carregamento da música e áudios
pygame.mixer.init()
musica1 = pygame.mixer.music.load('assets/musica.mp3')
pygame.mixer.music.set_volume(0.6)


# Configuração das fonte e letras
pygame.font.init()
fonte = pygame.font.Font('Jungle Fever.ttf', 30)
fonteFim = pygame.font.Font('Jungle Fever.ttf', 90)
pontos = 0


# Variáveis para colisão com as bordas da tela
tamanhoImagem = 7680
tamanhoPlayer = character.get_width()
posicaoTela = 0
movimentacaoTela = 0

# Mapa do jogo (1 e 2 = grama | 3, 4 e 5 = plataforma | 7 = pedra| 8 = guaraná | 9 = inimigo | 6 e A = solo)
game_map = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '8', '9', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '8', '0', '9', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '8', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '3', '3', '5', '4', '4', '0', '0', '0', '0', '0', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '8', '0', '0', '0', '0', '4', '3', '3', '4', '3', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '8', '0', '0', '0', '0', '3', '4', '4', '5'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '7', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '7', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4', '3', '0', '0', '0', '0', '0', '0', '0', '0', '4', '3', '3', '4', '5', '0', '8', '0', '0', '0', '0', '3', '4', '4', '3', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '0', '0', '3', '3', '4', '4', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '8', '0', '0', '0', '0', '0', '4', '4', '3', '4', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '9', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '0', '0', '0', '7', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '7', '0', '0', '0', '0', '0', '0', '0', '0', '0', '7', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '8', '0', '8', '0', '0', '0', '0', '3', '4', '3', '4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4', '3', '4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '8', '0', '0', '0', '3', '4', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '8', '0', '0', '0', '0', '3', '3', '4', '4', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '8', '0', '0', '0', '0', '0', '3', '3', '4', '4', '3', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '7', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '8', '0', '0', '0', '1', '1', '1', '2', '1', '2', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '3', '4', '3', '4', '3', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '8', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '0', '3', '4', '3', '3', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '4', '3', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '8', '0', '0', '0', '0', '4', '3', '4', '4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '8', '0', '0', '0', '0', '1', '2', '1', '6', 'A', 'A', '6', 'A', '6', '7', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '8', '0', '0', '0', '0', '4', '3', '3', '4', '4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '0', '0', '0', '0', '0', '9', '0', '0', '0', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '8', '0', '8', '0', '0', '0', '0', '8', '0', '8', '0', '0', '4', '3', '4', '3', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '1', '2', '1', '6', '6', 'A', 'A', '6', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '8', '0', '0', '0', '4', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '0', '0', '2', '1', '2', '1', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '0', '0', '0', '0', '0', '0', '2', '1', '1', '2', '1', '2', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '9', '0', '0', '8', '0', '0', '0', '0', '8', '8', '8'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '3', '3', '4', '4', '5', '0', '8', '0', '8', '0', '9', '0', '0', '8', '0', '8', '0', '8', '0', '8', '0', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '9', '0', '0', '8', '0', '2', '2', '1', '1', '6', 'A', 'A', 'A', 'A', 'A', '6', 'A', '6', '0', '8', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '3', '4', '3', '4', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '8', '0', '0', '0', '3', '5', '0', '8', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '8', '0', '0', '0', '0', '0', '0', '0', '2', '1', '1', 'A', 'A', '6', 'A', '2', '1', '2', '2', '1', '1', '2', '0', '0', '0', '0', '0', '0', '0', '0', '1', '2', '1', '2', '1', '0', '0', '0', '0', '0', '0', '0', '9', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '0', '0', '0', '0', '0', '0', '0', '0', '2', '1', '1', '1', '1', '6', 'A', '6', '6', 'A', '6', 'A', '1', '2', '1', '2', '1', '1', '2', '1', '0', '0', '0', '0', '0', '0', '0', '9', '0', '8', '8', '8'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '3', '4', '3', '4', '5', '0', '0', '0', '4', '3', '3', '4', '4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', 'A', 'A', 'A', 'A', 'A', '6', '6', 'A', 'A', 'A', 'A', 'A', 'A', '0', '8', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '3', '3', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '2', '1', 'A', 'A', '6', '6', 'A', '6', '6', 'A', '6', 'A', 'A', '6', 'A', '6', '1', '2', '1', '1', '2', '1', '2', '1', '6', '6', 'A', '6', 'A', '1', '2', '1', '2', '1', '1', '0', '0', '0', '0', '0', '0', '0', '9', '0', '0', '0', '0', '0', '0', '0', '0', '1', '2', '1', '1', '2', '1', 'A', '6', '6', '6', 'A', '6', 'A', 'A', '6', 'A', '6', 'A', 'A', '6', 'A', '6', 'A', 'A', '6', 'A', '2', '1', '1', '2', '1', '2', '0', '0', '0', '8', '8', '8'],
            ['1', '2', '1', '2', '1', '1', '2', '1', '2', '1', '1', '2', '1', '2', '1', '1', '2', '1', '2', '1', '1', '2', '1', '2', '1', '1', '2', '1', '2', '1', '1', '2', '1', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '1', '2', '1', '1', 'A', 'A', '6', 'A', '6', 'A', 'A', 'A', '6', 'A', '6', 'A', '6', 'A', '6', 'A', '6', 'A', 'A', '1', '2', '1', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '9', '0', '0', '3', '4', '0', '0', '0', '0', '0', '0', '5', '4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '8', '8', '8', '0', '0', '3', '4', '0', '0', '0', '0', '1', 'A', 'A', '6', '6', 'A', 'A', '6', 'A', 'A', 'A', '6', '6', 'A', 'A', 'A', 'A', 'A', '6', 'A', 'A', '6', 'A', '6', 'A', 'A', 'A', 'A', '6', 'A', 'A', '6', 'A', '6', 'A', 'A', '2', '1', '2', '1', '1', '2', '0', '0', '0', '0', '0', '0', '2', '1', '1', '2', 'A', '6', 'A', '6', '6', 'A', 'A', '6', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', '6', 'A', 'A', 'A', '6', 'A', 'A', 'A', 'A', '6', 'A', 'A', '6', 'A', '6', '1', '1', '2', '1', '2', '1'],
            ['6', '6', 'A', '6', 'A', 'A', '6', 'A', '6', '6', 'A', '6', 'A', '6', 'A', 'A', '6', 'A', '6', 'A', '6', '6', 'A', '6', 'A', 'A', '6', 'A', '6', '6', 'A', '6', 'A', '6', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '6', 'A', '6', 'A', 'A', '6', '6', 'A', '6', 'A', '6', 'A', '6', 'A', 'A', '6', '6', 'A', 'A', 'A', 'A', 'A', '6', 'A', '6', '6', 'A', '6', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', 'A', 'A', 'A', '6', 'A', '6', 'A', 'A', '6', '6', 'A', 'A', '6', '6', 'A', 'A', 'A', '6', 'A', 'A', '6', 'A', 'A', 'A', '6', '6', 'A', 'A', '6', 'A', 'A', '6', 'A', 'A', 'A', '6', 'A', '6', 'A', 'A', '6', '1', '2', '1', '1', '2', '1', '6', 'A', 'A', '6', '6', 'A', 'A', 'A', 'A', '6', '6', 'A', 'A', '6', '6', 'A', 'A', 'A', '6', 'A', '6', '6', 'A', '6', '6', 'A', '6', 'A', '6', '6', '6', 'A', 'A', 'A', '6', '6', 'A', 'A', '6', 'A', '6', 'A'],
            ['A', 'A', '6', 'A', '6', '6', '6', 'A', 'A', 'A', 'A', '6', 'A', '6', 'A', 'A', '6', 'A', '6', 'A', '6', '6', 'A', '6', 'A', 'A', '6', 'A', 'A', 'A', '6', '6', 'A', '6', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '6', 'A', '6', 'A', 'A', '6', '6', 'A', '6', 'A', '6', '6', 'A', '6', 'A', 'A', 'A', '6', '6', 'A', '6', 'A', '6', '6', 'A', 'A', '6', '6', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '3', '4', '3', '4', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '3', '4', '5', '0', '0', '0', '0', '0', '0', '0', '0', '1', '6', '6', 'A', 'A', 'A', 'A', '6', '6', 'A', 'A', 'A', '6', '6', 'A', 'A', '6', 'A', 'A', 'A', 'A', '6', 'A', '6', '6', 'A', '6', 'A', '6', 'A', '6', '6', 'A', 'A', 'A', 'A', '6', 'A', '6', 'A', 'A', '6', 'A', '6', 'A', 'A', '6', 'A', '6', 'A', '6', '6', 'A', '6', 'A', '6', '6', 'A', 'A', '6', '6', 'A', '6', 'A', 'A', 'A', '6', 'A', '6', 'A', '6', '6', 'A', '6', '6', 'A', '6', 'A', '6', 'A', 'A', '6', 'A', 'A', 'A', 'A', '6', 'A', '6', 'A']]




def load_image(tileset, x, y, tamanhoOriginal, tamanho):
    global tamanhoPersonagem
    img_orig = tileset.subsurface((x, y), tamanhoOriginal)
    # .subsurface((posiçãonotileemx, posiçãonotileemy), (largura, altura))
    img_scaled = pygame.transform.scale(img_orig, tamanho)
    # transforma/escalona
    return img_scaled
    # retorna objeto


class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        direita1 = load_image(character, 0, 0, originalPersonagem, tamanhoPersonagem)
        direita2 = load_image(character, 128, 0, originalPersonagem, tamanhoPersonagem)
        direita3 = load_image(character, 256, 0, originalPersonagem, tamanhoPersonagem)
        direita4 = load_image(character, 384, 0, originalPersonagem, tamanhoPersonagem)
        direita5 = load_image(character, 512, 0, originalPersonagem, tamanhoPersonagem)

        esquerda1 = load_image(character, 0, 128, originalPersonagem, tamanhoPersonagem)
        esquerda2 = load_image(character, 128, 128, originalPersonagem, tamanhoPersonagem)
        esquerda3 = load_image(character, 256, 128, originalPersonagem, tamanhoPersonagem)
        esquerda4 = load_image(character, 384, 128, originalPersonagem, tamanhoPersonagem)
        esquerda5 = load_image(character, 512, 128, originalPersonagem, tamanhoPersonagem)

        paradordireita = load_image(character, 0, 256, originalPersonagem, tamanhoPersonagem)
        paradoesquerda = load_image(character, 128, 256, originalPersonagem, tamanhoPersonagem)

        pulodireita = load_image(character, 256, 256, originalPersonagem, tamanhoPersonagem)
        puloesquerda = load_image(character, 384, 256, originalPersonagem, tamanhoPersonagem)

        self.andando_direita = [direita1, direita2, direita3, direita4, direita5]
        self.andando_esquerda = [esquerda1, esquerda2, esquerda3, esquerda4, esquerda5]
        self.parado_direita = [paradordireita]
        self.parado_esquerda = [paradoesquerda]
        self.pulo_direita = [pulodireita]
        self.pulo_esquerda = [puloesquerda]
        self.movimento = [paradordireita]

        self.image_indice = 0

        self.image = paradordireita
        self.rect = pygame.Rect((10, 450), (74, 80))
        self.intencao_posicao = list(self.rect.center)

        self.image_direcao = True
        self.velocidadeX = 0
        self.velocidadeY = 0
        self.gravidadeY = gravidade
        self.pulo = False
        self.noChao = False

    def update(self):
        self.image = self.movimento[self.image_indice]
        self.image_indice += 1
        if self.image_indice >= len(self.movimento):
            self.image_indice = 0

        self.mask = pygame.mask.from_surface(self.image)

        self.velocidadeY += self.gravidadeY
        self.intencao_posicao[0] += self.velocidadeX
        self.intencao_posicao[1] += self.velocidadeY

    def colisao_paredes(self):
        global Weith, Height, tamanhoPlayer, tamanhoImagem, tamanhoPersonagem
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= tamanhoImagem - tamanhoPersonagem[0]:
            self.rect.x = tamanhoImagem - tamanhoPersonagem[0]
        elif self.rect.y <= 0:
            self.rect.y = 0

    def pular(self):
        self.velocidadeY = -8
        self.intencao_posicao[1] += self.velocidadeY

    def autoriza(self):
        self.rect.center = self.intencao_posicao

    def rejeita(self):
        self.intencao_posicao = list(self.rect.center)
        self.velocidadeY = 0

    def colisao_mask(self, sprite1, sprite2):
        return pygame.sprite.collide_mask(sprite1, sprite2)

    def colisao_chao(self, grupo):
        temp = self.rect.center
        self.rect.center = self.intencao_posicao
        if not pygame.sprite.spritecollide(self, grupo, False):
            self.autoriza()
        else:
            self.pulo = True
            self.rect.center = temp
            self.rejeita()

    def processar_eventos(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.velocidadeX = 30
                self.image_direcao = True
                self.movimento = self.andando_direita
            elif event.key == pygame.K_LEFT:
                self.velocidadeX = - 30
                self.image_direcao = False
                self.movimento = self.andando_esquerda
            if event.key == pygame.K_UP:
                if self.pulo == True:
                    self.pulo = False
                    self.pular()
                    self.image_indice = 0
                    if self.image_direcao == True:
                        self.movimento = self.pulo_direita
                    else:
                        self.movimento = self.pulo_esquerda
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                self.velocidadeX = 0
            self.image_indice = 0
            if self.image_direcao == True:
                self.movimento = self.parado_direita
            else:
                self.movimento = self.parado_esquerda


class Plataforma(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem):
        pygame.sprite.Sprite.__init__(self, grupo_chao)
        self.image = imagem
        self.rect = pygame.Rect((x, y), (32, 32))


class Pedra(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, grupo_pedras)
        self.image = pedra
        self.rect = pygame.Rect((x, y), (32, 32))
        self.mask = pygame.mask.from_surface(self.image)
        self.velocidadeY = 0

    def update_cair(self, pedras):
        if raoni.rect.centerx >= pedras.rect.centerx and raoni.rect.centery > pedras.rect.centery:
            pedras.velocidadeY = 22
        pedras.rect.y += pedras.velocidadeY

    def colisoes(self, pedras):
        if pygame.sprite.spritecollide(self, grupo_chao, False):
            self.kill()

        if pygame.sprite.collide_mask(pedras, raoni):
            morreu('Esmagado!', 170)


class Guarana(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, grupo_guarana)
        self.image = azul
        self.rect = pygame.Rect((x, y), (32, 32))
        self.mask = pygame.mask.from_surface(self.image)


class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, grupo_inimigos)
        parado = load_image(vermelho, 0, 0, originalInimigo, tamanhoInimigo)
        mordendo1 = load_image(vermelho, 128, 0, originalInimigo, tamanhoInimigo)

        self.movimento = [parado]
        self.mordendo = [mordendo1, parado]
        self.image = parado

        self.rect = pygame.Rect((x, y), tamanhoInimigo)
        self.image_indice = 0

        self.mask = pygame.mask.from_surface(self.image)

    def update_frame(self):
        self.image = self.mordendo[self.image_indice]
        self.image_indice += 1
        if self.image_indice >= len(self.mordendo):
            self.image_indice = 0

    def ataque(self):
        morreu('Foi pego!', 220)


class Camera():
    def __init__(self, position, tamanho):
        self.window = pygame.Rect(position, tamanho)
        self.position = position
        self.offset_x = 0
        self.offset_y = 0
        # self.clean_image = pygame.Surface(self.window.size)
        bg_escalonado = pygame.transform.scale(bg, (Weith, Hight))
        self.clean_image = bg_escalonado
        # self.clean_image.fill(bg)
        self.draw_area = pygame.Surface(self.window.size)

    def in_viewport(self, r):
        return self.window.colliderect(r)

    def move(self, pos):
        self.window.center = pos
        self.offset_x = self.window.x
        # self.offset_y = self.window.y

    def start_drawing(self):
        self.draw_area.blit(self.clean_image, (0, 0))

    def paint(self, tela):
        tela.blit(self.draw_area, self.position)
        # pygame.draw.rect(tela, (255, 0, 0), (self.position, self.window.size), 3)

    def draw_group(self, group):
        for s in group:
            if self.in_viewport(s.rect):
                self.draw_area.blit(s.image, (s.rect.x-self.offset_x, s.rect.y-self.offset_y))


cam = Camera((0, 0), (Weith, Hight))

raoni = Personagem()
grupo_raoni = pygame.sprite.Group(raoni)
grupo_chao = pygame.sprite.Group()
grupo_pedras = pygame.sprite.Group()
grupo_folhas = pygame.sprite.Group()
grupo_inimigos = pygame.sprite.Group()
grupo_guarana = pygame.sprite.Group()
posicoesGuarana = []


print('Carregando o Jogo...')
run = True

# Projeta o Mapa
y = 0
for linha in game_map:
    x = 0
    for elemento in linha:
        if elemento == '1':
            chaoTile = Plataforma(x * 32, y * 32, verde)
            grupo_chao.add(chaoTile)
        if elemento == '2':
            chaoTile = Plataforma(x * 32, y * 32, verde2)
            grupo_chao.add(chaoTile)

        if elemento == '3':
            plataforma = Plataforma(x * 32, y * 32, madeira1)
            grupo_chao.add(plataforma)
        if elemento == '4':
            plataforma = Plataforma(x * 32, y * 32, madeira2)
            grupo_chao.add(plataforma)
        if elemento == '5':
            plataforma = Plataforma(x * 32, y * 32, madeira3)
            grupo_chao.add(plataforma)

        if elemento == '6':
            plataforma = Plataforma(x * 32, y * 32, chao1)
            grupo_chao.add(plataforma)
        if elemento == 'A':
            plataforma = Plataforma(x * 32, y * 32, chao2)
            grupo_chao.add(plataforma)

        if elemento == '7':
            pedraTile = Pedra(x * 32, y * 32)
            grupo_pedras.add(pedraTile)

        if elemento == '8':
            guaranaTile = Guarana(x * 32, y * 32)
            grupo_guarana.add(guaranaTile)
            posicao = [y, x]
            posicoesGuarana.append(posicao)

        if elemento == '9':
            inimigoTile = Inimigo(x * 32, y * 32)
            grupo_inimigos.add(inimigoTile)
        x += 1
    y += 1


def menuTutorial():
    global run, tutorial
    tutorial_escalonado = pygame.transform.scale(tutorial, (Weith, Hight))

    while run:

        tela.blit(tutorial_escalonado, (0, 0))

        textoVoltar = fonte.render("pressione V para VOLTAR ao Menu", 1, yellow)
        tela.blit(textoVoltar, (130, Hight - 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v:
                    menuJogo()

        relogio.tick(fps)
        pygame.display.update()

def menuJogo():
    global run, red, menu
    menu_escalonado = pygame.transform.scale(menu, (Weith, Hight))

    while run:

        tela.blit(menu_escalonado, (0, 0))

        textoMenu = fonteFim.render("MENU", 1, green)
        tela.blit(textoMenu, (260, 100))

        textoPlay = fonte.render("pressione SPACE para jogar", 1, yellow)
        tela.blit(textoPlay, (175, Hight - 100))

        textoTutorial = fonte.render("pressione T para ver o TUTORIAL", 1, yellow)
        tela.blit(textoTutorial, (130, Hight - 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jogo()
                elif event.key == pygame.K_t:
                    menuTutorial()

        relogio.tick(fps)
        pygame.display.update()


def jogo():
    global run, pontos, Hight

    hud_escalonada = pygame.transform.scale(hud, (64, 64))

    pygame.mixer.music.play(-1)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            raoni.processar_eventos(event)

        # A camera desenha os grupos
        cam.start_drawing()
        cam.draw_group(grupo_inimigos)
        cam.draw_group(grupo_chao)
        cam.draw_group(grupo_pedras)
        cam.draw_group(grupo_folhas)
        cam.draw_group(grupo_raoni)
        cam.draw_group(grupo_guarana)
        cam.paint(tela)

        # Desenha
        cam.move(raoni.rect.center)

        # Atualização do personagem
        raoni.update()

        # Colisão com o chão
        raoni.colisao_chao(grupo_chao)

        # Colisão com as paredes
        raoni.colisao_paredes()

        # Colisão com guaraná
        for guarana in grupo_guarana:
            if pygame.sprite.collide_mask(guarana, raoni):
                grupo_guarana.remove(guarana)
                pontos += 5
                x = guarana.rect.x // 32
                y = guarana.rect.y // 32
                game_map[y][x] = '0'
                guarana.kill()

        # Colisão com o inimigo
        for inimigo in grupo_inimigos:
            if pygame.sprite.collide_mask(inimigo, raoni):
                inimigo.ataque()
            inimigo.update_frame()


        # Mecânica das pedras
        for pedras in grupo_pedras:
            pedras.update_cair(pedras)
            pedras.colisoes(pedras)

        # Mecânica da queda
        if raoni.rect.y > Hight:
            morreu('Caiu!', 280)


        # Imagem da HUD
        tela.blit(hud_escalonada, (10, 10))
        # Escreve a pontuação
        if pontos < 100:
            cor = blue
        elif pontos >= 100 and pontos < 200:
            cor = yellow
        else:
            cor = green
        pontuacao = fonte.render(f"Pontos: ", 1, cor)
        tela.blit(pontuacao, (74, 10))
        pontuacao2 = fonte.render(f'{pontos}', 1, cor)
        tela.blit(pontuacao2, (204, 10))


        pygame.display.update()
        relogio.tick(fps)


def morreu(mensagem, x):
    global run

    pygame.mixer.music.stop()
    tela.fill(black)

    morto = fonteFim.render(mensagem, 1, red)
    tela.blit(morto, (x, Metade_Hight-30))

    run = False

menuJogo()


# Finaliação do programa
pygame.time.wait(2000)
print('Obrigado por Jogar!!!')
