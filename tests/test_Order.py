import pytest
from Order import Order
from Drink import Drink

@pytest.fixture
def drink_a():
    return Drink('pokeacola', {'blueberry', 'lime'}, 3)

@pytest.fixture
def drink_b():
    return Drink('hill fog', {'cherry'}, 2)

@pytest.fixture
def drink_c():
    return Drink('leaf wine', {'strawberry', 'mint', 'lemon'}, 2)

@pytest.fixture
def test_order():
    return Order([drink_a, drink_b])

class TestOrder:
    # Retrieving drinks from an order
    def test_get_items(self, test_order):
        assert test_order.get_items() == [drink_a, drink_b]
                
    # Retrieving the amount of items in an order
    def test_num_items(self, test_order):
        assert test_order.get_num_items() == 2

    # Calculate total for an order
    def test_get_total(self, test_order):
        assert test_order.get_total() == 5

    # Testing addition of a drink to an order
    def test_add_item(self, test_order):
        test_order.add_item(drink_c)
        assert test_order.get_items() == [drink_a, drink_b, drink_c]

    # Testing removal of a drink from an order
    def test_remove_item(self, test_order):
        test_order.remove_item(1)
        assert test_order.get_items() == [drink_a]

        #Testing if an invalid index returns an exception
        with pytest.raises(Exception):
            test_order.remove_item(2)
