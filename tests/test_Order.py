import pytest
import sys
from Order import Order
from Drink import Drink, Base, Flavor, Size


# Fixtures that caused an issue when used
# @pytest.fixture
# def drink_a():
#     return Drink('pokeacola', {Flavor.BLUE, Flavor.LIME}, 3)

# @pytest.fixture
# def drink_b():
#     return Drink(Base.HILL, {Flavor.CHER}, 2)

# @pytest.fixture
# def drink_c():
#     return Drink(Base.LEAF, {Flavor.STRA, Flavor.MINT, Flavor.LEMN}, 2)

drink_a = Drink(Base.POKE, {Flavor.BLUE, Flavor.LIME}, 3, Size.MGA)
drink_b = Drink(Base.HILL, {Flavor.CHER}, 2, Size.LRG)
drink_c = Drink(Base.LEAF, {Flavor.STRA, Flavor.MINT, Flavor.LEMN}, 2, Size.SML)

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

    # Calculate total for only drinks for an order
    def test_get_total(self, test_order):
        assert test_order.get_total() == 9.65

    # Calculate tax for an order
    def test_calc_tax(self, test_order):
        assert test_order.calc_tax() == 0.70

    # Calculating complete total including tax and drinks
    def test_true_total(self, test_order):
        assert test_order.get_true_total() == 10.35

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

    # Testing the creation recipt object with order information
    def test_create_recipt(self, test_order):
        recipt = test_order.create_recipt()
        assert recipt.startswith("Drink")

    # Unsure how to write a test on prints
    # def test_print_recipt(self, test_order):
    #     test_order.print_recipt()
    #     assert sys.stdout == test_order.create_recipt()