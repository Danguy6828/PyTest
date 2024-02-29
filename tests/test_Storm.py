import pytest
from Storm import Storm, Flavs, Topping

@pytest.fixture
def test_storm():
    return Storm(Flavs.MINT, {Topping.COKI, Topping.STOR})

class TestStorm:
    """Retrieving the flavor of Ice Storm object."""
    def test_get_flav(self, test_storm):
        assert test_storm.get_flav() == Flavs.MINT

    """Retrieving toppings from Ice Storm object."""
    def test_get_toppings(self, test_storm):
        assert test_storm.get_toppings() == {Topping.COKI, Topping.STOR}

    """Retrieving the total from an Ice Storm object."""
    def test_get_total(self, test_storm):
        assert test_storm.get_total() == 6.00

    """Setting the toppings of Ice Storm object."""
    def test_set_toppings(self, test_storm):
        test_storm.set_topping({Topping.TNTS, Topping.PECA})
        assert test_storm.get_toppings() == {Topping.TNTS, Topping.PECA}

    """Adding a topping to an Ice Storm object."""
    def test_add_toppings(self, test_storm):
        test_storm.add_toppings(Topping.DIDO)
        assert test_storm.get_toppings() == {Topping.COKI, Topping.STOR, Topping.DIDO}

    """Retrieving amount of toppings from Ice Storm object."""
    def test_get_num_toppings(self, test_storm):
        assert test_storm.get_num_toppings() == 2