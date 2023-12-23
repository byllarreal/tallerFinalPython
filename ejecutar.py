class Ejecutar:
    def __init__(self, datos,metodo):
        self.datos=datos
        self.metodo=metodo
        self.ejecute()
    
    def ejecute(self):
        return self.metodo(self.datos)

    



    

    
