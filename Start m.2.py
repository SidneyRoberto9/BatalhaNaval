import pygame
import sys
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

#====================Variaveis====================#
#Telas
tela_inicial = True
historia = True
escolha_p1 = True
escolha_p2 = True
jogo = True
turno1 = True
turno2 = True
final = True


#Matrizes do jogo e resolução da tela
lado_celula = 50
largura, altura = (lado_celula*26,lado_celula*14)
campo_p1 = [[False for i in range(14)] for j in range(26)]
campo_p2 = [[False for i in range(14)] for j in range(26)]
check_1  = [[False for i in range(14)]for j in range(26)]
check_2  = [[False for i in range(14)]for j in range(26)]
barco_quebrado_p1 = [[False for i in range(10)] for j in range(10)]
barco_quebrado_p2 = [[False for i in range(10)] for j in range(10)]

#Variaveis Globais
relogio = pygame.time.Clock() #Taxa de atualização do jogo/FPS
fps = 60
navios_quebrados_p1 = 0
navios_quebrados_p2 = 0
vitoria = 2
contador = 0

#posiconamento dos barcos
contador_de_barcos_1 = 0
contador_de_barcos_2 = 0
contador_de_barcos_3 = 0
contador_de_barcos_4 = 0
contador_de_barcos_total_p1 = 0
contador_de_barcos_total_p2 = 0

m_press = 0
m_press2 = 0
m_press3 = 0
m_press4 = 0

click1 = 0
click2 = 0
click3 = 0

modo_vertical1 = False
modo_vertical2 = False
modo_vertical3 = False

#=================Tabela de Cores===============#
branco = (255, 255, 255)
preto = (0, 0, 0)
topsia = (174,174,174)
cinza = (190,190,190)
vermelho = (255,0,0)
#==============================================#

#=====================display==================#
#display inicial
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("MEWNEANA: A BATALHA NAVAL")
pygame.mouse.set_cursor(*pygame.cursors.tri_left) 
icone = pygame.image.load("imagens/navil.png")
pygame.display.set_icon(icone)

#fundos
fundo_inicial = pygame.image.load("imagens/01.png")
fundo_inicial = pygame.transform.scale(fundo_inicial, (largura, altura))

fundo_de_jogo = pygame.image.load("imagens/fundo1.png")
fundo_de_jogo = pygame.transform.scale(fundo_de_jogo, (largura, altura))

fundo_2 = pygame.image.load("imagens/fundo2.png")
fundo_2 = pygame.transform.scale(fundo_2, (largura, altura))

fundo_batalha = pygame.image.load("imagens/fundobatalha.png")
fundo_batalha = pygame.transform.scale(fundo_batalha, (largura, altura))

tela_hist = pygame.image.load("imagens/05.png")
tela_hist = pygame.transform.scale(tela_hist, (largura, altura))

vitoria_1 = pygame.image.load("imagens/v1.png")
vitoria_1 = pygame.transform.scale(vitoria_1,(largura, altura))

vitoria_2 = pygame.image.load("imagens/v2.png")
vitoria_2 = pygame.transform.scale(vitoria_2,(largura, altura))

error =  pygame.image.load("imagens/X.png")
error = pygame.transform.scale(error,(lado_celula,lado_celula)) 

buraco = pygame.image.load("imagens/04.png")
buraco = pygame.transform.scale(buraco,(lado_celula,lado_celula)) 

#botoes
fonte = pygame.font.Font('Wood Xmas.otf', 60)

botao_largura = 200
botao_altura = 50

botao_x1 = lado_celula*6
botao_y1 = lado_celula*8

botao_x2 = lado_celula*6
botao_y2 = (lado_celula*10) + 20

botao_x3 = lado_celula*2
botao_y3 = lado_celula*12

botao_x4 = lado_celula*2
botao_y4 = lado_celula*12

botao_x5 = lado_celula*6
botao_y5 = (lado_celula*9) + 10

botao_x6 = lado_celula*19
botao_y6 = lado_celula*12

#barcos
barco_x1 = lado_celula * 20
barco_y1 = lado_celula * 2

barco_x2 = lado_celula * 20
barco_y2 = lado_celula * 4

barco_x3 = lado_celula * 20
barco_y3 = lado_celula * 6

barco_x4 = lado_celula * 20
barco_y4 = lado_celula * 8

#Barcos horizontais
#p1
barco1_p1 = pygame.image.load("imagens/Meawneanos/Patrulheiros submersos.png")
barco1_p1 = pygame.transform.scale(barco1_p1,(lado_celula*4,lado_celula))

barco2_p1 = pygame.image.load("imagens/Meawneanos/Naves escudeiras.png")
barco2_p1 = pygame.transform.scale(barco2_p1,(lado_celula*3,lado_celula))

barco3_p1 = pygame.image.load("imagens/Meawneanos/Naves atacantes.png")
barco3_p1 = pygame.transform.scale(barco3_p1,(lado_celula*2,lado_celula))

barco4_p1 = pygame.image.load("imagens/Meawneanos/Naves habitaveis.png")
barco4_p1 = pygame.transform.scale(barco4_p1,(lado_celula,lado_celula))

#p2
barco1_p2 = pygame.image.load("imagens/Akarianos/Patrulheiros submersos akarianos.png")
barco1_p2 = pygame.transform.scale(barco1_p2,(lado_celula*4,lado_celula))

barco2_p2 = pygame.image.load("imagens/Akarianos/Naves escudeiras akarianos.png")
barco2_p2 = pygame.transform.scale(barco2_p2,(lado_celula*3,lado_celula))

barco3_p2 = pygame.image.load("imagens/Akarianos/Naves atacantes akarianos.png")
barco3_p2 = pygame.transform.scale(barco3_p2,(lado_celula*2,lado_celula))

barco4_p2 = pygame.image.load("imagens/Akarianos/Naves habitaveis Akarianos.png")
barco4_p2 = pygame.transform.scale(barco4_p2,(lado_celula,lado_celula))

#Barcos verticais
#p1
barco1_p1v = pygame.image.load("imagens/Meawneanos/Patrulheiros submersos vertical.png")
barco1_p1v = pygame.transform.scale(barco1_p1v,(lado_celula,lado_celula*4))

barco2_p1v = pygame.image.load("imagens/Meawneanos/Naves escudeiras vertical.png")
barco2_p1v = pygame.transform.scale(barco2_p1v,(lado_celula,lado_celula*3))

barco3_p1v = pygame.image.load("imagens/Meawneanos/Naves atacantes vertical.png")
barco3_p1v = pygame.transform.scale(barco3_p1v,(lado_celula,lado_celula*2))

barco4_p1v = pygame.image.load("imagens/Meawneanos/Naves habitaveis vertical.png")
barco4_p1v = pygame.transform.scale(barco4_p1v,(lado_celula,lado_celula))

#p2
barco1_p2v = pygame.image.load("imagens/Akarianos/Patrulheiros submersos akarianos vertical.png")
barco1_p2v = pygame.transform.scale(barco1_p2v,(lado_celula,lado_celula*4))

barco2_p2v = pygame.image.load("imagens/Akarianos/Naves escudeiras akarianos vertical.png")
barco2_p2v = pygame.transform.scale(barco2_p2v,(lado_celula,lado_celula*3))

barco3_p2v = pygame.image.load("imagens/Akarianos/Naves atacantes akarianos vertical.png")
barco3_p2v = pygame.transform.scale(barco3_p2v,(lado_celula,lado_celula*2))

barco4_p2v = pygame.image.load("imagens/Akarianos/Naves habitaveis Akarianos vertical.png")
barco4_p2v = pygame.transform.scale(barco4_p2v,(lado_celula,lado_celula))


navio_p1 = ["navio1","navio2","navio3","navio4","navio5","navio6","navio7","navio8","navio9","navio10"]
navio_p2 = ["navio1","navio2","navio3","navio4","navio5","navio6","navio7","navio8","navio9","navio10"]

#atualizando tudo da tela
tela.blit(fundo_inicial, (0, 0))
pygame.display.update()

#funçoes
def verifica(pos_x, pos_y,lado = lado_celula):
    pos_x = (pos_x//lado) * lado
    pos_y = (pos_y//lado) * lado
    
    tupla = pos_x,pos_y
    return tupla

def botao(botao_x, botao_y, Frase, blarg = botao_largura, balt = botao_altura,fonte = fonte):
    pygame.draw.rect(tela, topsia, (botao_x - 2, botao_y - 2, blarg + 4, balt + 4), 1)
    pygame.draw.rect(tela, branco, (botao_x, botao_y, blarg, balt), 0)
    texto = fonte.render(Frase, 1, (0, 0, 0))
    tela.blit(texto, (botao_x + (blarg / 2 - texto.get_width() / 2), botao_y + (balt / 2 - texto.get_height() / 2)))

def sair():
    pygame.quit()
    sys.exit()

def fechar(evento):
    if evento.type == pygame.QUIT:
        sair()

def atualizar(fps):
    relogio.tick(fps)
    pygame.display.update()

def campo(ponto_inicial_x = 1, ponto_inicial_y = 11, ponto_final_x = 1, ponto_final_y = 11, cor = topsia, cheio = 1):
    for i in range(ponto_inicial_x, ponto_inicial_y):
        for j in range(ponto_final_x, ponto_final_y):
            pygame.draw.rect(tela, branco, (lado_celula * i, lado_celula * j, lado_celula, lado_celula), 0)
            pygame.draw.rect(tela, cor, (lado_celula * i, lado_celula * j, lado_celula, lado_celula), cheio)

#==============================================================================#
fundo = pygame.mixer.Sound("audio/audio_fundo.ogg")
fundo.play(1000)
while tela_inicial:
    botao(botao_x1, botao_y1, " start ")
    botao(botao_x2, botao_y2, " exit ")
    botao(botao_x5, botao_y5, " historia ")
    mx, my = pygame.mouse.get_pos()
    for evento in pygame.event.get():
        fechar(evento)

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if (botao_x1 + botao_largura > mx > botao_x1) and (botao_y1 + botao_altura > my > botao_y1):
                tela_inicial = False 
                historia = False

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if (botao_x5 + botao_largura > mx > botao_x5) and (botao_y5 + botao_altura > my > botao_y5):
                tela_inicial = False

        if (evento.type == pygame.MOUSEBUTTONDOWN) and (evento.button == 1):
            if (botao_x2 + botao_largura > mx > botao_x2) and (botao_y2 + botao_altura > my > botao_y2):
                    sair()

    atualizar(fps)

tela.blit(tela_hist, (0,0))
while historia:
    botao(botao_x6, botao_y6, " inciar jogo ")
    mx, my = pygame.mouse.get_pos()
    for evento in pygame.event.get():
        fechar(evento)

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if botao_largura + botao_x6 > mx > botao_x6 and botao_altura + botao_y6 > my > botao_y6:
                historia = False

    atualizar(fps)


tela.blit(fundo_de_jogo, (0, 0))
campo()
pygame.draw.rect(tela, branco, (lado_celula * 20, lado_celula * 2, lado_celula*4, lado_celula*8), 0)
pygame.draw.rect(tela, topsia, (lado_celula * 20, lado_celula * 2, lado_celula*4, lado_celula*8), 1)

while escolha_p1:
    botao(botao_x3, botao_y3, " proximo ")
    tela.blit(barco1_p1,(barco_x1, barco_y1))
    tela.blit(barco2_p1,(barco_x2, barco_y2))
    tela.blit(barco3_p1,(barco_x3, barco_y3))
    tela.blit(barco4_p1,(barco_x4, barco_y4))
    #===========================================================#
    if contador_de_barcos_1 == 1:
        pygame.draw.rect(tela, branco, (lado_celula*20, lado_celula * 2, lado_celula*4, lado_celula), 0)

    if contador_de_barcos_2 == 2:
        pygame.draw.rect(tela, branco, (lado_celula*20, lado_celula * 4, lado_celula*3, lado_celula), 0)

    if contador_de_barcos_3 == 3:
        pygame.draw.rect(tela, branco, (lado_celula*20, lado_celula * 6, lado_celula*2, lado_celula), 0)

    if contador_de_barcos_4 == 4:
        pygame.draw.rect(tela, branco, (lado_celula*20, lado_celula * 8, lado_celula, lado_celula), 0)

    if contador_de_barcos_total_p1 == 10:
        pygame.draw.rect(tela, topsia, (lado_celula * 20, lado_celula * 2, lado_celula*4, lado_celula*8), 1) 
        
    for evento in pygame.event.get():
        mx, my = pygame.mouse.get_pos()
        fechar(evento)

        #barco 1 =============================================================================================#
        if contador_de_barcos_1 < 1:
            if m_press == 1:
                mx1 , my1 = pygame.mouse.get_pos()
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_a:
                    modo_vertical1 =  True
                    click1 += 1
                    if click1 == 2:
                        modo_vertical1 = False
                        click1 = 0
                
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    eixo_y = (mx1//50) - 1
                    eixo_x = (my1//50) - 1
                    if modo_vertical1 == False:
                        if lado_celula*8 > mx > lado_celula and lado_celula *11 > my > lado_celula:
                            if not check_1[eixo_x][eixo_y] and not check_1[eixo_x][eixo_y+3]:
                                campo_p1[eixo_x][eixo_y] = navio_p1.pop()
                                campo_p1[eixo_x][eixo_y+1] = campo_p1[eixo_x][eixo_y]
                                campo_p1[eixo_x][eixo_y+2] = campo_p1[eixo_x][eixo_y]
                                campo_p1[eixo_x][eixo_y+3] = campo_p1[eixo_x][eixo_y]
                                check_1[eixo_x][eixo_y] = True
                                check_1[eixo_x][eixo_y+1] = True
                                check_1[eixo_x][eixo_y+2] = True
                                check_1[eixo_x][eixo_y+3] = True
                                casa = verifica(mx1, my1)
                                tela.blit(barco1_p1,(casa[0],casa[1]))
                                m_press = 0
                                contador_de_barcos_1 += 1 
                                contador_de_barcos_total_p1 += 1

                    elif modo_vertical1 == True:
                        if lado_celula*11 > mx > lado_celula and lado_celula *8 > my > lado_celula:
                            if not check_1[eixo_x][eixo_y] and not check_1[eixo_x+3][eixo_y]:
                                campo_p1[eixo_x][eixo_y] = navio_p1.pop()
                                campo_p1[eixo_x+1][eixo_y] = campo_p1[eixo_x][eixo_y]
                                campo_p1[eixo_x+2][eixo_y] = campo_p1[eixo_x][eixo_y]
                                campo_p1[eixo_x+3][eixo_y] = campo_p1[eixo_x][eixo_y]
                                check_1[eixo_x][eixo_y] = True
                                check_1[eixo_x+1][eixo_y] = True
                                check_1[eixo_x+2][eixo_y] = True
                                check_1[eixo_x+3][eixo_y] = True
                                casa = verifica(mx1, my1)
                                tela.blit(barco1_p1v,(casa[0],casa[1]))
                                m_press = 0
                                contador_de_barcos_1 += 1 
                                contador_de_barcos_total_p1 += 1
                                click1 = 0


            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if barco_x1 + (lado_celula*4) > mx > barco_x1 and barco_y1 + lado_celula > my > barco_y1:
                    m_press += 1
                    if m_press == 2:
                        m_press = 0    

        #barco 2 =============================================================================================#

        if contador_de_barcos_2 < 2:
            if m_press2 == 1:
                mx1 , my1 = pygame.mouse.get_pos()
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_a:
                    modo_vertical2 =  True
                    click2 += 1
                    if click2 == 2:
                        modo_vertical2 = False
                        click2 = 0
                
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    eixo_y = (mx1//50) - 1
                    eixo_x = (my1//50) - 1
                    if modo_vertical2 == False:
                        if lado_celula*9 > mx > lado_celula and lado_celula*11 > my > lado_celula:
                            if not check_1[eixo_x][eixo_y] and not check_1[eixo_x][eixo_y+2]:
                                campo_p1[eixo_x][eixo_y] = navio_p1.pop()
                                campo_p1[eixo_x][eixo_y+1] = campo_p1[eixo_x][eixo_y]
                                campo_p1[eixo_x][eixo_y+2] = campo_p1[eixo_x][eixo_y]
                                check_1[eixo_x][eixo_y] = True
                                check_1[eixo_x][eixo_y+1] = True
                                check_1[eixo_x][eixo_y+2] = True
                                casa = verifica(mx1, my1)
                                tela.blit(barco2_p1,(casa[0],casa[1]))
                                m_press2 = 0
                                contador_de_barcos_2 += 1
                                contador_de_barcos_total_p1 += 1
                                
                    elif modo_vertical2 == True:
                        if lado_celula*11 > mx > lado_celula and lado_celula*9 > my > lado_celula:
                            if not check_1[eixo_x][eixo_y] and not check_1[eixo_x+2][eixo_y]:
                                campo_p1[eixo_x][eixo_y] = navio_p1.pop()
                                campo_p1[eixo_x+1][eixo_y] = campo_p1[eixo_x][eixo_y]
                                campo_p1[eixo_x+2][eixo_y] = campo_p1[eixo_x][eixo_y]
                                check_1[eixo_x][eixo_y] = True
                                check_1[eixo_x+1][eixo_y] = True
                                check_1[eixo_x+2][eixo_y] = True
                                casa = verifica(mx1, my1)
                                tela.blit(barco2_p1v,(casa[0],casa[1]))
                                m_press2 = 0
                                contador_de_barcos_2 += 1
                                contador_de_barcos_total_p1 += 1
                                modo_vertical2 = False
                                click2 = 0
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if barco_x2 + (lado_celula*3) > mx > barco_x2 and barco_y2 + lado_celula > my > barco_y2:
                    m_press2 += 1
                    if m_press2 == 2:
                        m_press2 = 0
        
        #barco 3 =============================================================================================#
        if contador_de_barcos_3 < 3:
            if m_press3 == 1:
                mx1 , my1 = pygame.mouse.get_pos()
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_a:
                    modo_vertical3 =  True
                    click3 += 1
                    if click3 == 2:
                        modo_vertical3 = False
                        click3 = 0
                
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    eixo_y = (mx1//50) - 1
                    eixo_x = (my1//50) - 1
                    if modo_vertical3 == False:
                        if lado_celula*10 > mx > lado_celula and lado_celula*11 > my > lado_celula:
                            if not check_1[eixo_x][eixo_y] and not check_1[eixo_x][eixo_y+1]:
                                campo_p1[eixo_x][eixo_y] = navio_p1.pop()
                                campo_p1[eixo_x][eixo_y+1] = campo_p1[eixo_x][eixo_y]
                                check_1[eixo_x][eixo_y] = True
                                check_1[eixo_x][eixo_y+1] = True
                                casa = verifica(mx1, my1)
                                tela.blit(barco3_p1,(casa[0],casa[1]))
                                m_press3 = 0
                                contador_de_barcos_3 += 1
                                contador_de_barcos_total_p1 += 1

                    elif modo_vertical3 == True:
                        if lado_celula*11 > mx > lado_celula and lado_celula*10 > my > lado_celula:
                            if not check_1[eixo_x][eixo_y] and not check_1[eixo_x+1][eixo_y]:
                                campo_p1[eixo_x][eixo_y] = navio_p1.pop()
                                campo_p1[eixo_x+1][eixo_y] = campo_p1[eixo_x][eixo_y]
                                check_1[eixo_x][eixo_y] = True
                                check_1[eixo_x+1][eixo_y] = True
                                casa = verifica(mx1, my1)
                                tela.blit(barco3_p1v,(casa[0],casa[1]))
                                m_press3 = 0
                                contador_de_barcos_3 += 1
                                contador_de_barcos_total_p1 += 1
                                modo_vertical3 = False
                                click3 = 0

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if barco_x3 + (lado_celula*2) > mx > barco_x3 and barco_y3 + lado_celula > my > barco_y3:
                    m_press3 += 1
                    if m_press3 == 2:
                        m_press3 = 0    

        #barco 4 =============================================================================================#
        if contador_de_barcos_4 < 4:
            if m_press4 == 1:
                mx1 , my1 = pygame.mouse.get_pos()
                
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    eixo_y = (mx1//50) - 1
                    eixo_x = (my1//50) - 1
                    if lado_celula*11 > mx > lado_celula and lado_celula*11 > my > lado_celula:
                        if not check_1[eixo_x][eixo_y]:
                            campo_p1[eixo_x][eixo_y] = navio_p1.pop()
                            check_1[eixo_x][eixo_y] = True
                            casa = verifica(mx1, my1)
                            tela.blit(barco4_p1,(casa[0],casa[1]))
                            m_press4 = 0
                            contador_de_barcos_4 += 1
                            contador_de_barcos_total_p1 += 1

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if barco_x4 + lado_celula > mx > barco_x4 and barco_y4 + lado_celula > my > barco_y4:
                    m_press4 += 1
                    if m_press4 == 2:
                        m_press4 = 0  
        #====================================================================================================#
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: 
            if botao_x3 + botao_largura > mx > botao_x3 and botao_y3 + botao_altura > my > botao_y3:
                escolha_p1 = False
                modo_vertical1 = False
                modo_vertical2 = False
                modo_vertical3 = False
                m_press = 0
                m_press2 = 0
                m_press3 = 0
                m_press4 = 0
                click1 = 0
                click2 = 0
                click3 = 0
                contador_de_barcos_1 = 0
                contador_de_barcos_2 = 0
                contador_de_barcos_3 = 0
                contador_de_barcos_4 = 0
                
    atualizar(fps)

tela.blit(fundo_2, (0,0))
campo()
pygame.draw.rect(tela, branco, (lado_celula * 20, lado_celula * 2, lado_celula*4, lado_celula*8), 0)
pygame.draw.rect(tela, topsia, (lado_celula * 20, lado_celula * 2, lado_celula*4, lado_celula*8), 1)

while escolha_p2:
    botao(botao_x4, botao_y4, " proximo ")
    tela.blit(barco1_p2,(barco_x1, barco_y1))
    tela.blit(barco2_p2,(barco_x2, barco_y2))
    tela.blit(barco3_p2,(barco_x3, barco_y3))
    tela.blit(barco4_p2,(barco_x4, barco_y4))
    #===========================================================#
    if contador_de_barcos_1 == 1:
        pygame.draw.rect(tela, branco, (lado_celula*20, lado_celula * 2, lado_celula*4, lado_celula), 0)

    if contador_de_barcos_2 == 2:
        pygame.draw.rect(tela, branco, (lado_celula*20, lado_celula * 4, lado_celula*3, lado_celula), 0)

    if contador_de_barcos_3 == 3:
        pygame.draw.rect(tela, branco, (lado_celula*20, lado_celula * 6, lado_celula*2, lado_celula), 0)
        
    if contador_de_barcos_4 == 4:
        pygame.draw.rect(tela, branco, (lado_celula*20, lado_celula * 8, lado_celula, lado_celula), 0)
        
    if contador_de_barcos_total_p2 == 10:
        pygame.draw.rect(tela, topsia, (lado_celula * 20, lado_celula * 2, lado_celula*4, lado_celula*8), 1)

    for evento in pygame.event.get():
        mx, my = pygame.mouse.get_pos()
        fechar(evento)

        #barco 1 =============================================================================================#
        if contador_de_barcos_1 < 1:
            if m_press == 1:
                mx1 , my1 = pygame.mouse.get_pos()
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_a:
                    modo_vertical1 =  True
                    click1 += 1
                    if click1 == 2:
                        modo_vertical1 = False
                        click1 = 0

                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    eixo_y = (mx1//50) - 1
                    eixo_x = (my1//50) - 1
                    if modo_vertical1 == False:
                        if lado_celula*8 > mx > lado_celula and lado_celula *11 > my > lado_celula:
                            if not check_2[eixo_x][eixo_y] and not check_2[eixo_x][eixo_y+3]:
                                campo_p2[eixo_x][eixo_y] = navio_p2.pop()
                                campo_p2[eixo_x][eixo_y+1] = campo_p2[eixo_x][eixo_y]
                                campo_p2[eixo_x][eixo_y+2] = campo_p2[eixo_x][eixo_y]
                                campo_p2[eixo_x][eixo_y+3] = campo_p2[eixo_x][eixo_y]
                                check_2[eixo_x][eixo_y] = True
                                check_2[eixo_x][eixo_y+1] = True
                                check_2[eixo_x][eixo_y+2] = True
                                check_2[eixo_x][eixo_y+3] = True
                                casa = verifica(mx1, my1)
                                tela.blit(barco1_p2,(casa[0], casa[1]))
                                m_press = 0
                                contador_de_barcos_1 += 1 
                                contador_de_barcos_total_p2 += 1
                    elif modo_vertical1 == True:
                        if lado_celula*11 > mx > lado_celula and lado_celula *8 > my > lado_celula:
                            if not check_2[eixo_x][eixo_y] and not check_2[eixo_x+3][eixo_y]:
                                campo_p2[eixo_x][eixo_y] = navio_p2.pop()
                                campo_p2[eixo_x+1][eixo_y] = campo_p2[eixo_x][eixo_y]
                                campo_p2[eixo_x+2][eixo_y] = campo_p2[eixo_x][eixo_y]
                                campo_p2[eixo_x+3][eixo_y] = campo_p2[eixo_x][eixo_y]
                                check_2[eixo_x][eixo_y] = True
                                check_2[eixo_x+1][eixo_y] = True
                                check_2[eixo_x+2][eixo_y] = True
                                check_2[eixo_x+3][eixo_y] = True
                                casa = verifica(mx1, my1)
                                tela.blit(barco1_p2v,(casa[0], casa[1]))
                                m_press = 0
                                contador_de_barcos_1 += 1 
                                contador_de_barcos_total_p2 += 1
                                modo_vertical1 = False
                                click1 = 0
                                
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if barco_x1 + (lado_celula*4) > mx > barco_x1 and barco_y1 + lado_celula > my > barco_y1:
                    m_press += 1
                    if m_press == 2:
                        m_press = 0    

        #barco 2 =============================================================================================#
        if contador_de_barcos_2 < 2:
            if m_press2 == 1:
                mx1 , my1 = pygame.mouse.get_pos()
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_a:
                    modo_vertical2 =  True
                    click2 += 1
                    if click2 == 2:
                        modo_vertical2 = False
                        click2 = 0
                
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    eixo_y = (mx1//50) - 1
                    eixo_x = (my1//50) - 1
                    if modo_vertical2 == False:
                        if lado_celula*9 > mx > lado_celula and lado_celula*11 > my > lado_celula:
                            if not check_2[eixo_x][eixo_y] and not check_2[eixo_x][eixo_y+2]:
                                campo_p2[eixo_x][eixo_y] = navio_p2.pop()
                                campo_p2[eixo_x][eixo_y+1] = campo_p2[eixo_x][eixo_y]
                                campo_p2[eixo_x][eixo_y+2] = campo_p2[eixo_x][eixo_y]
                                check_2[eixo_x][eixo_y] = True
                                check_2[eixo_x][eixo_y+1] = True
                                check_2[eixo_x][eixo_y+2] = True
                                casa = verifica(mx1, my1)
                                tela.blit(barco2_p2,(casa[0], casa[1]))
                                m_press2 = 0
                                contador_de_barcos_2 += 1
                                contador_de_barcos_total_p2 += 1
                    elif modo_vertical2 == True:
                        if lado_celula*11 > mx > lado_celula and lado_celula*9 > my > lado_celula:
                            if not check_2[eixo_x][eixo_y] and not check_2[eixo_x+2][eixo_y]:
                                campo_p2[eixo_x][eixo_y] = navio_p2.pop()
                                campo_p2[eixo_x+1][eixo_y] = campo_p2[eixo_x][eixo_y]
                                campo_p2[eixo_x+2][eixo_y] = campo_p2[eixo_x][eixo_y]
                                check_2[eixo_x][eixo_y] = True
                                check_2[eixo_x+1][eixo_y] = True
                                check_2[eixo_x+2][eixo_y] = True
                                casa = verifica(mx1, my1)
                                tela.blit(barco2_p2v,(casa[0], casa[1]))
                                m_press2 = 0
                                contador_de_barcos_2 += 1
                                contador_de_barcos_total_p2 += 1
                                click2 = 0

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if barco_x2 + (lado_celula*3) > mx > barco_x2 and barco_y2 + lado_celula > my > barco_y2:
                    m_press2 += 1
                    if m_press2 == 2:
                        m_press2 = 0
        
        #barco 3 =============================================================================================#
        if contador_de_barcos_3 < 3:
            if m_press3 == 1:
                mx1 , my1 = pygame.mouse.get_pos()
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_a:
                    modo_vertical3 =  True
                    click3 += 1
                    if click3 == 2:
                        modo_vertical3 = False
                        click3 = 0
                
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    eixo_y = (mx1//50) - 1
                    eixo_x = (my1//50) - 1
                    if modo_vertical3 == False:
                        if lado_celula*10 > mx > lado_celula and lado_celula*11 > my > lado_celula:
                            if not check_2[eixo_x][eixo_y] and not check_2[eixo_x][eixo_y+1]:
                                campo_p2[eixo_x][eixo_y] = navio_p2.pop()
                                campo_p2[eixo_x][eixo_y+1] = campo_p2[eixo_x][eixo_y]
                                check_2[eixo_x][eixo_y] = True
                                check_2[eixo_x][eixo_y+1] = True
                                casa = verifica(mx1, my1)
                                tela.blit(barco3_p2,(casa[0], casa[1]))
                                m_press3 = 0
                                contador_de_barcos_3 += 1
                                contador_de_barcos_total_p2 += 1
                    elif modo_vertical3 == True:
                           if lado_celula*11 > mx > lado_celula and lado_celula*10 > my > lado_celula:
                            if not check_2[eixo_x][eixo_y] and not check_2[eixo_x+1][eixo_y]:
                                campo_p2[eixo_x][eixo_y] = navio_p2.pop()
                                campo_p2[eixo_x+1][eixo_y] = campo_p2[eixo_x][eixo_y]
                                check_2[eixo_x][eixo_y] = True
                                check_2[eixo_x+1][eixo_y] = True
                                casa = verifica(mx1, my1)
                                tela.blit(barco3_p2v,(casa[0], casa[1]))
                                m_press3 = 0
                                contador_de_barcos_3 += 1
                                contador_de_barcos_total_p2 += 1
                                modo_vertical3 = False
                                click3 = 0

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if barco_x3 + (lado_celula*2) > mx > barco_x3 and barco_y3 + lado_celula > my > barco_y3:
                    m_press3 += 1
                    if m_press3 == 2:
                        m_press3 = 0    

        #barco 4 =============================================================================================#
        if contador_de_barcos_4 < 4:
            if m_press4 == 1:
                mx1 , my1 = pygame.mouse.get_pos()
                
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    eixo_y = (mx1//50) - 1
                    eixo_x = (my1//50) - 1
                    if lado_celula*11 > mx > lado_celula and lado_celula*11 > my > lado_celula:
                        if not check_2[eixo_x][eixo_y]:    
                            campo_p2[eixo_x][eixo_y] = navio_p2.pop()
                            check_2[eixo_x][eixo_y] = True
                            casa = verifica(mx1, my1)
                            tela.blit(barco4_p2,(casa[0], casa[1]))
                            m_press4 = 0
                            contador_de_barcos_4 += 1
                            contador_de_barcos_total_p2 += 1

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if barco_x4 + lado_celula > mx > barco_x4 and barco_y4 + lado_celula > my > barco_y4:
                    m_press4 += 1
                    if m_press4 == 2:
                        m_press4 = 0  
        #====================================================================================================#
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: 
            if botao_x3 + botao_largura > mx > botao_x3 and botao_y3 + botao_altura > my > botao_y3:
                escolha_p2 = False
                modo_vertical1 = False
                modo_vertical2 = False
                modo_vertical3 = False
                m_press = 0
                m_press2 = 0
                m_press3 = 0
                m_press4 = 0
                click1 = 0
                click2 = 0
                click3 = 0
                contador_de_barcos_1 = 0
                contador_de_barcos_2 = 0
                contador_de_barcos_3 = 0
                contador_de_barcos_4 = 0           
    atualizar(fps)

tela.blit(fundo_batalha,(0,0))
campo()
campo(15,25,1,11)
while jogo:
    fundo.stop()
    for evento in pygame.event.get():
        fechar(evento)
        
        while turno1:
            eixo_x = 0
            eixo_y = 0
            pygame.draw.rect(tela, cinza, (145, 590, 236, 4))
            pygame.draw.rect(tela, vermelho, (895, 590, 216, 4))
            my, mx = pygame.mouse.get_pos()
            for evento in pygame.event.get():
                fechar(evento)

                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    eixo_x = (mx//lado_celula) - 1
                    eixo_y = (my//lado_celula) - 15
                    if eixo_y >= 0 and eixo_y < 10:
                        if check_2[eixo_x][eixo_y] and check_2[eixo_x][eixo_y] != 'agua':
                            if not barco_quebrado_p2[eixo_x][eixo_y]:

                                #verificação para navio de 4 pontos
                                #horizontal
                                if campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y+1] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y+2] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y+3]:
                                    barco_quebrado_p2[eixo_x][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x][eixo_y+1] = True   
                                    barco_quebrado_p2[eixo_x][eixo_y+2] = True  
                                    barco_quebrado_p2[eixo_x][eixo_y+3] = True 
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+16)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+17)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+18)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y-1] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y+1] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y+2]:
                                    barco_quebrado_p2[eixo_x][eixo_y-1] = True  
                                    barco_quebrado_p2[eixo_x][eixo_y] = True   
                                    barco_quebrado_p2[eixo_x][eixo_y+1] = True  
                                    barco_quebrado_p2[eixo_x][eixo_y+2] = True 
                                    tela.blit(error,((eixo_y+14)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+16)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+17)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y-2] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y-1] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y+1]:
                                    barco_quebrado_p2[eixo_x][eixo_y-2] = True  
                                    barco_quebrado_p2[eixo_x][eixo_y-1] = True   
                                    barco_quebrado_p2[eixo_x][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x][eixo_y+1] = True 
                                    tela.blit(error,((eixo_y+13)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+14)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+16)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y-3] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y-2] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y-1]:
                                    barco_quebrado_p2[eixo_x][eixo_y-3] = True  
                                    barco_quebrado_p2[eixo_x][eixo_y-2] = True   
                                    barco_quebrado_p2[eixo_x][eixo_y-1] = True  
                                    barco_quebrado_p2[eixo_x][eixo_y] = True 
                                    tela.blit(error,((eixo_y+12)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+13)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+14)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                #vertical
                                if campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x+1][eixo_y] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x+2][eixo_y] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x+3][eixo_y]:
                                    barco_quebrado_p2[eixo_x][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x+1][eixo_y] = True   
                                    barco_quebrado_p2[eixo_x+2][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x+3][eixo_y] = True 
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+2)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+3)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+4)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x-1][eixo_y] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x+1][eixo_y] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x+2][eixo_y]:
                                    barco_quebrado_p2[eixo_x-1][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x][eixo_y] = True   
                                    barco_quebrado_p2[eixo_x+1][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x+2][eixo_y] = True 
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+2)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+3)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x-2][eixo_y] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x-1][eixo_y] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x+1][eixo_y]:
                                    barco_quebrado_p2[eixo_x-2][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x-1][eixo_y] = True   
                                    barco_quebrado_p2[eixo_x][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x+1][eixo_y] = True 
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x-1)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+2)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x-3][eixo_y] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x-2][eixo_y] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x-1][eixo_y]:
                                    barco_quebrado_p2[eixo_x-3][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x-2][eixo_y] = True   
                                    barco_quebrado_p2[eixo_x-1][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x][eixo_y] = True 
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x-2)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x-1)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                #verificação para navio de 3 pontos
                                #horizontal
                                elif campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y+1] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y+2]:
                                    barco_quebrado_p2[eixo_x][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x][eixo_y+1] = True   
                                    barco_quebrado_p2[eixo_x][eixo_y+2] = True 
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+16)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+17)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y-1] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y+1]:
                                    barco_quebrado_p2[eixo_x][eixo_y-1] = True  
                                    barco_quebrado_p2[eixo_x][eixo_y] = True   
                                    barco_quebrado_p2[eixo_x][eixo_y+1] = True 
                                    tela.blit(error,((eixo_y+14)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+16)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y-2] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y-1]:
                                    barco_quebrado_p2[eixo_x][eixo_y-2] = True  
                                    barco_quebrado_p2[eixo_x][eixo_y-1] = True   
                                    barco_quebrado_p2[eixo_x][eixo_y] = True 
                                    tela.blit(error,((eixo_y+13)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+14)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                #vertical
                                elif campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x+1][eixo_y] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x+2][eixo_y]:
                                    barco_quebrado_p2[eixo_x][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x+1][eixo_y] = True   
                                    barco_quebrado_p2[eixo_x+2][eixo_y] = True 
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+2)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+3)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x-1][eixo_y] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x+1][eixo_y]:
                                    barco_quebrado_p2[eixo_x-1][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x][eixo_y] = True   
                                    barco_quebrado_p2[eixo_x+1][eixo_y] = True 
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+2)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x-2][eixo_y] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x-1][eixo_y]:
                                    barco_quebrado_p2[eixo_x-2][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x-1][eixo_y] = True   
                                    barco_quebrado_p2[eixo_x][eixo_y] = True 
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x-1)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                #verificação para navio de 2 pontos
                                #horizontal
                                elif campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y+1]:
                                    barco_quebrado_p2[eixo_x][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x+1][eixo_y+1] = True
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+16)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y-1]:
                                    barco_quebrado_p2[eixo_x][eixo_y-1] = True  
                                    barco_quebrado_p2[eixo_x][eixo_y] = True
                                    tela.blit(error,((eixo_y+14)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                #vertical
                                elif campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x+1][eixo_y]:
                                    barco_quebrado_p2[eixo_x][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x+1][eixo_y] = True
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+2)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x-1][eixo_y]:
                                    barco_quebrado_p2[eixo_x-1][eixo_y] = True  
                                    barco_quebrado_p2[eixo_x][eixo_y] = True
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x)*lado_celula))
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                #verificação para navio de 1 pontos
                                elif campo_p2[eixo_x][eixo_y] != campo_p2[eixo_x][eixo_y+1] and campo_p2[eixo_x][eixo_y] == campo_p2[eixo_x][eixo_y] and campo_p2[eixo_x][eixo_y] != campo_p2[eixo_x][eixo_y-1]:
                                    barco_quebrado_p2[eixo_x][eixo_y] = True  
                                    tela.blit(error,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p1 +=1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                        elif not check_2[eixo_x][eixo_y] and check_2[eixo_x][eixo_y] != 'agua':
                            check_2[eixo_x][eixo_y] = "agua"
                            tela.blit(buraco,((eixo_y+15)*lado_celula,(eixo_x+1)*lado_celula))
                            pygame.mixer.music.load("audio/water.ogg")
                            pygame.mixer.music.play(1)
                            turno1 = False
                            turno2 = True
                            pygame.display.update()

                        elif check_2[eixo_x][eixo_y] == "agua":
                            print("WATER")

            if navios_quebrados_p1 == 10:
                turno1 = False
                turno2 = False
                jogo = False 
                vitoria = 1

            atualizar(fps) 

        while turno2:
            eixo_x = 0
            eixo_y = 0
            pygame.draw.rect(tela, vermelho, (145, 590, 236, 4))
            pygame.draw.rect(tela, cinza, (895, 590, 216, 4))
            mx, my = pygame.mouse.get_pos()
            for evento in pygame.event.get():
                fechar(evento)

                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    eixo_x = (my//lado_celula) - 1
                    eixo_y = (mx//lado_celula) - 1
                    if eixo_y >= 0 and eixo_y < 10:
                        if check_1[eixo_x][eixo_y] and check_1[eixo_x][eixo_y] != 'agua':
                            if not barco_quebrado_p1[eixo_x][eixo_y]:

                                #verificação para navio de 4 pontos
                                #horizontal
                                if campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y+1] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y+2] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y+3]:
                                    barco_quebrado_p1[eixo_x][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y+1] = True   
                                    barco_quebrado_p1[eixo_x][eixo_y+2] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y+3] = True 
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+2)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+3)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+4)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y-1] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y+1] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y+2]:
                                    barco_quebrado_p1[eixo_x][eixo_y-1] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y] = True   
                                    barco_quebrado_p1[eixo_x][eixo_y+1] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y+2] = True 
                                    tela.blit(error,((eixo_y)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+2)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+3)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y-2] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y-1] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y+1]:
                                    barco_quebrado_p1[eixo_x][eixo_y-2] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y-1] = True   
                                    barco_quebrado_p1[eixo_x][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y+1] = True 
                                    tela.blit(error,((eixo_y-1)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+2)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y-3] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y-2] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y-1]:
                                    barco_quebrado_p1[eixo_x][eixo_y-3] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y-2] = True   
                                    barco_quebrado_p1[eixo_x][eixo_y-1] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y] = True 
                                    tela.blit(error,((eixo_y-2)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y-1)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                #vertical
                                if campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x+1][eixo_y] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x+2][eixo_y] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x+3][eixo_y]:
                                    barco_quebrado_p1[eixo_x][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x+1][eixo_y] = True   
                                    barco_quebrado_p1[eixo_x+2][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x+3][eixo_y] = True 
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+2)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+3)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+4)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x-1][eixo_y] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x+1][eixo_y] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x+2][eixo_y]:
                                    barco_quebrado_p1[eixo_x-1][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y] = True   
                                    barco_quebrado_p1[eixo_x+1][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x+2][eixo_y] = True 
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+2)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+3)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x-2][eixo_y] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x-1][eixo_y] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x+1][eixo_y]:
                                    barco_quebrado_p1[eixo_x-2][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x-1][eixo_y] = True   
                                    barco_quebrado_p1[eixo_x][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x+1][eixo_y] = True 
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x-1)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+2)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x-3][eixo_y] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x-2][eixo_y] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x-1][eixo_y]:
                                    barco_quebrado_p1[eixo_x-3][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x-2][eixo_y] = True   
                                    barco_quebrado_p1[eixo_x-1][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y] = True 
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x-2)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x-1)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                #verificação para navio de 3 pontos
                                #horizontal
                                elif campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y+1] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y+2]:
                                    barco_quebrado_p1[eixo_x][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y+1] = True   
                                    barco_quebrado_p1[eixo_x][eixo_y+2] = True 
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+2)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+3)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y-1] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y+1]:
                                    barco_quebrado_p1[eixo_x][eixo_y-1] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y] = True   
                                    barco_quebrado_p1[eixo_x][eixo_y+1] = True 
                                    tela.blit(error,((eixo_y)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+2)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y-2] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y-1]:
                                    barco_quebrado_p1[eixo_x][eixo_y-2] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y-1] = True   
                                    barco_quebrado_p1[eixo_x][eixo_y] = True 
                                    tela.blit(error,((eixo_y-1)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                #vertical
                                elif campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x+1][eixo_y] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x+2][eixo_y]:
                                    barco_quebrado_p1[eixo_x][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x+1][eixo_y] = True   
                                    barco_quebrado_p1[eixo_x+2][eixo_y] = True 
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+2)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+3)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x-1][eixo_y] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x+1][eixo_y]:
                                    barco_quebrado_p1[eixo_x-1][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y] = True   
                                    barco_quebrado_p1[eixo_x+1][eixo_y] = True 
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+2)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x-2][eixo_y] and campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x-1][eixo_y]:
                                    barco_quebrado_p1[eixo_x-2][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x-1][eixo_y] = True   
                                    barco_quebrado_p1[eixo_x][eixo_y] = True 
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x-1)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()


                                #verificação para navio de 2 pontos
                                #horizontal
                                elif campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y+1]:
                                    barco_quebrado_p1[eixo_x][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y+1] = True
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+2)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x][eixo_y-1]:
                                    barco_quebrado_p1[eixo_x][eixo_y-1] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y] = True
                                    tela.blit(error,((eixo_y)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                #vertical
                                elif campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x+1][eixo_y]:
                                    barco_quebrado_p1[eixo_x][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x+1][eixo_y] = True
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+2)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                elif campo_p1[eixo_x][eixo_y] == campo_p1[eixo_x-1][eixo_y]:
                                    barco_quebrado_p1[eixo_x-1][eixo_y] = True  
                                    barco_quebrado_p1[eixo_x][eixo_y] = True
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x)*lado_celula))
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                #verificação para navio de 1 pontos
                                #horizontal
                                elif campo_p1[eixo_x][eixo_y] != campo_p1[eixo_x][eixo_y+1] and campo_p1[eixo_x][eixo_y] != campo_p1[eixo_x][eixo_y-1]:
                                    barco_quebrado_p1[eixo_x][eixo_y] = True  
                                    tela.blit(error,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                                    navios_quebrados_p2 += 1
                                    pygame.mixer.music.load("audio/explosion.ogg")
                                    pygame.mixer.music.play(1)
                                    pygame.display.update()

                                #errar todos os navios
                        elif not check_1[eixo_x][eixo_y] and check_1[eixo_x][eixo_y] != "agua":
                            check_1[eixo_x][eixo_y] = "agua"
                            tela.blit(buraco,((eixo_y+1)*lado_celula,(eixo_x+1)*lado_celula))
                            pygame.mixer.music.load("audio/water.ogg")
                            pygame.mixer.music.play(1)
                            pygame.display.update()
                            turno1 = True
                            turno2 = False

                        elif check_1[eixo_x][eixo_y] == "agua":
                            print("WATER")

                if navios_quebrados_p2 == 10:
                    turno1 = False
                    turno2 = False
                    jogo = False 
                    vitoria = 2

            atualizar(fps) 
        atualizar(fps) 
while final:
    for evento in pygame.event.get():
        fechar(evento)
        
        if vitoria == 1:
            tela.blit(vitoria_1,(0,0))
            pygame.mixer.music.load("audio/audio.ogg")
            pygame.mixer.music.play(1)

        if vitoria == 2:
            tela.blit(vitoria_2,(0,0))
            pygame.mixer.music.load("audio/audio.ogg")
            pygame.mixer.music.play(1)

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_q:
            sair()  
    atualizar(fps)
sair()
