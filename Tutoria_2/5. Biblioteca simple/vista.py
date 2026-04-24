class VistaBiblioteca:

    def mostrar_menu(self):
        print("\n=== Biblioteca ===")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Ver libros")
        print("5. Salir")

    def pedir_opcion(self):
        return input("Opción: ")

    def pedir_libro(self):
        return input("Título: "), input("Autor: ")

    def pedir_titulo(self):
        return input("Título: ")

    def mostrar_libros(self, libros):
        for l in libros:
            estado = "Disponible" if l.disponible else "Prestado"
            print(f"{l.titulo} - {l.autor} ({estado})")