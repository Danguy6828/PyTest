class Drink:
    base = ['water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']
    flavor = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']

    def __init__(self, base: str, flavors: set, total: int):
        self._base = base

        if not isinstance(self._flavors, set):
            raise Exception('Please check that flavors is in the right format.')

        self._flavors = flavors
        self._total = total

    def get_flavors(self):
        return self._flavors
    
    def get_base(self):
        return self._base
    
    def get_total(self):
        return self._total
    
    def get_num_flavors(self):
        return len(self._flavors)

    def set_flavors(self, new_flavors:set):
        if all(flavor in Drink.flavor for flavor in new_flavors):
            self._flavors = set(new_flavors)
        else:
            raise Exception('Please make sure all flavors selected are valid.')

    def add_flavors(self, flavor:str, amount:int):
        if flavor in Drink.flavor:
            self._flavors[flavor] = amount
        else: 
            raise Exception('Please check your entered flavors.')
