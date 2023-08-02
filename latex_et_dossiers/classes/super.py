class Person:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    def show(self):
        return f"{self.name} is {self.sex}"

class Citizen(Person):
    def __init__(self, name, sex, country):
        super().__init__(name, sex)
        self.country = country
    def nationality(self):
        return f"{self.name} is {self.sex} from {self.country}"
    def details(self):
        super().show()

p = Person("aimata", "f")
f = Citizen("Zidane", "m", "Tahiti")
