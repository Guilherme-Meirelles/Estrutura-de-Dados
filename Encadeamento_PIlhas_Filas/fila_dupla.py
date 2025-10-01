from __future__ import annotations
from typing import Any

class FilaDupla:
   
    

    def __init__(self, tamanho: int) -> None:
        
        #Cria uma nova fila com capacidade para armazenar *tamanho* elementos.
        # o vlaor *None* será a representão de um local do vetor sem elementos
        
        i = 0
        self.valores : list[Any] = []
        while i < tamanho:
            self.valores.append(None)
            i += 1
        self.inicio_esquerda = tamanho // 2 
        self.fim_direita = self.inicio_esquerda
        self.tamanho = tamanho

    def enfileira_direita(self, item: int) -> None:
        
        #Adiciona *item* no final da fila.

        #Requer que a quantidade de elementos na fila seja menor que o
        #*tamanho*.
        
        if self.fim_direita == self.tamanho:
            if self.cheia():
                raise ValueError('fila cheia')
        self.valores[self.fim_direita] = item
        self.fim_direita += 1

    def desenfileira_direita(self) -> int:
        
        #Remove e devolve o primeiro elemento da fila.

        #Requer que a fila não esteja vazia.
        
       
        if self.vazia():
            raise ValueError('fila vazia')
        self.fim_direita -= 1
        item = self.valores[self.fim_direita]
        self.valores[self.fim_direita] = None
        
        return item

    def enfileira_esquerda(self, item: int) -> None:
        
        #Adiciona *item* no final da fila.

        #Requer que a quantidade de elementos na fila seja menor que o
        #*tamanho*.
        
        if self.inicio_esquerda == 0:
            if self.cheia():
                raise ValueError('fila cheia')
        self.inicio_esquerda -= 1
        self.valores[self.inicio_esquerda] = item

    def desenfileira_esquerda(self) -> int:
        
        #Remove e devolve o primeiro elemento da fila.

        #Requer que a fila não esteja vazia.
        
       
        if self.vazia():
            raise ValueError('fila vazia')
        item = self.valores[self.inicio_esquerda]
        self.valores[self.inicio_esquerda] = None
        self.inicio_esquerda += 1
        return item

    def vazia(self) -> bool:
        
        #Devolve True se a fila está vazia, False caso contrário.

    
        return self.fim_direita == self.inicio_esquerda

    def cheia(self) -> bool:
        
        #Quando o vetor tem a mesma quantidade de elementos que o seu *tamnaho* então o vetor está cheio
        
        self.deslocar_fila()
        return self.inicio_esquerda == 0 and self.fim_direita == self.tamanho
    
    def deslocar_fila(self):
        
        #Caso o vetor não esteje cheio mas uma de suas extremidades está ocupada por elementos.
        #Desloca-se estes elementos para poderem ser adicionados mais elementos em uma das extremidades
        
    
        if self.fim_direita == self.tamanho:
            desloc = (self.inicio_esquerda + 1) // 2
            if desloc > 0:
                for i in range(self.inicio_esquerda, self.fim_direita ):
                    self.valores[i - desloc] = self.valores[i]
                    self.valores[i] = None
            self.inicio_esquerda = self.inicio_esquerda - desloc
            self.fim_direita = self.fim_direita - desloc
        else:
            desloc = ((self.tamanho - self.fim_direita ) + 1) // 2
            if desloc > 0:
                for i in range(self.fim_direita - 1, self.inicio_esquerda -1 , -1):
                    self.valores[i + desloc] = self.valores[i]
                    self.valores[i] = None
            self.inicio_esquerda = desloc + self.inicio_esquerda
            self.fim_direita = desloc + self.fim_direita
    
    def primeiro(self) -> int:
        
        #Revela o primeiro elemento da fila
        
        if self.vazia():
            raise ValueError('fila vazia')
        return self.valores[self.inicio_esquerda]
    
    def ultimo(self) -> int:
        
        #Revela o ultimo elemento da fila
        
        if self.vazia():
            raise ValueError('fila vazia')
        return self.valores[self.fim_direita - 1]
    
    def __len__(self) -> int:
        return self.fim_direita - self.inicio_esquerda


    def __repr__(self) -> str:
        
        #Representação da fila
        
        return str(self.valores)
    
'''
x = FilaDupla(8)

print(x.vazia())
x.enfileira_direita(7)
x.enfileira_direita(7)
x.enfileira_direita(7)
x.enfileira_direita(7)
x.desenfileira_esquerda()
print(x)
x.enfileira_direita(7)
print(x)
x.enfileira_esquerda(133)
x.enfileira_esquerda(10)
x.enfileira_esquerda(11)
x.enfileira_esquerda(12)
print(x.cheia())
print(x)
x.desenfileira_direita()
x.desenfileira_direita()
x.desenfileira_direita()
x.enfileira_esquerda(13)
print(x)
'''
