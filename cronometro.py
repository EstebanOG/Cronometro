import time
from crea_unidades import crea as instancias

class cronometro:

    def start(self):    
        instancias.crea_instancias(instancias)          
        time.sleep(0.1)
        instancias.ms.valor_actual=instancias.ms.valor_actual+1
        if instancias.ms.maximo_alcanzado()==True:
            instancias.ss.valor_actual = instancias.ss.valor_actual+1 
        if instancias.ss.maximo_alcanzado()==True:
            instancias.mm.valor_actual = instancias.mm.valor_actual+1 
        if instancias.mm.maximo_alcanzado()==True:
            instancias.hh.valor_actual = instancias.hh.valor_actual+1
        text = '{} : {} : {} : {}'.format(instancias.hh.valor_actual,instancias.mm.valor_actual,instancias.ss.valor_actual,instancias.ms.valor_actual)
        return text

    def restart(self):
        hrs = instancias.hh
        min = instancias.mm
        seg = instancias.ss
        mil = instancias.ms
        mil.valor_actual=0
        seg.valor_actual=0
        min.valor_actual=0
        hrs.valor_actual=0

    def pause(self,estado):
        if estado ==True:
            estado = False
        else:
            estado = True
        return estado
