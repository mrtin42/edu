class Animal():
    def __init__(self,
                 species="undefined",
                 age=0,
                 threat_level="peaceful",
                 hunger_level=0):
        self.species = species
        self.age = age
        self.threat_level = threat_level
        self.hunger_level = hunger_level
    
    def setSpecies(self,
                   species):
        self.species = species
    
    def setAge(self,
               age):
        self.age = age

    def setHungerLevel(self,
                       level):
        self.hunger_level = level

    def setThreatLevel(self):
        if self.hunger_level < 4:
            self.threat_level = "peaceful"
        elif self.hunger_level >=4 and self.hunger_level <= 7:
            self.threat_level = "narky"
        elif self.hunger_level > 7:
            self.threat_level = "aggresive"

hyena = Animal()
hyena.setSpecies("hyena")
hyena.setAge(3)
hyena.setHungerLevel(3)
hyena.setThreatLevel()

print(f"This hyena is feeling {hyena.threat_level}")
print(f"Hunger level: {hyena.hunger_level}")
print(f"Age: {hyena.age}")