from Drink import Drink, Base, Flavor, Size

class Order:
    """Class that takes in multiple Drink objects to create an Order."""
    def __init__(self, items):
        """Initializes a new object of the Order Class"""
        self._items = items

    def get_items(self):
        """Function to retrieve all Drinks in an Order."""
        return self._items

    def get_num_items(self):
        """Function to count the number of Drinks in a single order."""
        return len(self._items)

    def get_total(self):
        """Function to calculate the totals for only Drinks an order."""
        totals = []
        for item in self._items:
            totals.append(item.get_total())
        total = sum(totals)
        return round(total, 2)

    def add_item(self, item:Drink):
        """Function to add a Drink to an order."""
        self._items.append(item)

    def remove_item(self, index:int):
        """Function to remove a Drink from an order."""
        if index < len(self._items) and index > (-1):
            del self._items[index]
        else:
            raise Exception('Please enter a valid index.')
        
    def calc_tax(self):
        """Function to calculate the tax of an order."""
        tax = self.get_total() * 0.0725
        return round(tax, 2)
    
    def get_true_total(self):
        """Function that calculates the complete total of the order including tax."""
        total = self.get_total() + self.calc_tax()
        return round(total, 2)

    def create_recipt(self):
        """Function the send an order as raw data to a 'recipt'."""
        recipt = ''
        for index, item in enumerate(self._items, start=1):
            list_flavor = []
            for flavor in item.get_flavors():
                list_flavor.append(f'{flavor.value}')
            recipt += (f'Drink: #{index}:\n'
                       f'Base: {item.get_base().value}\n'
                       f'Flavor(s):{list_flavor}\n'
                       f'Cost: ${item.get_total()}\n'
                       '\n')
        recipt += (f'Tax: ${self.calc_tax()}\n'
                   f'Total: ${self.get_true_total()}\n')
        return recipt
    
    def print_recipt(self):
        recipt = self.create_recipt()
        print(recipt)