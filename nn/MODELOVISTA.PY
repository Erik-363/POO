# Modelo
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def obtener_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Vista
class PersonaView:
    def mostrar_informacion(self, info):
        print(info)

# Controlador
class PersonaController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def mostrar_persona(self):
        info = self.modelo.obtener_informacion()
        self.vista.mostrar_informacion(info)

# Uso
persona = Persona("Juan", 30)
vista = PersonaView()
controlador = PersonaController(persona, vista)

controlador.mostrar_persona() 