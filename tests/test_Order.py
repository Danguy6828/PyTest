import pytest
import sys
from Order import Order
from Drink import Drink, Base, Flavor, Size
from Food import Food, Type, Topping

drink_a = Drink(Base.POKE, {Flavor.BLUE, Flavor.LIME}, 3, Size.MGA)
drink_b = Drink(Base.HILL, {Flavor.CHER}, 2, Size.LRG)
drink_c = Drink(Base.LEAF, {Flavor.STRA, Flavor.MINT, Flavor.LEMN}, 2, Size.SML)

food_a = Food(Type.CDOG, {Topping.KECH, Topping.CHOC})
food_b = Food(Type.FRYS, {Topping.CHIL, Topping.MSTD})
food_c = Food(Type.NACH, {Topping.CRML})

@pytest.fixture
def test_order():
    return Order([drink_a, drink_b])

@pytest.fixture
def test_food_order():
    return Order([food_a, food_c])

@pytest.fixture
def test_mixed_order():
    return Order([food_b, drink_c, food_a])

class TestOrder:
    """Retrieving drinks from an order"""
    def test_get_drink_items(self, test_order):
        assert test_order.get_items() == [drink_a, drink_b]
                
    """Retrieving the amount of drinks in an order"""
    def test_num_drink_items(self, test_order):
        assert test_order.get_num_items() == 2

    """Calculate total for only drinks for an order"""
    def test_get_drink_total(self, test_order):
        assert test_order.get_total() == 9.65

    """Calculate tax for a drink order"""
    def test_calc_drink_tax(self, test_order):
        assert test_order.calc_tax() == 0.70

    """Calculating complete total including tax and drinks"""
    def test_true_drink_total(self, test_order):
        assert test_order.get_true_total() == 10.35

    """Testing addition of a drink to an order"""
    def test_add_drink_item(self, test_order):
        test_order.add_item(drink_c)
        assert test_order.get_items() == [drink_a, drink_b, drink_c]

    """Testing removal of a drink from an order"""
    def test_remove_drink_item(self, test_order):
        test_order.remove_item(1)
        assert test_order.get_items() == [drink_a]

        """Testing if an invalid index returns an exception"""
        with pytest.raises(Exception):
            test_order.remove_item(2)

    """Testing the creation of a drink recipt object with order information"""
    def test_create_drink_recipt(self, test_order):
        recipt = test_order.create_recipt()
        assert recipt.startswith("Drink")

    # Unsure how to write a test on prints
    # def test_print_recipt(self, test_order):
    #     test_order.print_recipt()
    #     assert sys.stdout == test_order.create_recipt()
        
#Test Code for Food in Order
    """Retrieving food from an order"""
    def test_get_food_items(self, test_food_order):
        assert test_food_order.get_items() == [food_a, food_c]
                
    """Retrieving the amount of food in an order"""
    def test_num_food_items(self, test_food_order):
        assert test_food_order.get_num_items() == 2

    """Calculate total for only food for an order"""
    def test_get_food_total(self, test_food_order):
        assert test_food_order.get_total() == 4.9

    """Calculate tax for an order"""
    def test_calc_food_tax(self, test_food_order):
        assert test_food_order.calc_tax() == 0.36

    """Calculating complete total including tax and food"""
    def test_true_food_total(self, test_food_order):
        assert test_food_order.get_true_total() == 5.26

    """Testing addition of food to an order"""
    def test_add_food_item(self, test_food_order):
        test_food_order.add_item(food_b)
        assert test_food_order.get_items() == [food_a, food_c, food_b]

    """Testing removal of food from an order"""
    def test_remove_food_item(self, test_food_order):
        test_food_order.remove_item(1)
        assert test_food_order.get_items() == [food_a]

        """Testing if an invalid index returns an exception"""
        with pytest.raises(Exception):
            test_food_order.remove_item(2)

    """Testing the creation recipt object with order information"""
    def test_create_food_recipt(self, test_food_order):
        recipt = test_food_order.create_recipt()
        assert recipt.startswith("Food")

#Test Code for Mixed Drink and Food Order
    """Retrieving items from an order"""
    def test_get_items(self, test_mixed_order):
        assert test_mixed_order.get_items() == [food_b, drink_c, food_a]
                
    """Retrieving the amount of food in an order"""
    def test_num_items(self, test_mixed_order):
        assert test_mixed_order.get_num_items() == 3

    """Calculate total for only food for an order"""
    def test_get_total(self, test_mixed_order):
        assert test_mixed_order.get_total() == 8.55

    """Calculate tax for an order"""
    def test_calc_tax(self, test_mixed_order):
        assert test_mixed_order.calc_tax() == 0.62

    """Calculating complete total including tax and food"""
    def test_true_total(self, test_mixed_order):
        assert test_mixed_order.get_true_total() == 9.17

    """Testing addition of food to an order"""
    def test_add_item(self, test_mixed_order):
        test_mixed_order.add_item(drink_b)
        assert test_mixed_order.get_items() == [food_b, drink_c, food_a, drink_b]

    """Testing removal of food from an order"""
    def test_remove_item(self, test_mixed_order):
        test_mixed_order.remove_item(1)
        assert test_mixed_order.get_items() == [food_b, food_a]

        """Testing if an invalid index returns an exception"""
        with pytest.raises(Exception):
            test_mixed_order.remove_item(3)

    """Testing the creation recipt object with order information"""
    def test_create_food_recipt(self, test_mixed_order):
        recipt = test_mixed_order.create_recipt()
        assert "Drink" in recipt