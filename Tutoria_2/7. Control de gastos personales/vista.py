class VistaGastos:

    def mostrar_menu(self):
        print("\n=== Gastos ===")
        print("1. Agregar gasto")
        print("2. Ver resumen")
        print("3. Salir")

    def pedir_opcion(self):
        return input("Opción: ")

    def pedir_datos(self):
        categoria = input("Categoría: ")
        monto = float(input("Monto: "))
        fecha = input("Fecha: ")
        return categoria, monto, fecha

    def mostrar_resumen(self, resumen):
        for cat, total in resumen.items():
            print(f"{cat}: {total:.2f}")