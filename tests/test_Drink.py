import pytest
from Drink import Drink

test = Drink('pokeacola', {'blueberry', 'lime'}, 3)

class TestDrink:
    # Retrieving flavors from drink
    def test_get_flavors(self):
        assert test.get_flavors() == {'blueberry', 'lime'}

    # Retrieving base from drink
    def test_get_base(self):
        assert test.get_base() == 'pokeacola'

    # Retrieving total from drink
    def test_get_total(self):
        assert test.get_total() == 3

    # Retrieving total amount of flavors in drink
    def test_get_num_flavors(self):
        assert test.get_num_flavors() == 2

    # Setting flavors in drink
    def test_set_flavors(self):
        test.set_flavors({'lemon', 'lime'})
        assert test.get_flavors() == {'lemon', 'lime'}

        # Testing if invalid flavor entry triggers exception
        with pytest.raises(Exception):
            test.set_flavors({'soda', 'lime'}) 

    # Adding flavor to drink
    def test_add_flavor(self):
        test.add_flavor('mint')
        assert test.get_flavors() == {'lemon','lime','mint'}

        #Testing if invalid flavor added triggers exception
        with pytest.raises(Exception):
            test.add_flavor('blood')