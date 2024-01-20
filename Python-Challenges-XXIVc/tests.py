import unittest
from main import *


class UnitTests(unittest.TestCase):

  def test_test_get_dish_info(self):
       # Failure message: 

        # I should be able to get the dish info string by calling the appropriate method. Make sure calculate_cost() is implemented!

        expected = """Dish: Spaghetti Carbonara

        Ingredients: spaghetti, salt, bacon, egg, cheese, pepper

        Cost to prepare: 6 THB

        Sale price: 30 THB"""



        spaghetti = Ingredient("Spaghetti", 0.01, False)

        salt = Ingredient("Salt", 0.01, True)

        bacon = Ingredient("Bacon", 0.01, True)

        egg = Ingredient("Egg", 0.01, True)

        cheese = Ingredient("Cheese", 0.01, False)

        pepper = Ingredient("Pepper", 0.01, True)



        carbonara = Dish("Spaghetti Carbonara", 100)

        carbonara.add_ingredient(spaghetti)

        carbonara.add_ingredient(salt)

        carbonara.add_ingredient(bacon)

        carbonara.add_ingredient(egg)

        carbonara.add_ingredient(cheese)

        carbonara.add_ingredient(pepper)



        given = carbonara.get_dish_info()




        self.assertEqual(given, expected)


        expected = """Dish: Spaghetti CarbonaraIngredients: spaghetti, salt, bacon, egg, cheese, pepperCost to prepare: 6 THBSale price: 30 THB"""



        spaghetti = Ingredient("Spaghetti", 0.01, False)

        salt = Ingredient("Salt", 0.01, True)

        bacon = Ingredient("Bacon", 0.01, True)

        egg = Ingredient("Egg", 0.01, True)

        cheese = Ingredient("Cheese", 0.01, False)

        pepper = Ingredient("Pepper", 0.01, True)



        carbonara = Dish("Spaghetti Carbonara", 100)

        carbonara.add_ingredient(spaghetti)

        carbonara.add_ingredient(salt)

        carbonara.add_ingredient(bacon)

        carbonara.add_ingredient(egg)

        carbonara.add_ingredient(cheese)

        carbonara.add_ingredient(pepper)



        given = carbonara.get_dish_info()

        given = given.replace(" ", "").replace("\t", "").replace("\n", "").lower()


        expected = expected.replace(" ", "").replace("\t", "").replace("\n", "").lower()


        self.assertEqual(given, expected)

  def test_test_make_ingredient(self):
        noodles = Ingredient("Ba Mee", 7, True)


        noodles = Ingredient("Ba Mee", 7, True)


  def test_test_get_name(self):
        noodles = Ingredient("Ba Mee", 7, True)

        self.assertEqual(noodles.get_name(), "Ba Mee")


        noodles = Ingredient("Ba Mee", 7, True)

        self.assertEqual(noodles.get_name(), "Ba Mee")


  def test_test_get_cost(self):
        noodles = Ingredient("Ba Mee", 7, True)

        self.assertEqual(noodles.get_cost(), 7)


        noodles = Ingredient("Ba Mee", 7, True)

        self.assertEqual(noodles.get_cost(), 7)

  def test_test_get_sourced_locally(self):

        cheese = Ingredient("Manchego", 655, False)

        self.assertEqual(cheese.get_sourced_locally(), False)


        cheese = Ingredient("Manchego", 655, False)

        self.assertEqual(cheese.get_sourced_locally(), False)

  def test_test_make_dish(self):
        tom_yum = Dish("Tom Yum", 300)


        tom_yum = Dish("Tom Yum", 300)


  def test_test_add_ingredient(self):
        lemongrass = Ingredient("Lemongrass", 4, True)

        tom_yum = Dish("Tom Yum", 300)

        tom_yum.add_ingredient(lemongrass)


        lemongrass = Ingredient("Lemongrass", 4, True)

        tom_yum = Dish("Tom Yum", 300)

        tom_yum.add_ingredient(lemongrass)



