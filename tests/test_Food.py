import pytest
from Food import Food, Type, Topping

@pytest.fixture
def test_food():
    return Food(Type.HDOG, {Topping.CRML, Topping.CHOC})

class TestFood:
    """Retrieving type of food from object."""
    def test_get_type(self, test_food):
        assert test_food.get_type() == Type.HDOG

    """Retrieving toppings from food object."""
    def test_get_toppings(self, test_food):
        assert test_food.get_toppings() == {Topping.CRML, Topping.CHOC}
    
    """Retrieving the total from a food object."""
    def test_get_total(self, test_food):
        assert test_food.get_total() == 3.30

    """Setting the toppings of a food object."""
    def test_set_toppings(self, test_food):
        test_food.set_topping({Topping.CHER, Topping.WHIP})
        assert test_food.get_toppings() == {Topping.CHER, Topping.WHIP}

    """Adding toppings to an existing food object."""
    def test_add_toppings(self, test_food):
        test_food.add_toppings(Topping.BACN)
        assert test_food.get_toppings() == {Topping.CRML, Topping.CHOC, Topping.BACN}

    """Retrieving the number of toppings in a food object."""
    def test_get_num_toppings(self, test_food):
        assert test_food.get_num_toppings() == 2
