class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas

    def promedio(self):
        return sum(self.notas) / len(self.notas)


class ModeloEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def agregar(self, estudiante):
        self.estudiantes.append(estudiante)

    def listar(self):
        return self.estudiantes