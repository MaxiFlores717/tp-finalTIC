import random

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
            print(self.nombre ,"usó Expelliarmus con ", enemigo.nombre)
        elif hechizo == "Avada Kedavra":
            enemigo.vida = 0
            print(self.nombre ,"usó Avada Kedavra con ", enemigo.nombre)
        elif hechizo == "Crucio":
            enemigo.vida -= 30
            print(self.nombre ,"usó Crucio con ", enemigo.nombre)

    # Se agregó un sistema de curación con probabilidad.
    # Cada vez que un mago utiliza el hechizo de curación existe un 30%
    # de probabilidad de recuperar toda la vida. En caso contrario,
    # recupera únicamente 20 puntos de vida.  
    def curar(self):
        if random.random() < 0.30:
            self.vida = 100
            print(self.nombre, "decidió usar la curación completa")
        else:
            self.vida = min(100, self.vida + 20)
            print(self.nombre, "usó la curación parcial (+20 de vida).")
            
    def decidirAccion(self, enemigo):

        numero = random.random()

        # Si el mago tiene poca vida(menor a 40 de vida)
        if self.vida <= 40:
            if numero <= 0.70:
                self.curar()
            else:
                self.atacar("Crucio", enemigo)

        # Si el mago tiene más de 40 de vida
        else:
            if numero <= 0.70:
                self.atacar("Crucio", enemigo)
            else:
                self.curar()

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

mago = Mago("Harry", 30, True)
impuroP = Impuro("Hermione", 90, True, "Padres Muggles")
mago.mostrarEstado()
# mago.decidirAccion(impuroP)

print()

puro = Puro("Draco Malfoy", 90, True, "Malfoy")
puro.mostrarEstado()

print()

impuro = Impuro("Hermione", 90, True, "Padres Muggles")
impuro2 = Impuro("Severus", 40, True, "Mestizo")
impuro.mostrarEstado()
print()
impuro2.mostrarEstado()

print()
print("----- Ataques ------")
print()
puro.decidirAccion(impuro)
print()
impuro.decidirAccion(puro)
# impuro2.atacar("Expelliarmus", puro)
print()
impuro.mostrarEstado()
print()
puro.mostrarEstado()

