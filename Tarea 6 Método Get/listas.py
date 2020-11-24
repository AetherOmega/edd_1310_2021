class Nodo:
    def _init_( self , value , siguiente= None):
        self.data = value
        self.siguiente = siguiente

#Metodo head
class LinkedList:
    def _init_( self ): #
        self.__head = None

#Metodo empty
    def is_empty( self ):
        return self.__head == None

#Metodo append (Agrega el nodo al final entrando por head.)
    def append( self , value ):
        nuevo = Nodo( value )
        if self.__head == None: # self.is_empty()
            self.__head = nuevo
        else:
            curr_node = self.__head
            while curr_node.siguiente != None:
                curr_node = curr_node.siguiente
            curr_node.siguiente = nuevo

#Metodo transveral
    def transversal( self ):
        curr_node = self.__head
        while curr_node != None:
            print(f" { curr_node.data } -> " , end="")
            curr_node = curr_node.siguiente
        print(" ")

#Metodo remove
    def remove(self, value):
        curr_node = self.__head
        if self.__head.data == value: # Este if cambia de nodo si se esta eliminando head
            self._head = self._head.siguiente
        else:
            anterior = None
            while curr_node.data != value and curr_node.siguiente != None:
                anterior = curr_node #con esto se almacena el nodo anterior
                curr_node = curr_node.siguiente
            if curr_node.data == value:
                anterior.siguiente = curr_node.siguiente
            else:
                print("El dato no existe en la lista")

#Metodo preppend
    def preppend(self,value):
        nuevo = Nodo(value, self.__head) #Crea el nuevo nodo
        self.__head = nuevo #Le da al nuevo nodo el valor de head

    def get(self,posicion = None): #Por defecto regresa el ultimo
        contador = 0
        dato = None
        if posicion == None:
            dato = self.tail().data #Esto se convierte en un Nodo
        else:
            dato = self.preppend().data
            contador+1
        return dato
