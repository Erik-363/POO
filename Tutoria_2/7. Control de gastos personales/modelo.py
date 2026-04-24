class Gasto:
    def __init__(self, categoria, monto, fecha):
        self.categoria = categoria
        self.monto = monto
        self.fecha = fecha


class ModeloGastos:
    def __init__(self):
        self.gastos = []

    def agregar(self, gasto):
        self.gastos.append(gasto)

    def resumen_por_categoria(self):
        resumen = {}
        for g in self.gastos:
            if g.categoria in resumen:
                resumen[g.categoria] += g.monto
            else:
                resumen[g.categoria] = g.monto
        return resumen