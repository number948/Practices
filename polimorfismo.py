class Animal:
    def Hablar(self):
        pass

class Perro(Animal):
    def Hablar(self):
        print("guau!")

class Gato(Animal):
    def Hablar(self):
        print("miau!")


for animal in Perro(), Gato():
    animal.Hablar()