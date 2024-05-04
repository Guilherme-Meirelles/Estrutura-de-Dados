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
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)

        else:
            # primeira inserção
            self.head = Node(elem)
        self._size = self._size + 1

    def remove(self, index):
        # Remove um elemento a partir de seu índice
        if index == 0:
            elem = self.head.data
            pointer = self.head.next
            self.head = None
            self.head = pointer
        else:
            pointer = self.head
            for i in range(index - 1):
                if pointer:
                    pointer = pointer.next
                else:
                    raise IndexError('list out of range')
            pointer2 = pointer.next
            elem = pointer2.data
            pointer.next = pointer2.next
            pointer2 = None
        self._size -= 1
        return elem


        
    def __len__(self):
        # Retorna o tamanho da lista
        return self._size
    
    def __getitem__ (self, index):
        # busca de elemento
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
        # modificação de elemento
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
x.index(10)
print(x.remove(1))
print(len(x))
print(x[1])
'''