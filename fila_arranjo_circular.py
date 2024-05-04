from typing import Any


class FilaCircular:

    # Funciona como uma fila, adiciona o elemento no final e remove o elemento no inicio do vetor.

    valores: list[Any]
    # Indíce onde o próximo elemento será inserido
    tamanho : int
    # comprimento do vetor, quando o inicio ou o fim cheagam a este valor, seus valores retornam a zero
    fim: int
    # Indíce do primeiro elemento da fila
    inicio: int

    
    def __init__(self, tamanho: int) -> None:
    
        #Cria uma nova fila com capacidade para armazenar *tamanho*
        #elementos.
        
        
        self.valores = []
        i: int = 0
        while i < tamanho:
            self.valores.append(None)
            i += 1
        self.tamanho = tamanho 
        self.inicio = 0
        self.fim = 0

    def enfileira(self, item: int):
        
        #Adiciona *item* no final da fila.

        #Requer que a quantidade de elementos na fila seja menor que
        #*tamanho*.

        
        if self.cheia():
            raise ValueError('fila cheia')
        
        if self.fim == self.tamanho:
            self.fim = 0
        self.valores[self.fim] = item
        self.fim += 1

    def desenfileira(self) -> str:
        
        #Remove e devolve o primeiro elemento da fila.

        #Requer que a fila não esteja vazia(apenas elementos None).

        
        if self.vazia():
            raise ValueError('fila vazia')
        if self.inicio == self.tamanho:
            self.inicio = 0
        
        item = self.valores[self.inicio]
        self.valores[self.inicio] = None
        self.inicio += 1
        return item

    def vazia(self) -> bool:
        
        #Devolve True se a fila está vazia, False caso contrário.

    
        return self.inicio == self.fim and self.valores[0] is None
            
        

    def cheia(self) -> bool:
        
        #Devolve True se a fila está vazia, isto é, a quantidade de elementos na
        #fila é igual a *tamanho*, False caso contrário.
        
    
        return self.inicio == self.fim and self.valores[0] is not None
        
    def primeir0_elem(self) -> int:
        # Devolve o primeiro elemento da lista
        if self.vazia():
            raise ValueError('fila vazia')
        return self.valores[self.inicio]
    
    def ultimo_elem(self) -> int:
        # Devolve o ultimo elemento da lista
        if self.vazia():
            raise ValueError('fila vazia')
        return self.valores[self.fim - 1]
    
    def __len__(self) -> int:
        #quantidade de elementos

        if self.vazia():
            return 0
        elif self.cheia():
            return self.tamanho
        else:
            return abs(self.fim - self.inicio)
    
    def __repr__(self) -> str:
        # representação da fila circular na forma de list
        return str(self.valores)
    

x = FilaCircular(5)
print(x.cheia())
print(x.vazia())
print(x)
x.enfileira(3)
x.enfileira(4)
x.enfileira(6)
x.enfileira(8)
x.enfileira(9)
x.desenfileira()
x.desenfileira()
x.desenfileira()
x.desenfileira()
x.desenfileira()
print(x.vazia())

print(x.vazia())
print(x)
print(x.cheia())

x.enfileira(5)
x.enfileira(10)
print(x)
print(x.cheia())
x.desenfileira()
x.enfileira(7)
print(x)
print(x.primeir0_elem())
print(x.ultimo_elem())
print(len(x))
