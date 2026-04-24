import random

class ModeloJuego:
    def __init__(self):
        self.numero = random.randint(1, 10)

    def verificar(self, intento):
        if intento < self.numero:
            return "bajo"
        elif intento > self.numero:
            return "alto"
        else:
            return "correcto"