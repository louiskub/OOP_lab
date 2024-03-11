class IceCream:
    def __init__(self, flavor):
        self.flavor = flavor

        
class Customer:
    def __init__(self, flavor, package, quantity, price):
        self.flavor = flavor
        self.package = package
        self.quantity = quantity
        self.price = price
        
flavors = ("Chocolate", "Strawberry", "Sherbet", "Vaniila", "Oreo", "Coffee", "Rainbow", "Blueberry")
ice_cream = [IceCream(flavors[i]) for i in range(8)] 