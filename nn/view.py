class Vista:
    def mostrar_personas(self, personas):
        if personas:
            print("Lista de Personas:")
            for persona in personas:
                print(persona)
        else:
            print("No hay personas para mostrar.")

    def pedir_nombre(self):
        return input("Ingrese el nombre de la persona: ")

    def pedir_edad(self):
        return int(input("Ingrese la edad de la persona: "))

    def mostrar_mensaje(self, mensaje):
        print(mensaje)