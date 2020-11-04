from arrays import Array
class asalariado(Array):
    def horas_extra( self, s_base, extra):
        return int(s_base)+(276.5*int(extra))

    def prestaciones(self, anio_ingreso,sueldo):
        antiguedad = 2020 - int(anio_ingreso)
        prestaciones = int(sueldo)*((3*antiguedad)/100)
        return prestaciones

archivo = open('junio.dat', 'rt')
archivo.readline()
obreros = asalariado(14)
for obrero in range(obreros.get_length()):
    datos = archivo.readline().split(',')
    obreros.set_item(datos,obrero)

#Sueldo por horas extra
for obrero in obreros:
    n_sueldo = obreros.horas_extra(obrero[5], obrero[4])
    obrero[5] = n_sueldo

#Prestaciones
for obrero in obreros:
    obrero[5] = int(obrero[5]) + obreros.prestaciones(obrero[6][0:4], obrero[5])

for obrero in obreros:
    print(obrero)

#Antuguedad de los empleados
for x in range(obreros.get_length()):
    for y in range(obreros.get_length()-1):
        if obreros.get_item(y)[6][0:14] > obreros.get_item(y+1)[6][0:4]:
            burbuja = obreros.get_item(y)
            '''obreros[y] = obreros[y+1]'''
            obreros.set_item(obreros.get_item(y+1),y)
            '''obreros[y+1] = burbuja'''
            obreros.set_item(burbuja,y+1)
            print(obreros)
