










#https://stackoverflow.com/questions/40898482/defining-method-of-class-in-if-statement
class Food:
    def __init__(self, name):
        self.name = name
    def awesome(self):
        return f"{self.name} tastes unknown"

class Cookie(Food):
    def awesome(self):
        return f"{self.name} is awesome"

x = Cookie("oreo")
y = Food("mango")

#or going through getter and setter
