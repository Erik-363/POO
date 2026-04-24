# modelo.py
class ModeloCalculadora:
    
    def sumar(self, pedir_n1,pedir_n2):
        return pedir_n1 + pedir_n2

    def restar(self, pedir_n1,pedir_n2):
        return pedir_n1 - pedir_n2
    
    def multiplicar(self, pedir_n1,pedir_n2):
        return pedir_n1 * pedir_n2
    
    def dividir(self, pedir_n1,pedir_n2):
        if pedir_n2 == 0:
            raise ValueError("No se puede dividir por cero")
        return pedir_n1 / pedir_n2
    
