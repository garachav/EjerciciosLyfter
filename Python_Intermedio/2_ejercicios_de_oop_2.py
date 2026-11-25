# Cree una clase base Animal y dos clases hijas Dog y Cat:
# Animal debe tener nombre y método speak() que retorne "Hace un sonido"
# Dog debe sobrescribir speak() para decir "Guau"
# Cat debe sobrescribir speak() para decir "Miau"

class Animal():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return "Hace un sonido"
    
    
class Dog(Animal):
    def speak(self):
        return "Guau"
    
class Cat(Animal):
    def speak(self):
        return "Miau"

dog1= Dog("Firulais")
print(dog1.speak())

cat1=Cat("Minino")
print(cat1.speak())

cow1 = Animal("Hamburgruesa")
print(cow1.speak())