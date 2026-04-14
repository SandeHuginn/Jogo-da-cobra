import pygame
import random

# Inicializa o pygame
pygame.init()

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)

# Tamanho da tela
largura = 600
altura = 400

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

clock = pygame.time.Clock()

tamanho_bloco = 10
velocidade = 15

font_style = pygame.font.SysFont(None, 30)


def pontuacao(score):
    texto = font_style.render(f"Pontos: {score}", True, branco)
    tela.blit(texto, [0, 0])


def desenhar_cobra(tamanho, lista_cobra):
    for x in lista_cobra:
        pygame.draw.rect(tela, verde, [x[0], x[1], tamanho, tamanho])


def jogo():
    fim_jogo = False
    game_over = False

    x = largura / 2
    y = altura / 2

    x_mudanca = 0
    y_mudanca = 0

    cobra_lista = []
    comprimento = 1

    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0

    while not fim_jogo:

        while game_over:
            tela.fill(preto)
            msg = font_style.render("Você perdeu! C = jogar novamente | Q = sair", True, vermelho)
            tela.blit(msg, [50, altura / 2])
            pontuacao(comprimento - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_jogo = True
                        game_over = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudanca = -tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_mudanca = tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y_mudanca = -tamanho_bloco
                    x_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y_mudanca = tamanho_bloco
                    x_mudanca = 0

        # Verifica colisão com a parede
        if x >= largura or x < 0 or y >= altura or y < 0:
            game_over = True

        x += x_mudanca
        y += y_mudanca
        tela.fill(preto)

        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        cabeca = []
        cabeca.append(x)
        cabeca.append(y)
        cobra_lista.append(cabeca)

        if len(cobra_lista) > comprimento:
            del cobra_lista[0]

        # Colisão com o próprio corpo
        for bloco in cobra_lista[:-1]:
            if bloco == cabeca:
                game_over = True

        desenhar_cobra(tamanho_bloco, cobra_lista)
        pontuacao(comprimento - 1)

        pygame.display.update()

        # Comer comida
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0
            comprimento += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()


jogo()