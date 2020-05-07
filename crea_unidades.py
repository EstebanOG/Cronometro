#Se crean los objetos de cada unidad de tiempo
from unidad_tiempo import unidad
class crea:
    ms = unidad()
    ss = unidad()
    mm = unidad()
    hh = unidad()
    def crea_instancias(self):
        self.ms.valor_maximo=10
        self.ss.valor_maximo=60
        self.mm.valor_maximo=60
        self.hh.valor_maximo=60