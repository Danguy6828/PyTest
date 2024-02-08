from enum import Enum
class Base(Enum):
    """
    Enumerator that holds all bases of a drink
    """
    WATR = 'Water'
    SBRI = 'Sbrite'
    POKE = 'Pokeacola'
    SALT = 'Mr. Salt'
    HILL = 'Hill Fog'
    LEAF = 'Leaf Wine'

class Flavor(Enum):
    """
    Enumerator that holds all flavors of a drink
    """
    LEMN = 'Lemon'
    CHER = 'Cherry'
    STRA = 'Strawberry'
    MINT = 'Mint'
    BLUE = 'Blueberry'
    LIME = 'Lime'

class Size(Enum):
    """
    Enumerator that holds all sizes of a drink
    """
    SML = 'Small'
    MED = 'Medium'
    LRG = "Large"
    MGA = "Mega"

class Drink:
    """Class that creates a Drink object that consists of different values."""
    def __init__(self, base: str, flavors: set, total: float, size: str):
        """Initializes a new object of the Drink Class"""
        self._base = base

        if not isinstance(flavors, set):
            raise Exception('Please check that flavors is a set.')

        self._flavors = flavors
        self._total = total
        self._size = size

    def get_flavors(self):
        """Function to retrieve flavors from a Drink object."""
        return self._flavors
    
    def get_base(self):
        """Function to retrieve base from a Drink object."""
        return self._base
    
    def get_total(self):
        """Function to calculate the cost of a Drink object."""
        drink_total = 0
        before_total = self._total + (len(self._flavors)*0.15)
        if self._size == Size.SML:
            drink_total = before_total + 1.50
        elif self._size == Size.MED:
            drink_total = before_total + 1.75
        elif self._size == Size.LRG:
            drink_total = before_total + 2.05
        elif self._size == Size.MGA:
            drink_total = before_total + 2.15
        else:
            raise Exception('Please enter a valid size')
        return round(drink_total, 2)
    
    def get_num_flavors(self):
        """Function to retrieve the amount flavors from a Drink object."""
        return len(self._flavors)
    
    def get_size(self):
        """Function to retrieve size of a Drink object."""
        return self._size

    def set_flavors(self, new_flavors:set):
        """Function to set the flavors a Drink object."""
        if all(flavor in Flavor for flavor in new_flavors):
            self._flavors = set(new_flavors)
        else:
            raise Exception('Please make sure all flavors selected are valid.')

    def add_flavor(self, flavor:str):
        """Function to add flavors to a Drink object."""
        if flavor in Flavor:
            self._flavors.add(flavor)
        else: 
            raise Exception('Please enter a valid flavor.')

    def set_size(self, size:Size):
        """Function to set the size of a Drink object."""
        if size in Size:
            self._size = size
        else:
            raise Exception('Please enter a valid size.')
            