class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False


class ModeloTareas:
    def __init__(self):
        self.tareas = []

    def agregar(self, tarea):
        self.tareas.append(tarea)

    def completar(self, descripcion):
        for t in self.tareas:
            if t.descripcion == descripcion:
                t.completada = True

    def eliminar(self, descripcion):
        self.tareas = [t for t in self.tareas if t.descripcion != descripcion]

    def listar(self):
        return self.tareas