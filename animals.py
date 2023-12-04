class Moving:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError




class Animal(Moving):
    def voice(self):
        raise NotImplementedError


class Transport(Moving):
    def launch(self):
        raise NotImplementedError


class Duck(Animal):
    def voice(self):
        print(f"{self.name} makes Krya")

    def move(self):
        print(f"{self.name} swims")


class Tiger(Animal):
    def voice(self):
        print(f"{self.name} makes Rrrr")

    def move(self):
        print(f"{self.name} runs")


class Car(Transport):
    def launch(self):
        print(f"{self.name} starts")

    def move(self):
        print(f"{self.name} goes")


Duck = Duck("Duck")
Duck.voice()
Duck.move()
Tiger = Tiger("tiger")
Tiger.voice()
Tiger.move()
Car = Car("Car")
Car.launch()
Car.move()
