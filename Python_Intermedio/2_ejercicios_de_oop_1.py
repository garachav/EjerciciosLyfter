# Cree una clase Rectangle que:
# Tenga atributos width y height
# Tenga un método get_area() que retorne el área
# Tenga un método get_perimeter() que retorne el perímetro
# Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado

class Rectangle:
    def __init__(self,width, height):
        if width <= 0 or height <= 0 :
            raise ValueError ("There is a negative value, it must be positive. ")
        self.width = width
        self.height = height



    def get_area(self):
        area=self.width*self.height
        return area

    def get_perimeter(self):
        perimeter=self.width*2+self.height*2
        return perimeter



def side():    
    while True:
        try:
            side = int(input("Please, enter the side value: "))
            if side <= 0 :
                raise ValueError
            else:
                break
        except ValueError:
            print("There is a negative value, it must be positive, please try again: ")
    return side

try:
    therectangle1 = Rectangle(side(),side())
except ValueError as e:
    print(e)

try:
    therectangle2 = Rectangle(4,-5)
except ValueError as e:
    print(e)


print(f"The area of the Rectangle 1 is {therectangle1.get_area()}")
print(f"The perimeter of the Rectangle 1 is {therectangle1.get_perimeter()}")


print(f"The area of the Rectangle 2 is {therectangle2.get_area()}")
print(f"The perimeter of the Rectangle 2 is {therectangle2.get_perimeter()}")
