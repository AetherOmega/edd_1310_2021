class Stack:
    def _init_( self ):
        self.__data = list()

    def is_empty( self ):
        return len( self.__data ) == 0

    def lenght( self ):
        return len( self.__data )

    def pop( self ):
        if self.is_empty():
            print("La pila está vacía")

        else:
            return self.__data.pop()

    def push( self, value):
        self.__data.append( value )

    def peek( self ):
        return self._data[ len( self._data) - 1]

    def to_string( self ):
        for item in self.__data[::-1]:
            print(" ********************* ")
            print(f" |------------- {item}------------ | ")

def suma_lista_rec( lista ):
    if len(lista) == 1:
        return lista[0]

    else:
        return ( lista.pop() + suma_lista_rec( lista ) )

def contadorRegresivo( n ):
    if n > 0:
        print(n)

        contadorRegresivo(n - 1)
    if n == 0:
        print(n)
        print("//////////Acabando cuenta regresiva///////////")

def pila_mid( pila, valor_mid ):
    pico = pila.pop()

    if pila.lenght() != valor_mid + 1:
        pila_mid(pila, valor_mid)
    else:
        pila.pop()

    pila.push( pico )

def main_pila( ):
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)
    s.push(9)
    s.push(10)
    s.push(11)
    s.to_string()

    mitad = ( s.lenght() / 2 )

    if (mitad % 2) != 0:
        mitad = int(mitad)

    print("\nObteniendo mitad \n")
    pila_mid(s, mitad)
    s.to_string()

def main_contador():
    contadorRegresivo(10)

def main_suma_lista( ):
    datos = [4, 2, 3, 5] #14
    res = suma_lista_rec( datos )
    print( res )
