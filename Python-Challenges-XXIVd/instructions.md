# Python Challenges XXIVd

_OOP4 : Past paper questions_


---

### **TASK 1**

There are 1000 students at a university. They will each require a printing account.

Students need to buy printing credits that will be added to their account. Each page printed uses one printing credit. The university needs software to keep track of the number of printing credits each student has in their account. The university has decided to implement the software using object-oriented programming (OOP).


	PrintAccount
	-------------------------------------------------------
	FirstName : STRING // parameter sent to Constructor()
	LastName  : STRING // parameter sent to Constructor()
	PrintID   : STRING // parameter sent to Constructor()
	Credits   : INTEGER // initialised to 50
	-------------------------------------------------------
	Constructor()   // instantiates an object of the PrintAccount class,
	                // and assigns initial values to the attributes
	GetName()       // returns FirstName and LastName concatenated
	                // with a space between them
	GetPrintID()    // returns PrintID
	SetFirstName()  // sets the FirstName for a student
	SetLastName()   // sets the LastName for a student
	SetPrintID()    // sets the PrintID for a student
	AddCredits()    // increases the number of credits for a student
	RemoveCredits() // removes credits from a student account

The diagram above shows the design for the class `PrintAccount`. This includes the attributes and methods.

---
1\. Write program code for the `PrintAccount` class and its Constructor() method.

---
2\.  Write program code for the `SetFirstName()` method.

---
3\.  Write program code for the `GetName()` method.

---
4\.  The method `AddCredits()` calculates the number of printing credits a student buys and adds the printing credits to the student’s account

• Credits cost $1 for 25 credits.

• If a student buys $20 or more of credits in a single payment, they receive an extra 50 credits.

• If a student buys between $10 and $19 (inclusive) of credits in a single payment, they receive an extra 25 credits.

Payment from a student is stored in the variable `MoneyInput`. This is passed as a parameter.

Write program code for `AddCredits().` Use constants for the values that do not change.

---
5\.  A global array, `StudentAccounts`, stores 1000 instances of `PrintAccount`.

Write pseudocode to declare the array `StudentAccounts`.

_Answer this question by creating a variable named `StudentAccountsInPseudo` and store the answer as a string._

---
6\. The main program has a function, `CreateID()`, that:

• takes the first name and last name as parameters

• creates `PrintID` that is a concatenation of:

    ◦ the first three letters of the first name in lower case

    ◦ the first three letters of the last name in lower case

    ◦ the character ‘1’for example, the name Bill Smith would produce "bilsmi1"

• checks if the `PrintID` created already exists in the global array `StudentAccounts`:

    ◦ If `PrintID` does not exist, it creates an instance of `PrintAccount` in the next free index in `StudentAccounts`.

    ◦ If `PrintID` does exist, the number is incremented until a unique ID is created, for example, `"bilsmi2"`.

It then creates an instance of `PrintAccount` in the next free index in `StudentAccounts`.

The global variable `NumberStudents` stores the number of print accounts that have currently been created.

The function should return the value of `StudentAccounts` once it has been updated.

Write program code for the procedure `CreateID()`.

---

---

### **TASK 2**

Players complete one game to place them into a category for the competition. The games club wants to implement a program to place players into the correct category. The programmer has decided to use object-oriented programming (OOP).

The highest score that can be achieved in the game is 150. Any score less than 50 will not

qualify for the competition. Players will be placed in a category based on their score.

The following diagram shows the design for the class Player. This includes the properties

and methods.

	# Player class
	#---------------------------------------------------------------------
	# Score    : INTEGER // initialised to 0
	# Category : STRING // "Beginner", "Intermediate", "Advanced" or "Not Qualified"

	             initialised to "Not Qualified"

	# PlayerID : STRING // initialised with the parameter InputPlayerID
	#---------------------------------------------------------------------
	# Create()      // method to create and initialise an object using
	                // language-appropriate constructor
	# SetScore()    // checks that the Score parameter has a valid value
	                // if so, assigns it to Score

	# SetCategory() // sets Category based on player’s Score
	# SetPlayerID() // allows a player to change their PlayerID
	                // validates the new PlayerID
	# GetScore()    // returns Score
	# GetCategory() // returns Category
	# GetPlayerID() // returns PlayerID

The constructor receives the parameter `InputPlayerID` to create the `PlayerID`.

Other properties are initialised as instructed in the class diagram.

---
Write program code for the `Create()` constructor method.

---
Write program code for the following three get methods.

	GetScore()
	GetCategory()
	GetPlayerID()
---
The method `SetPlayerID()` asks the user to input the new player ID and reads in this value.

It checks that the length of the `PlayerID` is less than or equal to 15 characters and

greater than or equal to 4 characters. If the input is valid, it sets this as the `PlayerID`,

otherwise it loops until the player inputs a valid `PlayerID`.

Use suitable input and output messages.

Write program code for `SetPlayerID()`.

---
The method `SetScore()` checks that its INTEGER parameter `ScoreInput` is valid. If

it is valid, it is then set as Score. A valid `ScoreInput` is greater than or equal to 0 and

less than or equal to 150.

If the `ScoreInput` is valid, the method sets `Score` and returns `TRUE`.

If the `ScoreInput` is not valid, the method does not set Score, displays an error message, and it returns `FALSE`.

Write program code for `SetScore(ScoreInput : INTEGER)`.

---
Write program code for the method `SetCategory().` Use the properties and methods in the original class definition.

Players will be placed in one of the following categories.

	Category      Criteria
	-------------------------
	Advanced      Score is greater than 120
	Intermediate  Score is greater than 80 and less than or equal to 120
	Beginner      Score is greater than or equal to 50 and less than or equal to 80
	Not Qualified Score is less than 50

---
Joanne has played the first game to place her in a category for the competition.

The function `CreatePlayer()` performs the following tasks.

• allows the player ID and score to be input with suitable prompts

• creates an instance of `Player` with the identifier `JoannePlayer`

• sets the score for the object

• sets the category for the object

• outputs the category for the object

• returns the newly created `Player` object back to the calling point.

Write program code for the `CreatePlayer()` function.


---------------------------------------------------------------------------------


---

### **TASK 3**

Kendra collects books. She is writing a program to store and analyse information about her books.

Her program stores information about each book as a record. The following table shows the

information that will be stored about each book.

	Field name    Description
	---------------------------------------
	Title         The title of the book
	Author        The first listed author of the book
	ISBN          13-digit code that uniquely identifies the book,

	              for example:

	              "0081107546738"
	Fiction       If the book is fiction (TRUE) or non-fiction (FALSE)

	LastRead      The date when Kendra last read the book

(a) Write Python code to declare an Abstract Data Type (ADT) named `Book`, to store the

information in the table.

	----------------------------------------------------------------------------------


---

### **TASK 4**

A game uses a set of cards. Each card has a number (between 0 and 9 inclusive) and a shape

("square", "triangle" or "circle").

The game is written using object-oriented programming.

The class, `Card`, has the private properties:

	      `• Number
	    `• Shape
and the methods:

	    `• Constructor()
	    `• GetNumber()
	    `• GetShape()
The purpose of each method in the class `Card` is given in the following table.

	Method        Purpose
	Constructor() Takes a number and a shape as parameters
	              Checks that the number and the shape are valid and:
	               • either assigns the parameters to Number and Shape
	               • or raises an error.
	GetNumber()   A public method that returns the number for that card.

	GetShape()    A public method that returns the shape for that card.

---
Write program code for the `Constructor()` method.

_Because an instance cannot be created if the input values are invalid, a while loop / data validation is NOT appropriate for this task. Instead, you should create two custom Exception classes and raise them when needed:_ `InvalidNumberError` _and_ `InvalidShapeError`

---
Write program code for the `GetNumber()` method.

---
A card, `OneS`, has the value 1 for `Number` and the value "square" for `Shape`.

Write program code to instantiate an instance of `Card` for `OneS`.

---
The game has a function, `Compare()` that takes two cards as parameters and compares

them.

If the cards are identical, the function outputs `"SNAP"` and returns `−1`. If they are not identical, and the card numbers are different, it returns the Number of the card with the higher value or, the Number for the cards if they are the same.

Write program code for the `Compare()` function.

	----------------------------------------------------------------------------------


---

### **TASK 5**

A computer game is being developed using object-oriented programming. The following image is a screenshot from the game.

There are scenery elements and animated elements. The player’s character is one of the animated elements.

Each game element has the attributes:

	Attribute     Description                           Example value
	PositionX     The x coordinate of the game element. 92
	PositionY     The y coordinate of the game element. 106
	Width         The width of the game element.        150
	Height        The height of the game element.       200
	ImageFilename The filename of the image file for    GameElementFrame1.png

	              the game element.

Each game element has a method, `GetDetails()` that returns a string containing all the

element’s attributes.

The player’s character is one of a number of animated elements. All animated elements have the attributes:

	Attribute       Description                            Example value
	AnimationFrames Frames per second                      60
	Direction       A string giving the direction the      "Left"
	                object is travelling in.
	Strength        A value for the strength that          2000

	                indicates the power of the object.
	Health          A value for the health that indicates  100

	                the health of the object.

The player’s character can either move left or right, or jump.

---
Write program code to define the `GameElement` class.

---
The `Scenery()` class has two attributes, `CauseDamage` and `DamagePoints`.

If the attribute `CauseDamage` is `TRUE`, then the scenery element can cause damage.

The method `GiveDamagePoints()` checks whether the object can cause damage. If the

object can cause damage, the method returns the integer value of the `DamagePoints`

attribute.

Write program code for the Scenery class.

---
A new scenery object, `GiftBox`, is to be created.

(i) The attributes of `GiftBox` are as follows:

	Attribute     Value
	PositionX     150
	PositionY     150
	Width         50
	Height        75
	ImageFilename "box.png"
	CauseDamage   TRUE
	DamagePoints  50

Write program code to create an instance of `GiftBox`.

---
An additional method, `GetScenery()`, returns all the attributes of the Scenery class.

Write program code for the `GetScenery()` method.

You should use the `GetDetails()` method that the `Scenery` class inherits from the `GameElement` class.

---
Write program code for the `AnimatedElement` class as detailed above.

Create an instance of an `AnimatedElement` named `YourPlayer`. This element has the same dimensions as a `GiftBox`, but, when created, is placed in the top left of the screen instead. The other values for the `YourPlayer` instance are shown in the table above.

The `AnimatedElement` class should extend the functionality of the `GetDetails()` method by containing a `GetAnimeDetails()` method.

---
