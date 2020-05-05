class unidad:

    valor_maximo=0
    valor_actual=0

    def maximo_alcanzado(self):
        if self.valor_actual==self.valor_maximo:
            self.valor_actual=0
            return True

