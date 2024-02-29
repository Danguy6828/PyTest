import pytest
from Order import Order
from Drink import Drink, Base, Flavor, Size
from Food import Food, Type, Topping
from Storm import Storm, Flavs, Topping as Topp

drink_a = Drink(Base.POKE, {Flavor.BLUE, Flavor.LIME}, 3, Size.MGA)
drink_b = Drink(Base.HILL, {Flavor.CHER}, 2, Size.LRG)
drink_c = Drink(Base.LEAF, {Flavor.STRA, Flavor.MINT, Flavor.LEMN}, 2, Size.SML)

food_a = Food(Type.CDOG, {Topping.KECH, Topping.CHOC})
food_b = Food(Type.FRYS, {Topping.CHIL, Topping.MSTD})
food_c = Food(Type.NACH, {Topping.CRML})

storm_a = Storm(Flavs.VANI, {Topp.COKI, Topp.CHOC})
storm_b = Storm(Flavs.BUPE, {Topp.PECA, Topp.CHER})
storm_c = Storm(Flavs.SMOR, {Topp.CRML, Topp.DIDO})

@pytest.fixture
def test_order():
    return Order([drink_a, drink_b])

@pytest.fixture
def test_food_order():
    return Order([food_a, food_c])

@pytest.fixture
def test_storm_order():
    return Order([storm_b, storm_c])

@pytest.fixture
def test_mixed_order():
    return Order([food_b, drink_c, storm_a])

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

#Test Code for Ice Storm in Order
    """Retrieving Ice Storm from an order"""
    def test_get_storm_items(self, test_storm_order):
        assert test_storm_order.get_items() == [storm_b, storm_c]
                
    """Retrieving the amount of Ice Storms in an order"""
    def test_num_storm_items(self, test_storm_order):
        assert test_storm_order.get_num_items() == 2

    """Calculate total for only Ice Storms for an order"""
    def test_get_storm_total(self, test_storm_order):
        assert test_storm_order.get_total() == 9.50

    """Calculate tax for an order"""
    def test_calc_storm_tax(self, test_storm_order):
        assert test_storm_order.calc_tax() == 0.69

    """Calculating complete total including tax and Ice Storms"""
    def test_true_storm_total(self, test_storm_order):
        assert test_storm_order.get_true_total() == 10.19

    """Testing addition of an Ice Storm to an order"""
    def test_add_storm_item(self, test_storm_order):
        test_storm_order.add_item(storm_a)
        assert test_storm_order.get_items() == [storm_b, storm_c, storm_a]

    """Testing removal of an Ice Storm from an order"""
    def test_remove_storm_item(self, test_storm_order):
        test_storm_order.remove_item(1)
        assert test_storm_order.get_items() == [storm_b]

        """Testing if an invalid index returns an exception"""
        with pytest.raises(Exception):
            test_storm_order.remove_item(2)

    """Testing the creation recipt object with order information"""
    def test_create_storm_recipt(self, test_storm_order):
        recipt = test_storm_order.create_recipt()
        assert recipt.startswith("Ice Storm")

#Test Code for Mixed Drink, Food, and Ice Storm Order
    """Retrieving items from an order"""
    def test_get_items(self, test_mixed_order):
        assert test_mixed_order.get_items() == [food_b, drink_c, storm_a]
                
    """Retrieving the amount of items in an order"""
    def test_num_items(self, test_mixed_order):
        assert test_mixed_order.get_num_items() == 3

    """Calculate total for only items for an order"""
    def test_get_total(self, test_mixed_order):
        assert test_mixed_order.get_total() == 10.55

    """Calculate tax for an order"""
    def test_calc_tax(self, test_mixed_order):
        assert test_mixed_order.calc_tax() == 0.76

    """Calculating complete total including tax and items"""
    def test_true_total(self, test_mixed_order):
        assert test_mixed_order.get_true_total() == 11.31

    """Testing addition of an item to an order"""
    def test_add_item(self, test_mixed_order):
        test_mixed_order.add_item(drink_b)
        assert test_mixed_order.get_items() == [food_b, drink_c, storm_a, drink_b]

    """Testing removal of an item from an order"""
    def test_remove_item(self, test_mixed_order):
        test_mixed_order.remove_item(1)
        assert test_mixed_order.get_items() == [food_b, storm_a]

        """Testing if an invalid index returns an exception"""
        with pytest.raises(Exception):
            test_mixed_order.remove_item(3)

    """Testing the creation recipt object with order information"""
    def test_create_food_recipt(self, test_mixed_order):
        recipt = test_mixed_order.create_recipt()
        assert "Ice Storm" in recipt