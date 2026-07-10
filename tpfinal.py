class Mago:

    def __init__(self, nombre, vida, estadoVarita):
        self.nombre = nombre
        self.vida = vida
        self.estadoVarita = estadoVarita
    
    def mostrarEstado(self):

        print("----- Datos del Mago -----")
        print("Nombre:", self.nombre)

        if self.vida > 0:
            print("Vida:", self.vida)
        else:
            print("Vida: Sin Vida")

        if self.estadoVarita:
            print("Estado: Con Varita")
        else:
            print("Estado: Sin Varita")

class Puro(Mago):

    def __init__(self, nombre, vida, estadoVarita, linaje):
        super().__init__(nombre, vida, estadoVarita)
        self.linaje = linaje


class Impuro(Mago):

    def __init__(self, nombre, vida, estadoVarita, origen):
        super().__init__(nombre, vida, estadoVarita)
        self.origen = origen


mago = Mago("Harry", 100, True)

puro = Puro("Voldemort", 90, True, "Muggles")

impuro = Impuro("Hermione", 90, True, "Muggles")