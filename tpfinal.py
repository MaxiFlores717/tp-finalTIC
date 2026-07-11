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
            
    def atacar(self, hechizo, enemigo):
        
        if hechizo == "Expelliarmus":
            enemigo.estadoVarita = False
        elif hechizo == "Avada Kedravra":
            enemigo.vida = 0
        elif hechizo == "Crucio":
            enemigo.vida = enemigo.vida - 30
            

class Puro(Mago):

    def __init__(self, nombre, vida, estadoVarita, linaje):
        super().__init__(nombre, vida, estadoVarita)
        self.linaje = linaje
    def mostrarEstado(self):
        super().mostrarEstado()
        print("Linaje:", self.linaje)
        print("Tipo: Mago Puro")

class Impuro(Mago):

    def __init__(self, nombre, vida, estadoVarita, origen):
        super().__init__(nombre, vida, estadoVarita)
        self.origen = origen
    
    def mostrarEstado(self):
        super().mostrarEstado()
        print("Origen:", self.origen)
        print("Tipo: Mago Impuro")

mago = Mago("Harry", 100, True)
mago.mostrarEstado()

print()

puro = Puro("Draco Malfoy", 90, True, "Malfoy")
puro.mostrarEstado()

print()

impuro = Impuro("Hermione", 90, True, "Padres Muggles")
impuro2 = Impuro("Severus", 90, True, "Mestizo")
impuro.mostrarEstado()

#Ataques
print()
print("------ Ataques -------")
print()
impuro2.atacar("Crucio", impuro)
impuro.atacar("Avada Kedravra", impuro2)
impuro.mostrarEstado()
print()
impuro2.mostrarEstado()
