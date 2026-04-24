class VistaAgenda:

    def mostrar_menu(self):
        print("\n=== Agenda ===")
        print("1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Listar contactos")
        print("4. Salir")

    def pedir_opcion(self):
        return input("Seleccione: ")

    def pedir_datos(self):
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        return nombre, telefono, email

    def pedir_nombre(self):
        return input("Nombre a eliminar: ")

    def mostrar_contactos(self, contactos):
        for c in contactos:
            print(f"{c.nombre} - {c.telefono} - {c.email}")
