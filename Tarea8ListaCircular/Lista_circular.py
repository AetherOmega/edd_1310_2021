#lista circular

class Nodo:
    def __init__( self , value):
        self.data = value
        self.siguiente = None

class ListaCircular:
    def __init__(self, head):
        self.head = head
        self.head.next = head

#Metodo lenght
    def length(self):
        current = self.head.next
        conta = 1
        if self.head is not None:
            while current != self.head:
                conta += 1
                current = current.next
                return conta
            else:
                return 0

#Metodo empty
    def is_empty( self ):
            return self.__head == None

#Metodo insert
    def insert(self, nodo, posicion):
        if posicion == 0:
            ultimo_elemento = self.search(-1)
            ultimo_elemento.next = nodo
            nodo.next = self.head
            self.head = nodo
        elif posicion < 0:
            ultimo_elemento = self.search(-1)
            ultimo_elemento.next = nodo
            nodo.next = self.head
        else:
            elemento = self.search(posicion)
            nodo.next = elemento.next
            elemento.next = nodo

#Metodo transversal
    def transversal( self ):
        curr_node = self.__head
        while curr_node != None:
            print(f" { curr_node.data } -> " , end="")
            curr_node = curr_node.siguiente
        print(" ")

#Metodo search
    def search(self, nodo, ante=False):
            if nodo == 0:
                if ante is False:
                    return self.head
                else:
                    return [self.search(-1), self.head]
            elif nodo < 0:
                current = self.head
                while current.next !=self.head:
                    anterior = current
                    valor = current.next
                return valor if ante is False else [anterior, valor]
            else:
                f = 1
                valor = self.head
                while f < nodo and valor.next !=self.head:
                    f += 1
                    anterior = valor
                    valor = valor.next
                return valor if ante is False else [anterior, valor]

#Metodo remove
    def remove(self, posicion):
        if posicion > 1:
            anterior = self.search(posicion-1)
        elif posicion < 0:
            anterior = self.search(-1, True)[0]
        else:
            anterior = self.search(-1)
            self.head = anterior.next.next
        anterior.next = anterior.next.next
