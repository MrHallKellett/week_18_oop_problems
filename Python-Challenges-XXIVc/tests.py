_D='Tom Yum'
_C='Ba Mee'
_B=False
_A=True
import unittest
from main import*
class UnitTests(unittest.TestCase):
	def test_test_get_dish_info(self):H='Spaghetti Carbonara';G='Pepper';F='Cheese';E='Egg';D='Bacon';C='Salt';B='Spaghetti';A='';expected='Dish: Spaghetti Carbonara\n\n        Ingredients: spaghetti, salt, bacon, egg, cheese, pepper\n\n        Cost to prepare: 6 THB\n\n        Sale price: 30 THB';spaghetti=Ingredient(B,.01,_B);salt=Ingredient(C,.01,_A);bacon=Ingredient(D,.01,_A);egg=Ingredient(E,.01,_A);cheese=Ingredient(F,.01,_B);pepper=Ingredient(G,.01,_A);carbonara=Dish(H,100);carbonara.add_ingredient(spaghetti);carbonara.add_ingredient(salt);carbonara.add_ingredient(bacon);carbonara.add_ingredient(egg);carbonara.add_ingredient(cheese);carbonara.add_ingredient(pepper);given=carbonara.get_dish_info();self.assertEqual(given,expected);expected='Dish: Spaghetti CarbonaraIngredients: spaghetti, salt, bacon, egg, cheese, pepperCost to prepare: 6 THBSale price: 30 THB';spaghetti=Ingredient(B,.01,_B);salt=Ingredient(C,.01,_A);bacon=Ingredient(D,.01,_A);egg=Ingredient(E,.01,_A);cheese=Ingredient(F,.01,_B);pepper=Ingredient(G,.01,_A);carbonara=Dish(H,100);carbonara.add_ingredient(spaghetti);carbonara.add_ingredient(salt);carbonara.add_ingredient(bacon);carbonara.add_ingredient(egg);carbonara.add_ingredient(cheese);carbonara.add_ingredient(pepper);given=carbonara.get_dish_info();given=given.replace(' ',A).replace('\t',A).replace('\n',A).lower();expected=expected.replace(' ',A).replace('\t',A).replace('\n',A).lower();self.assertEqual(given,expected)
	def test_test_make_ingredient(self):noodles=Ingredient(_C,7,_A);noodles=Ingredient(_C,7,_A)
	def test_test_get_name(self):noodles=Ingredient(_C,7,_A);self.assertEqual(noodles.get_name(),_C);noodles=Ingredient(_C,7,_A);self.assertEqual(noodles.get_name(),_C)
	def test_test_get_cost(self):noodles=Ingredient(_C,7,_A);self.assertEqual(noodles.get_cost(),7);noodles=Ingredient(_C,7,_A);self.assertEqual(noodles.get_cost(),7)
	def test_test_get_sourced_locally(self):A='Manchego';cheese=Ingredient(A,655,_B);self.assertEqual(cheese.get_sourced_locally(),_B);cheese=Ingredient(A,655,_B);self.assertEqual(cheese.get_sourced_locally(),_B)
	def test_test_make_dish(self):tom_yum=Dish(_D,300);tom_yum=Dish(_D,300)
	def test_test_add_ingredient(self):A='Lemongrass';lemongrass=Ingredient(A,4,_A);tom_yum=Dish(_D,300);tom_yum.add_ingredient(lemongrass);lemongrass=Ingredient(A,4,_A);tom_yum=Dish(_D,300);tom_yum.add_ingredient(lemongrass)
if __name__=='__main__':unittest.main()