from enum import Enum

class Flavs(Enum):
    """Enumerator that holds all flavors of Ice Storms."""
    MINT = 'Mint Chocolate Chip'
    COCO = 'Chocolate'
    VANI = 'Vanilla Bean'
    BANA = 'Banana'
    BUPE = 'Butter Pecan'
    SMOR = "S'more"

class Topping(Enum):
    """Enumerator that holds all topping options."""
    CHER = 'Cherry'
    WHIP = 'Whipped Cream'
    CRML = 'Caramel Sauce'
    CHOC = 'Chocolate Sauce'
    STOR = 'Storios'
    DIDO = 'Dig Dogs'
    TNTS = "T&T's"
    COKI = 'Cookie Dough'
    PECA = 'Pecans'

class Storm:
    """Class that creates a Storm object that consists of a flavor and optional toppings."""
    def __init__(self, flav: str, topping: set):
        """Initializes a new object of a Storm Class"""
        self._flav = flav

        if not isinstance(topping, set):
            raise Exception('Please check that topping is a set.')
        
        self._topping = topping

    def get_flav(self):
        """Function to retrieve flavor of Ice Storm object."""
        return self._flav

    def get_toppings(self):
        """Function to retrieve toppings from Ice Storm object."""
        return self._topping
    
    def get_flav_total(self):
        """Function that returns cost depending on flavor."""
        flav_total = 0
        if self._flav in [Flavs.MINT, Flavs.SMOR]:
            flav_total = 4.00
        elif self._flav in [Flavs.COCO, Flavs.VANI]:
            flav_total = 3.00
        elif self._flav in [Flavs.BANA, Flavs.BUPE]:
            flav_total = 3.50
        else:
            raise Exception('Please enter a valid flavor')
        return flav_total
    
    def get_topping_total(self):
        """Function to calculate the total for toppings in an Ice Storm object."""
        topping_total = 0
        for topping in self._topping:
            if topping in [Topping.CHER, Topping.WHIP]:
                topping_total += 0.00
            elif topping in [Topping.CRML, Topping.CHOC, Topping.PECA]:
                topping_total += 0.50
            elif topping in [Topping.STOR, Topping.DIDO, Topping.TNTS, Topping.COKI]:
                topping_total += 1.00
            else:
                raise Exception('Please enter valid toppings')
        return topping_total
    
    def get_total(self):
        """Function to calculate the cost of an Ice Storm object."""
        storm_total = self.get_flav_total() + self.get_topping_total()
        return storm_total
    
    def get_num_toppings(self):
        """Function to count the number of toppings in an Ice Storm object."""
        return len(self._topping)
    
    def set_topping(self, new_topping:set):
        """Function to set toppings in an Ice Storm object."""
        if all(topping in Topping for topping in new_topping):
            self._topping = set(new_topping)
        else:
            raise Exception('Please make sure all toppings selected are valid.')
        
    def add_toppings(self, topping:str):
        """Function to add a topping to an Ice Storm object."""
        if topping in Topping:
            self._topping.add(topping)
        else:
            raise Exception('Please enter a valid topping.')