# Cree una clase de Bus con:
# Un atributo de max_passengers.
# Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección). Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
# Un método para bajar pasajeros uno por uno (en cualquier orden).

class Person:
    def __init__(self, name):
        self.name = name


class Bus():
    def __init__(self,max_passengers):
        self.max_passengers=max_passengers
        self.passengers=[]

    def load_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
        else:
            print("El bus está lleno")

    def unload_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
        else:
            print(f"{person.name} no va en el bus")


ana = Person("Ana")
luis = Person("Luis")
bus = Bus(3)
bus.load_passenger(ana)
bus.load_passenger(luis)
bus.unload_passenger(ana)
print(len(bus.passengers))
bus.unload_passenger(ana) 