class Human():
    def __init__(self,
                name="no name",
                age=0,
                nationality="no nationality",
                gender = "no gender"):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.gender = gender
    
    def speak(self):
        print(f'Hi! My name is {self.name}.')


bob = Human("bob",17,"british","male")

print(bob.name)


