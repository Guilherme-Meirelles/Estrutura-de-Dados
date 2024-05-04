from __future__ import annotations
from typing import List, Any
from random import shuffle
from copy import deepcopy

class Pilha:
    """Classe representando uma pilha"""

    def __init__(self) -> None:
        # Representa os itens da nossa pilha
        self.__elem: List[int] = [-1,-1,-1,-1]
        # Representa a quantidade de elementos
        self.__topo = -1

    #Verifica se a pilha está vazia (0 elementos)
    def pilha_vazia(self) -> bool:
        return self.__topo == -1

    #Verifica se a pilha está cheia (4 elementos)
    def pilha_cheia(self) -> bool:
        return self.__topo == 3
    
    #Verifica a quantidade de elementos da pilha
    def quantidade_elementos(self) -> int:
        return self.__topo + 1

    # Verifica o elemento do topo da lista ( o de maior índice)
    def elemento_do_topo(self) -> int:
        if not self.pilha_vazia():
            return self.__elem[self.__topo]
        else:
            raise ValueError('Erro: Pilha Vazia')
    
    # Adiciona elementos para a pilha, pode-se adicionar no máximo 4 elementos sem remove-los
    def empilha(self, x: int) -> None:
        if not self.pilha_cheia():
            self.__topo +=1 
            self.__elem[self.__topo] = x
        
    # Remove elementos da pilha, não remove elementos de uma pilha vazia
    def desempilha(self) -> Any:
        if not self.pilha_vazia():
            x = self.__elem[self.__topo]
            self.__elem[self.__topo] = -1
            self.__topo -= 1
            return x

    # Define como a pilha será representada. Ex: [1, 2, 3]
    def __repr__(self) -> str:
        return f'{self.__elem}'


#Jogo de Gerenciamento de Pilhas

#Faz a lista de pilhas do jogo
def lista_de_pilhas(n :int) -> list[Pilha]:

    pilha = Pilha()
    b: int = n + 2
    list_pilhas: list[Pilha] = []
    while b > 0:
        list_pilhas.append(deepcopy(pilha))
        b -= 1
    return list_pilhas

#Gera os números que serão sorteados nas pilhas
def lista_de_inteiros(n :int) -> list[int] :

    lista :list = []
    for c in range(0, 4):
        for d in range(1, n+1):
            lista.append(d)
    shuffle(lista)
    return lista

#Enche as pilhas com os números sorteados
def enche_lista_de_pilhas(list_int: list[int], list_pihas: list[Pilha]) -> list[Pilha]:

    contador = 0
    for c in range(0, len(list_pihas) - 2):
        for d in range(0, 4):
            list_pihas[c].empilha(list_int[contador])
            contador += 1
    return list_pihas

#Define as jogadas e suas condições, se uma das condições não for atendida a jogada não é feita
def jogada(lista_de_pilhas: list[Pilha], pilha1_posição:int, pilha2_posição:int) -> list[Pilha]:

    pilha1 = lista_de_pilhas[pilha1_posição]
    pilha2 = lista_de_pilhas[pilha2_posição]
    if not pilha1.pilha_vazia():
        if not pilha2.pilha_cheia():
            if not pilha2.pilha_vazia() and not pilha1.elemento_do_topo() == pilha2.elemento_do_topo():
                print('Erro: Elementos do topo são diferentes')
            else:
                pilha2.empilha(pilha1.elemento_do_topo())
                pilha1.desempilha()
        else:
            print('Erro: Pilha2 cheia')
    else:
        print('Erro: Pilha1 vazia ')
    return lista_de_pilhas

#Define quando o jogo termina e o jogador vence
def vencedor(lista_de_pilhas: list[Pilha]) -> bool:
    a = deepcopy(lista_de_pilhas)
    x = True
    for b in a:
        if b.quantidade_elementos()< 4 and b.quantidade_elementos() > 0:
            x = False
        else:
            while b.quantidade_elementos() > 1 and x == True:
                d = b.desempilha()
                c = b.elemento_do_topo()
                if c != d:
                    x = False
    return x


def main():
    

    n :int = int(input('Escolha um número de um número de 1 a 7 para o jogo:'))

    
    list_vazia_pilhas: list[Pilha] = lista_de_pilhas(n)
    

    list_de_num_inteiros: list[int] = lista_de_inteiros(n)


    list_pilhas: list[Pilha] = enche_lista_de_pilhas(list_de_num_inteiros, list_vazia_pilhas)
    print(list_pilhas)
    


    while True:
        x = int(input('Digite a posição de 0 a n+1 da lista de bolinhas, qual frasco você desempilhará uma bolinha:'))
        y = int(input('Digite a posição de 0 a n+1 da lista de bolinhas, qual frasco você empilhará uma bolinha:'))
        print(jogada(list_pilhas, x, y))
        if vencedor(list_pilhas) == True:
            break
    print('Venceu')


if __name__ == "__main__":
    main()

















