import pytest
from Drink import Drink, Base, Flavor, Size

@pytest.fixture
def test_drink():
    return Drink(Base.POKE, {Flavor.BLUE, Flavor.LIME}, 3, Size.LRG)

class TestDrink:
    """Retrieving flavors from drink."""
    def test_get_flavors(self, test_drink):
        assert test_drink.get_flavors() == {Flavor.BLUE, Flavor.LIME}

    """Retrieving base from drink."""
    def test_get_base(self, test_drink):
        assert test_drink.get_base() == Base.POKE

    """Retrieving total from drink."""
    def test_get_total(self, test_drink):
        assert test_drink.get_total() == 5.35

    """Retrieving total amount of flavors in drink."""
    def test_get_num_flavors(self, test_drink):
        assert test_drink.get_num_flavors() == 2

    """Setting flavors in drink."""
    def test_set_flavors(self, test_drink):
        test_drink.set_flavors({Flavor.LEMN, Flavor.LIME})
        assert test_drink.get_flavors() == {Flavor.LEMN, Flavor.LIME}

        """Testing if invalid flavor entry triggers exception."""
        with pytest.raises(Exception):
            test_drink.set_flavors({'soda', Flavor.LEME}) 

    """Adding flavor to drink."""
    def test_add_flavor(self, test_drink):
        test_drink.add_flavor(Flavor.MINT)
        assert test_drink.get_flavors() == {Flavor.BLUE, Flavor.LIME, Flavor.MINT}

        """esting if invalid flavor added triggers exception."""
        with pytest.raises(Exception):
            test_drink.add_flavor('blood')

    """Retrieving size from drink."""
    def test_get_size(self, test_drink):
        assert test_drink.get_size() == Size.LRG

    """Setting size of drink."""
    def test_set_size(self, test_drink):
        test_drink.set_size(Size.MGA) 
        assert test_drink.get_size() == Size.MGA