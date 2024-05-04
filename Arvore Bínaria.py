from typing import Any
from random import randint,sample,seed
from fila_arranjo_inicio_fim import Fila

class Node:
    
    def __init__(self,item):
        self.item = item
        self.direita = None
        self.esquerda = None

    def __repr__(self) -> str:
        return str(self.item)
        

class Arvore_Binaria:
    no : Node

    def __init__(self, item = None, no = None):
        if no:
            self.raiz = no
        elif item:
            x = Node(item)
            self.raiz = x
        else:
            self.raiz = None

    def percurso_in_ordem(self,no = None) -> Any:
        
        if no is None:
            no = self.raiz
        if no.esquerda:
            #print('(', end = ' ')
            self.percurso_in_ordem(no.esquerda)
        print(no, end = ' ')
        if no.direita:
            self.percurso_in_ordem(no.direita)
            #print(')', end=' ')


    def percurso_pre_ordem(self,no = None) -> Any:
        
        if no is None:
            no = self.raiz
        print(no, end = ' ')
        if no.esquerda:
            self.percurso_pre_ordem(no.esquerda)
        if no.direita:
            self.percurso_pre_ordem(no.direita)
        

    def percurso_pos_ordem(self,no = None) -> Any:
        
        if no is None:
            no = self.raiz
        if no.esquerda:
            self.percurso_pos_ordem(no.esquerda)
        if no.direita:
            self.percurso_pos_ordem(no.direita)
        print(no, end = ' ')


    def altura(self,no = None) -> int:
        
        if no is None:
            no = self.raiz
        altura_esquerda = 0
        altura_direita = 0
        if no.esquerda:
           altura_esquerda = self.altura(no.esquerda)
        if no.direita:
            altura_direita = self.altura(no.direita)
        if altura_esquerda > altura_direita:
            return altura_esquerda + 1
        else:
            return altura_direita + 1
        
class Arvore_Binaria_de_Busca(Arvore_Binaria):

    def inserir(self, valor):

        pai = None
        aux = self.raiz
        while(aux):
            pai = aux
            if valor < aux.item:
                aux = aux.esquerda
            else:
                aux = aux.direita
        if pai == None:
            self.raiz = Node(valor)
        elif valor < pai.item:
            pai.esquerda = Node(valor)
        else:
            pai.direita = Node(valor)
    
    def buscar(self, valor):

        return self._buscar(valor, self.raiz)

    def _buscar(self, valor, no = Node):

        if no is None:
            return no
        if no.item == valor:
            return Arvore_Binaria_de_Busca(no)
        if valor < no.item:
            return self._buscar(valor, no.esquerda)
        else:
            return self._buscar(valor, no.direita)
    
    def percuso_em_nivel(self, no = None):

        if no == None:
            no = self.raiz

        fila = Fila(self.altura() ** 2)
        fila.enfileira(no)
        while fila.vazia() is False:
            no = fila.desenfileira()
            if no.esquerda:
                fila.enfileira(no.esquerda)
            if no.direita:
                fila.enfileira(no.direita)
            print(no, end = ' ')

    def menor_elem(self, no = None):
        
        if no == None:
            no = self.raiz
        while no.esquerda:
            no = no.esquerda
        return no
    
    def maior_elem(self, no = None):

        if no == None:
            no = self.raiz
        while no.direita:
            no = no.direita
        return no
    
    def remove(self, valor : int, no = ''):
        # Não consegui implementar
        return None
                
            
            
     
       
    


        '''
        def buscar(self, valor, no = 0):

        if no == 0:
            no = self.raiz
        if no is None or no.item == valor:
            return no
        if valor < no.item:
            return self.buscar(valor, no.esquerda)
        else:
            return self.buscar(valor, no.direita)
        '''
        
    '''
    def caminho_esquerdo(self, no=None):
        
        if no is None:
            no = self.raiz
        y = 0
        if no.esquerda:
            y = self.caminho_esquerdo(no.esquerda)
        return y + 1
    '''

        
            

'''
x = Arvore_Binaria('+')
x.raiz.direita = Node('-')
x.raiz.esquerda = Node('*')
x.raiz.esquerda.esquerda = Node(1)
x.raiz.esquerda.direita = Node('/')
x.raiz.esquerda.direita.direita = Node(10)
x.raiz.esquerda.direita.esquerda = Node(3)
x.raiz.direita.esquerda = Node(4)
x.raiz.direita.direita = Node(5)
x.percurso_in_ordem()
print()
x.percurso_pre_ordem()
print()
x.percurso_pos_ordem()
print()
print(x.altura())
#print(x.caminho_esquerdo())
'''
seed(77)
valores = sample(range(1,100), 10)
print(valores)
y = Arvore_Binaria_de_Busca()
for v in valores:
    y.inserir(v)

y.percurso_in_ordem()
print()
y.percuso_em_nivel()
print()
print(y.remove(33))
print(' ')
y.percurso_in_ordem()
print()
y.percuso_em_nivel()


'''
z = [1, 44, 19, 33, 90]
for c in z:
    a = y.buscar(c)
    if a is None:
        print(c, 'Não encontrado')
    else:
        print(a.raiz.item, "Encontrado")


print(y.menor_elem())
print(y.maior_elem())
'''
