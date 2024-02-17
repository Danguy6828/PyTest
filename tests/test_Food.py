import pytest
from Food import Food, Type, Topping

@pytest.fixture
def test_food():
    return Food(Type.HDOG, {Topping.CRML, Topping.CHOC})

class TestFood:
    
    def test_get_type(self, test_food):
        assert test_food.get_type() == Type.HDOG

    def test_get_toppings(self, test_food):
        assert test_food.get_toppings() == {Topping.CRML, Topping.CHOC}

    def test_get_total(self, test_food):
        assert test_food.get_total() == 3.30

    def test_set_toppings(self, test_food):
        test_food.set_topping({Topping.CHER, Topping.WHIP})
        assert test_food.get_toppings() == {Topping.CHER, Topping.WHIP}

    def test_add_toppings(self, test_food):
        test_food.add_toppings(Topping.BACN)
        assert test_food.get_toppings() == {Topping.CRML, Topping.CHOC, Topping.BACN}

    def test_get_num_toppings(self, test_food):
        assert test_food.get_num_toppings() == 2
