# Python Challenges XXIV

_Object Oriented Programming_

The Python keyword `class` can be used to define a class - a template for an object that you want to create. An object is a custom data structure with methods that can be called upon to process its data.

A class can _inherit_ its properties and methods from a parent  class (or _super class_). The class that performs **inheritance** is known as a child class (or _sub class_). The `super()` function is used to make a class inherit methods and attributes from its parent.

A child class can overwrite the methods inherited from its base class. This is known as **polymorphism**. This allows you to create objects that are _'same same but different'_ - sharing most of the properties of another object but with a few additional and modified features.

---	
	
	class BaseClass:
	
	   def __init__(self, arg1, arg2):	
	      self.__something = arg1
	      self.__otherthing = arg2
		  
	class ClassName(BaseClass): # inheritance
	
	   def __init__(self, arg1, arg2, arg3):  # polymorphism	
	      super().__init__(arg1, arg2)        # base class constructor arguments
	      self.__child_property_only = arg3
	
The self keyword used in Python object-oriented programming demonstrates **encapsulation**. Variables that are accessible anywhere inside the class have identifiers preceded with the `self.` keyword. In Python programming it is possible to access local object data from _outside_ the object, but this can be prevented by pre-pending a double underscore to the identifier of each variable __ to signify it is **private.** You should write methods that have the sole purpose of retrieving the data from the class via return values. Methods that change data inside a class are known as _setters_. Methods that retrieve data from a class are called _getters_.

---	
	
	class MyClass:
	
	       def __init__(self, name, id):	
	             self.__name = name
	             self.__id = id
				 
	       def get_name(self):	
	             return self.__name
				 
	       def set_id(self, new_id):	
	             self.__id = new_id
				 
	class ChildClass(MyClass):
	
	       def __init__(self, name, id, title): 	
	             super().__init__(name, id)        
	             self.__title = title
				 
	       def get_full_name(self):	
	             return self.__title + " " + self.get_name() # must use getter to access inherited property.
	
---

Work through the OOP past exam paper tasks below, making sure to use 'RUN TESTS'. Get each test to pass before moving on.

You will need access to the _OOP Programming Problems_ worksheet for the full context of the questions.

---

### **TASK 1**

Write the 'X-Games' OOP program as described.

You should implement a `Member` class, a `Competitor` class and an `Official` class. Create an object instance stored in a variable named `BMXJudge` as instructed.

---


### **TASK 2**

Write the 'lending library' OOP program as described.

You should implement a `StockItem` class, a `Book` class and a `CD` class, and create an object instance named `NewBook` as instructed.

---

### **TASK 3**

Write the 'safety deposit box' OOP program as described.

You should implement a `SafetyDepositBox` class with all of the described methods, and an instance of the object stored inside a variable named `ThisSafe` as instructed. Your `Valid()` function should not be contained within the `SafetyDepositBox` class.

Make sure your `StateChange()` function returns a value representing either a) the new state or b) a message relating to the code change / an error.

If you complete the final task (the infinite while loop) this will render the tests unusable - so only do this once everything else is complete.