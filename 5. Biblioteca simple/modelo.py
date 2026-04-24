class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True


class ModeloBiblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        self.libros.append(libro)

    def prestar(self, titulo):
        for l in self.libros:
            if l.titulo == titulo:
                l.disponible = False

    def devolver(self, titulo):
        for l in self.libros:
            if l.titulo == titulo:
                l.disponible = True

    def listar(self):
        return self.libros