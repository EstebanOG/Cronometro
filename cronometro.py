import time
from crea_unidades import crea as instancias

class cronometro:

    stop=False        
    def start(self):    
        instancias.crea_instancias(instancias)          
        while self.stop != True:
            print(instancias.hh.valor_actual,":",instancias.mm.valor_actual,":",instancias.ss.valor_actual,":",instancias.ms.valor_actual)
            time.sleep(0.1)
            instancias.ms.valor_actual=instancias.ms.valor_actual+1
            if instancias.ms.maximo_alcanzado()==True:
                instancias.ss.valor_actual = instancias.ss.valor_actual+1 
            if instancias.ss.maximo_alcanzado()==True:
                instancias.mm.valor_actual = instancias.mm.valor_actual+1 
            if instancias.mm.maximo_alcanzado()==True:
                instancias.hh.valor_actual = instancias.hh.valor_actual+1 

    def restart(self):
        instancias.ms.valor_actual=0
        instancias.ss.valor_actual=0
        instancias.mm.valor_actual=0
        instancias.hh.valor_actual=0
        self.start()
