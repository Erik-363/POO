class VistaInventario:

    def mostrar_menu(self):
        print("\n=== Inventario ===")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Ver inventario")
        print("4. Salir")

    def pedir_opcion(self):
        return input("Opción: ")

    def pedir_producto(self):
        nombre = input("Nombre: ")
        stock = int(input("Stock: "))
        precio = float(input("Precio: "))
        return nombre, stock, precio

    def pedir_venta(self):
        nombre = input("Producto: ")
        cantidad = int(input("Cantidad: "))
        return nombre, cantidad

    def mostrar_inventario(self, productos):
        for p in productos:
            print(f"{p.nombre} - Stock: {p.stock} - Precio: {p.precio:.2f}")