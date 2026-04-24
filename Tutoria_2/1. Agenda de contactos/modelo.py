class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email


class ModeloAgenda:
    def __init__(self):
        self.contactos = []

    def agregar(self, contacto):
        self.contactos.append(contacto)

    def eliminar(self, nombre):
        self.contactos = [c for c in self.contactos if c.nombre != nombre]

    def listar(self):
        return self.contactos