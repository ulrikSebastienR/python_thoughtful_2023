class Food:
    def __init__(self, name):
        self.name = name
    def awesomeness(self):
        return f"{self.name} tastes unknown"

class Fruit(Food):
    def __init__(self, name):
        self.name = name
    def awesomeness(self):
        return f"{self.name} is sweet"

x = Food("crisp")
s = Food("halwa")
