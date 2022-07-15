import pygame
from estados import estado_inicial, estado1, estado2, estado3, estado4, estado5, estado6, estado7, estado8, estado9, estado10, estado_final


class Estado():

    # constroir os estados da arvore para resolver o problema m_e = missionarios na esquerda, m_d missionarios a direita, c_e = canibais a esquerda,
    # c_d = canibais a direita e l_r lado do rio, estado pai = pai e seus filhos = filhos.

    def __init__(self, m_e, m_d, c_e, c_d, l_r):

        # Inicializamos um estado com as quantidades de missionários e canibais de cada lado e de que lado ta está o barco.

        self.m_e = m_e
        self.c_e = c_e
        self.m_d = m_d
        self.c_d = c_d
        self.l_r = l_r
        self.pai = None
        self.filhos = []

    def __str__(self):

        # para que seja possível representar o estado em forma de string.

        return 'Missionarios: {}\t| Missionarios: {}\nCanibais: {}\t| Canibais: {}'.format(
            self.m_e, self.m_d, self.c_e, self.c_d
        )

    def estado_valido(self):

        # Verifica se o estado é válido, ou seja, se o número de canibais ou missionários não negativo e se o número de missionários não é menor que o de
        # canibais em qualquer uma das margens.

        if ((self.m_e < 0) or (self.m_d < 0)
                or (self.c_e < 0) or (self.c_d < 0)):
            return False

        return ((self.m_e == 0 or self.m_e >= self.c_e) and
                (self.m_d == 0 or self.m_d >= self.c_d))

    def estado_final(self):

        # Verifica se o estado atual é um estado solução.
        resultado_esquerda = self.m_e == self.c_e == 0
        resultado_direita = self.m_d == self.c_d == 3
        return resultado_esquerda and resultado_direita

    def gerar_filhos(self):

        # Gera os possíveis filhos de um estado, desde que este seja um estado válido e não seja um estado solução;
        # e apos isso ncontra o n_l_r = novo lado do rio.
        n_l_r = 'dir' if self.l_r == 'esq' else 'esq'
        # lista os possíveis movimentos.
        movimentos = [
            {'missionarios': 2, 'canibais': 0},
            {'missionarios': 1, 'canibais': 0},
            {'missionarios': 1, 'canibais': 1},
            {'missionarios': 0, 'canibais': 1},
            {'missionarios': 0, 'canibais': 2},
        ]
        # Gera todos os possíveis estados e armazena apenas os válidos na lista de filhos do estado atual.
        for movimento in movimentos:
            if self.l_r == 'esq':
                # Caso o barco esteja a esquerda do rio, os missionários e canibais saem da esquerda para a direita.
                m_e = self.m_e - movimento['missionarios']
                m_d = self.m_d + movimento['missionarios']
                c_e = self.c_e - movimento['canibais']
                c_d = self.c_d + movimento['canibais']
            else:
                # Caso contrário os missionários e canibais saem da direita para a esquerda.
                m_d = self.m_d - movimento['missionarios']
                m_e = self.m_e + movimento['missionarios']
                c_d = self.c_d - movimento['canibais']
                c_e = self.c_e + movimento['canibais']
            # Cria o estado do filho e se for válido, o adiciona à lista de filhos.
            filho = Estado(m_e, m_d, c_e, c_d, n_l_r)
            filho.pai = self
            if filho.estado_valido():
                self.filhos.append(filho)


class Missionarios_Canibais():

    # Gera a arvore de estados para eesolver o problema.

    def __init__(self):

        # Inicializa o problema com o estado-raiz prédefinido e insere a raiz na fila de execução.
        self.fila_execucao = [Estado(3, 0, 3, 0, 'esq')]
        self.solucao = None

    def gerar_solucao(self):

        # Realiza a busca em largura em busca da solução.
        for elemento in self.fila_execucao:
            if elemento.estado_final():
                # Se a solução foi encontrada, o caminho-solução é gerado percorrendo o caminho de volta até a raiz.
                self.solucao = [elemento]
                while elemento.pai:
                    self.solucao.insert(0, elemento.pai)
                    elemento = elemento.pai
                break;
            # se não for a solução, gera seus filhos e os adiciona na fila de execução.
            elemento.gerar_filhos()
            self.fila_execucao.extend(elemento.filhos)


def main():
    # Instancia o problema.
    problema = Missionarios_Canibais()
    problema.gerar_solucao()
    # Inicialindo o Pygame e criando janela.
    pygame.init()
    display = pygame.display.set_mode([1350, 400])
    pygame.display.set_caption('Missionarios e Canibais')
    objectGroup = pygame.sprite.Group()
    estados = estado_inicial(objectGroup)

    #Exibe a solucao.
    for estado in problema.solucao:
        print(estado)
        print(34 * '-')

    estados = estado1(objectGroup)
    estados = estado2(objectGroup)
    estados = estado3(objectGroup)
    estados = estado4(objectGroup)
    estados = estado5(objectGroup)
    estados = estado6(objectGroup)
    estados = estado7(objectGroup)
    estados = estado8(objectGroup)
    estados = estado9(objectGroup)
    estados = estado10(objectGroup)
    estados = estado_final(objectGroup)
    gameLoop = True
    clock = pygame.time.Clock()
    if __name__ == '__main__':
            while gameLoop:
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameLoop = False

                # atualizar e desenhar
                display.fill([30, 20, 20])
                objectGroup.update()
                objectGroup.draw(display)
                pygame.display.update()

if __name__ == '__main__':
    main()
