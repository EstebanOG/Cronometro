import time
from crea_unidades import crea as instancias

class cronometro:

    def start():
        text=''
        hrs = instancias.hh
        min = instancias.mm
        seg = instancias.ss
        mil = instancias.ms
        instancias.crea_instancias(instancias)
        #while hrs.valor_actual <= 23:
        #time.sleep(0.1)
        mil.valor_actual=mil.valor_actual+1
        if mil.maximo_alcanzado()==True:
            seg.valor_actual = seg.valor_actual+1
        if seg.maximo_alcanzado()==True:
            min.valor_actual = min.valor_actual+1
        if min.maximo_alcanzado()==True:
            hrs.valor_actual = hrs.valor_actual+1
        text = '{} : {} : {} : {}'.format(hrs.valor_actual,min.valor_actual,seg.valor_actual,mil.valor_actual)
        print(text)
        return text

    def restart():
        hrs = instancias.hh
        min = instancias.mm
        seg = instancias.ss
        mil = instancias.ms
        mil.valor_actual=0
        seg.valor_actual=0
        min.valor_actual=0
        hrs.valor_actual=0

    def pause(estado):
        if estado ==True:
            estado = False
        else:
            estado = True
