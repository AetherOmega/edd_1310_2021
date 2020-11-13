from array_2d import Array2D
class Juego:
    CELULA_VIVA = 1
    CELULA_MUERTA = 0
    def __init__(self,rens,cols,generaciones,poblacion):
        self.largo = cols
        self.alto = rens
        self.grid = Array2D (self.alto, self.largo,0)
        self.generaciones = generaciones
        self.grid.clearing(self.CELULA_MUERTA)
        self.poblacion=poblacion

    def tupla(self):
        self.poblacion=[(1,2), (2,1), (2,2), (2,3)]
        for celula in self.poblacion:
            self.grid.set_item(celula[0],celula[1],self.CELULA_VIVA)
        print(self.imprime_grid())

    def configura_generaciones(self,nueva_poblacion):
        self.grid.clearing()
        for celula in nueva_poblacion:
            self.grid.set_item(celula[0],celula[1],self.CELULA_VIVA)
        print(self.imprime_grid())

        def imprime_grid(self):
        for r in range(self.grid.get_num_rows()):
            for c in range(self.grid.get_num_cols()):
                if self.grid.get_item(r,c) == 0:
                    print("░░",end="")
                else:
                    print("▓▓",end="")
            print("")

     def get_num_rows(self):
         return self.alto

    def get_num_cols(self):
        return self.largo

    def set_celula_muerta(self, row, col):
        self.grid.set_item(row, col, self.CELULA_MUERTA)

    def set_celula_viva(self, row, col):
        self.grid.set_item(row, col, self.CELULA_VIVA)

    def get_is_viva( self, row, col):
        return self.grid.get_item(row,col) == self.CELULA_VIVA


     def get_is_muerta( self, row, col):

     def __ajusta_limites__(self,lim):
         lim[0] = lim[0] + 1 if lim[0] == -1 else lim[0]
         lim[0] = lim[1] + 1 if lim[1] == -self.alto else lim[1]
         lim[0] = lim[2] + 1 if lim[2] == -1 else lim[1]
         lim[0] = lim[3] + 1 if lim[3] == self.largo else lim[3]
         print("lim",lim)
         return lim

     def get_numero_vecinos_vivos(self, row, col):
         limites=[ row-1, row+1, col-1, col+1]
         vivos = 0
         imites=self.__ajusta_limites__(limites)
         if row >= 0 and row <= self.alto-1 and col >= 0 and col <= self.largo-1:
             for r in tange(limites[0],limites[1]+1):
                 for c in range(limites[2],limites[3]+1):
                     if r == row and c == col:
                         continue
                     else:
                         if self.grid.get_item(r,c) == self.CELULA_VIVA:
                             vivos += 1

         else :
             print("Coordenada la celula fuera del grid")
        return vivos

     def evolucionar( self, celulas_nacidas, celulas_muertas):
        for celula_nueva in celulas_nacidas:
            self.grid.set_item(celula_nueva[0],celula_nueva[1],self.CELULA_VIVA)
        for muertas in celulas_muertas:
            self.grid.set_item(muertas[0], muertas[1], self.CELULA_MUERTA)
            imprime_grid() 
