from __future__ import annotations



class No:
    # Nós do encadeamento
    
    prox : No | None

    def __init__(self, elem :int) -> None:

        

        self.item = elem
        self.prox = None


class Pilha:
    # Estrura da pilha e suas funções básicas
    
    topo: No | None

    def __init__(self) -> None:
        
        
        #Cria uma pilha vazia
        
        self.topo = None
        self.comprimento = 0

    def __len__(self) -> int:
        
        #comprimento da pilha através da função len()
    
        return self.comprimento

    def vazia(self) -> bool:
        
        #Devolve True se a pilha está vazia, False caso contrário.
        
        return self.topo is None

    def elem_topo(self) ->  int:
        
        #retorna o elemento do topo da pilha
        
        if self.topo is None:
            raise ValueError('Pilha Vazia')
        return self.topo.item

    def empilha(self, item: int):
        
        #Adiciona o *item* na pilha.
        
        if self.topo:
            ponteiro = No(item)
            ponteiro.prox = self.topo
            self.topo = ponteiro
        else:
            self.topo = No(item)
        self.comprimento += 1

    def desempilha(self) -> int:
        
        #Devolve o elemento mais recentemente adicionado da pilha.

        #Requer que a pilha não esteja vazia.
        
        if self.topo is None:
            raise ValueError('pilha vazia')
        item = self.topo.item
        self.topo = self.topo.prox
        self.comprimento -= 1
        return item

    def __repr__(self):
        
        #Representação da pilha em lista, o elemento do topo será o primeiro elemento e seus sucessores os seguintes
        
        ponteiro = self.topo
        elementos = []
        while ponteiro != None:
            elementos.append(ponteiro.item)
            ponteiro = ponteiro.prox
        return str(elementos)
    
'''
x = Pilha()
print(x.vazia())
x.empilha(7)
x.empilha(8)
print(x.elem_topo())
x.empilha(10)
print(x)
print(len(x))
x.desempilha()
print(x)
print(x.vazia())
'''