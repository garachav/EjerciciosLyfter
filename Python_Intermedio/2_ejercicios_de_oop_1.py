# Cree una clase Rectangle que:
# Tenga atributos width y height
# Tenga un método get_area() que retorne el área
# Tenga un método get_perimeter() que retorne el perímetro
# Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado

class Rectangle:
    def __init__(self,width, height):
        self.width = width
        self.height = height
        
    def get_area(self):
        area=self.width*self.height
        return area

    def get_perimeter(self):
        perimeter=self.width*2+self.height*2
        return perimeter

def width():     
    while True:
        try:
            width = int(input("Please, enter the width: "))
            if width <= 0 :
                raise ValueError
            else:
                break
        except ValueError:
            print("There is a negative value, it must be positive, please try again: ")
    return width

def height():
    while True:
        try:
            height = int(input("Please, enter the height: "))
            if height <= 0 :
                raise ValueError
            else:
                break
        except ValueError:
            print("There is a negative value, it must be positive, please try again: ")
    return height

therectangle1 = Rectangle(width(),height())

print(f"The area of the Rectangle 1 is {therectangle1.get_area()}") #75000
print(f"The perimeter of the Rectangle 1 is {therectangle1.get_perimeter()}")#1100
