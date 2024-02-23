from enum import Enum

class Type(Enum):
    """Enumerator that holds all types of food."""
    HDOG = 'Hotdog'
    CDOG = 'Corndog'
    ICRM = 'Ice Cream'
    ONRI = 'Onion Rings'
    FRYS = 'French Fries'
    TATO = 'Tator Tots'
    NACH = 'Nacho Chips'

class Topping(Enum):
    """Enumerator that holds all topping options."""
    CHER = 'Cherry'
    WHIP = 'Whipped Cream'
    CRML = 'Caramel Sauce'
    CHOC = 'Chocolate Sauce'
    CHES = 'Nacho Cheese'
    CHIL = 'Chili'
    BACN = 'Bacon Bits'
    KECH = 'Ketchup'
    MSTD = 'Mustard'

class Food:
    """Class that creates a Food object that consists of a type and optional toppings."""
    def __init__(self, type: str, topping: set):
        """Initializes a new object of a Food Class"""
        self._type = type

        if not isinstance(topping, set):
            raise Exception('Please check that topping is a set.')
        
        self._topping = topping

    def get_type(self):
        """Function to retrieve type of food from Food object."""
        return self._type

    def get_toppings(self):
        """Function to retrieve toppings from a Food object."""
        return self._topping
    
    def get_type_total(self):
        """Function that returns cost depending on Type."""
        type_total = 0
        if self._type == Type.HDOG:
            type_total = 2.30
        elif self._type == Type.CDOG:
            type_total = 2.00
        elif self._type == Type.ICRM:
            type_total = 3.00
        elif self._type == Type.ONRI:
            type_total = 1.75
        elif self._type == Type.FRYS:
            type_total = 1.50
        elif self._type == Type.TATO:
            type_total = 1.70
        elif self._type == Type.NACH:
            type_total = 1.90
        else:
            raise Exception('Please enter a valid food item')
        return type_total
    
    def get_topping_total(self):
        """Function to calculate the total for toppings in a Food object."""
        topping_total = 0
        for topping in self._topping:
            if topping in [Topping.CHER, Topping.WHIP, Topping.KECH, Topping.MSTD]:
                topping_total += 0.00
            elif topping in [Topping.CRML, Topping.CHOC]:
                topping_total += 0.50
            elif topping in [Topping.CHES, Topping.BACN]:
                topping_total += 0.30
            elif topping == Topping.CHIL:
                topping_total += 0.60
            else:
                raise Exception('Please enter valid toppings')
        return topping_total
    
    def get_total(self):
        """Function to calculate the cost of a Food object."""
        food_total = self.get_type_total() + self.get_topping_total()
        return food_total
    
    def get_num_toppings(self):
        """Function to count the number of toppings in a Food object."""
        return len(self._topping)
    
    def set_topping(self, new_topping:set):
        """Function to set toppings in a Food object."""
        if all(topping in Topping for topping in new_topping):
            self._topping = set(new_topping)
        else:
            raise Exception('Please make sure all toppings selected are valid.')
        
    def add_toppings(self, topping:str):
        """Function to add a topping to a Food object."""
        if topping in Topping:
            self._topping.add(topping)
        else:
            raise Exception('Please enter a valid topping.')