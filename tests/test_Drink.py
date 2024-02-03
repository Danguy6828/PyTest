import pytest
from Drink import Drink

@pytest.fixture
def test_drink():
    return Drink('pokeacola', {'blueberry', 'lime'}, 3)

class TestDrink:
    # Retrieving flavors from drink
    def test_get_flavors(self, test_drink):
        assert test_drink.get_flavors() == {'blueberry', 'lime'}

    # Retrieving base from drink
    def test_get_base(self, test_drink):
        assert test_drink.get_base() == 'pokeacola'

    # Retrieving total from drink
    def test_get_total(self, test_drink):
        assert test_drink.get_total() == 3

    # Retrieving total amount of flavors in drink
    def test_get_num_flavors(self, test_drink):
        assert test_drink.get_num_flavors() == 2

    # Setting flavors in drink
    def test_set_flavors(self, test_drink):
        test_drink.set_flavors({'lemon', 'lime'})
        assert test_drink.get_flavors() == {'lemon', 'lime'}

        # Testing if invalid flavor entry triggers exception
        with pytest.raises(Exception):
            test_drink.set_flavors({'soda', 'lime'}) 

    # Adding flavor to drink
    def test_add_flavor(self, test_drink):
        test_drink.add_flavor('mint')
        assert test_drink.get_flavors() == {'blueberry','lime','mint'}

        #Testing if invalid flavor added triggers exception
        with pytest.raises(Exception):
            test_drink.add_flavor('blood')