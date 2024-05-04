from __future__ import annotations
from typing import Any
class Fila:
   
    

    def __init__(self, tamanho) -> None:
        
        #Cria uma nova fila com capacidade para armazenar *tamanho* elementos.
        # o vlaor *None* será a representão de um local do vetor sem elementos
        
        i = 0
        self.valores : list[Any] = []
        while i < tamanho:
            self.valores.append(None)
            i += 1
        self.inicio = 0
        self.fim = -1

    def enfileira(self, item: int) -> None:
        
        #Adiciona *item* no final da fila.

        #Requer que a quantidade de elementos na fila seja menor que o
        #*tamanho*.
        
        
        if self.cheia():
            raise ValueError('fila cheia')
        self.fim += 1
        self.valores[self.fim] = item

    def desenfileira(self) -> Any:
        
        #Remove e devolve o primeiro elemento da fila.

        #Requer que a fila não esteja vazia.
        
       
        if self.vazia():
            raise ValueError('fila vazia')
        item = self.valores[self.inicio]
        self.valores[self.inicio] = None
        self.inicio += 1
        return item

    def vazia(self) -> bool:
        
        #Devolve True se a fila está vazia, False caso contrário.

    
        return self.fim < self.inicio

    def cheia(self) -> bool:
        
        #Quando o valor do self.fim da fila é igual ao tamanho da fila -1, então a fila está cheia.
        #Não podendo adicionar mais elementos
        self.deslocar_fila()
        return self.fim >= len(self.valores) - 1
    
    def deslocar_fila(self):
        
        #Caso haja elementos *None* antes do primeiro elemento do vetor.
        #Desloca a fila para o primeiro elemento ficar na posição zero e joga os elementos vão*None* para o fim do vetor
        
        desloc = self.inicio
        if desloc > 0:
            for i in range(desloc, self.fim + 1):
                self.valores[i - desloc] = self.valores[i]
                self.valores[i] = None
            self.inicio = 0
            self.fim = self.fim - desloc
    
    def primeiro(self) -> int:
        
        #Revela o primeiro elemento da fila
        
        if self.vazia():
            raise ValueError('fila vazia')
        return self.valores[self.inicio]
    
    def ultimo(self) -> int:
        
        #Revela o ultimo elemento da fila
        
        if self.vazia():
            raise ValueError('fila vazia')
        return self.valores[self.fim]

    def __len__(self) -> int:
        return self.fim - self.inicio

    def __repr__(self) -> str:
        
        #Representação da fila
        
        return str(self.valores)
'''
x = Fila(4)
print(x.vazia())
x.enfileira(5)
x.enfileira(8)
x.enfileira(9)
x.enfileira(10)
print(x.primeiro())
print(x.ultimo())
print(x.cheia())
print(x.desenfileira())
print(x.cheia())
print(x)
print(x.desenfileira())
print(x)
x.enfileira(15)
x.deslocar_fila()
print(x)
'''