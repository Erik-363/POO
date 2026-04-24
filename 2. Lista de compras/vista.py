class VistaCompras:

    def mostrar_menu(self):
        print("\n=== Lista de Compras ===")
        print("1. Agregar")
        print("2. Eliminar")
        print("3. Marcar comprado")
        print("4. Ver lista")
        print("5. Salir")

    def pedir_opcion(self):
        return input("Opción: ")

    def pedir_producto(self):
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))
        return nombre, cantidad

    def pedir_nombre(self):
        return input("Nombre: ")

    def mostrar_lista(self, productos):
        for p in productos:
            estado = "ya" if p.comprado else "aun no"
            print(f"{p.nombre} ({p.cantidad}) - {estado}")
