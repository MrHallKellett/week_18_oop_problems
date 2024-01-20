# Python Challenges XXIVc

## OOP 3: My Object-Oriented Restaurant

---
	
	Dish: Spaghetti Carbonara
	Ingredients: spaghetti, salt, bacon, egg, cheese, pepper
	Cost to prepare: 89 THB
	Sale price: 445 THB
	
A restaurant system needs to represent its menu using OOP.

- All items on the menu are dishes. All dishes have a name, a weight,  and a list of ingredients. A cost to prepare is calculated by adding up the cost of each ingredient and multiplying this by the weight. A sale price is calculated by multiplying the cost to prepare by 5. The dish class contains a `get_dish_info()` method that needs to return the dish info as shown above.
- Dishes contain ingredients. An ingredient has a name, a cost per 1kg, and a ‘sourced locally’ yes/no flag.
- A Dish needs to be able to `add_ingredient()` and `calculate_cost()`. Calculate cost should be called every time a new ingredient is added.
- Some dishes are salads. Salads have a dressing property which is separate from the list of ingredients. A salad contains a method that outputs TRUE if it can be prepared from locally sourced ingredients only.
- Some dishes are burgers. Burgers have a ‘total calories’ property.
- Each child object should have a constructor method and a ‘getter method’ to access each attribute.
- Using ##comments, explain how polymorphism / inheritance / containment / encapsulation is being used inside your object model.

Inside `test()`, instantiate objects to represent the following:

A cheeseburger is made from beef, onion, bread, lettuce, tomato and cheese. It contains 800 calories. It weight 0.2 kg.

Beef costs 100 THB per kilo. Onion costs 7 THB per kilo. Bread costs 12 THB per kilo. Lettuce costs 10 THB per kilo. Tomato costs 20 THB per kilo. Cheese costs  270 THB per kilo. These ingredients are all sourced locally apart from cheese.

A house salad is made from lettuce, tomato, onion and cheese. It has a honey-mustard dressing, which costs 150 THB per kilo and is not sourced locally. It weighs 0.04 kg.


---

## Extension Task:

A new owner wishes to make the menu more vegetarian friendly.

Each ingredient should now contain an `is_vegetarian` property.

Each dish should also have an `is_vegetarian` property.

Raise a custom exception `NotSuitableForVegetariansError` if a non-vegetarian ingredient is added to a vegetarian dish.