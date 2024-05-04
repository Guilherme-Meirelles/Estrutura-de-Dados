class Node:

    def __init__(self, data):
        # Encadeamento
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        # Constroi uma lista ligada
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            # inserção quando a lista já possui elementos
            pointer = Node(elem)
            pointer.next = self.head
            self.head = pointer

        else:
            # primeira inserção
            self.head = Node(elem)
        self._size = self._size + 1

    def remove(self, elem):
        # Remove um elemento a partir de seu índice
        if self.head.data == elem:
            pointer = self.head.next
            self.head.next = None
            self.head = pointer
            index = 0
        else:
            pointer = self.head
            index = 1
            while pointer and pointer.next.data != elem:
                    index += 1
                    pointer = pointer.next

            if pointer.next.data == elem:
                pointer_aux = pointer.next
                pointer.next = pointer_aux.next
                pointer_aux.next = Node
            else:
                raise IndexError('Element not found')
        self._size -= 1
        return index


        
    def __len__(self):
        # Retorna o tamanho da lista
        return self._size
    
    def __getitem__ (self, index):
        # busca de elemento por indice, indice da cabeça da lista é igual a 0
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('list out of range')
        if pointer:
            return pointer.data
        else:
            raise IndexError('list out of range')
        
    def __setitem__ (self, index, elem):
        # modificação de elemento por indice
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('list out of range')
        if pointer:
            pointer.data = elem
        else:
            raise IndexError('list out of range')
        
    def index(self, elem):
        # Descobre se um elemento está na lista e devolve seu índice
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError(f'{elem} is not in list')
    
    def __repr__(self):
        aux = []
        if self.head != None:
            pointer = self.head
            while pointer:
                aux.append(pointer.data)
                pointer = pointer.next
        return str(aux)
    
'''
no1 = Node(5)
no2 = Node(7)
print(no1.data)
no1.next = no2
print(no1.next.data)

x = LinkedList()

x.append(5)
x.append(10)
x.append(8)
x[0] = 3
print(x)
x.index(5)
x.append(7)
print(x.remove(10))
print(len(x))
print(x[1])
print(x)
'''