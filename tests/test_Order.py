import pytest
from Order import Order
from Drink import Drink

drink_a = Drink('pokeacola', {'blueberry', 'lime'}, 3)
drink_b = Drink('hill fog', {'cherry'}, 2)
drink_c = Drink('leaf wine', {'strawberry', 'mint', 'lemon'}, 2)

test = Order([drink_a, drink_b])

class TestOrder:
    # Retrieving drinks from an order
    def test_get_items(self):
        assert test.get_items() == [drink_a, drink_b]
                
    # Retrieving the amount of items in an order
    def test_num_items(self):
        assert test.get_num_items() == 2

    # Calculate total for an order
    def test_get_total(self):
        assert test.get_total() == 5

    # Testing addition of a drink to an order
    def test_add_item(self):
        test.add_item(drink_c)
        assert test.get_items() == [drink_a, drink_b, drink_c]

    # Testing removal of a drink from an order
    def test_remove_item(self):
        test.remove_item(1)
        assert test.get_items() == [drink_a, drink_c]

        #Testing if an invalid index returns an exception
        with pytest.raises(Exception):
            test.remove_item(2)
