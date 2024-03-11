def is_alphabetic_string(str):
    def isfullstop(s):
        return "." in s

    for char in str:
        if char.isalpha() or char.isspace() or isfullstop(char):
            continue
        else:
            return False
    return True

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.__year = year
        
my_car = Car("Porsche", "911 Carrera", 2020)
print(my_car.__year)

name = input()
#print(is_alphabetic_string(name))