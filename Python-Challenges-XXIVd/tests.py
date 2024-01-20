import unittest
from main import *

# Add imports here!
from io import StringIO
from unittest.mock import patch

class UnitTests(unittest.TestCase):

  # Add initialization code here!
  def redirect_output(self, *args, end="\n"):
    if args:
      for a in args:
        self.outputs.append(a)
        self.outputs.append(end)
    else:
      self.outputs.append(end)

  def setUp(self):
      # Add setup code here!
      self.outputs = []

  def test_test_set_first_name_param(self):
        x = PrintAccount("Jim", "Jones", "jimjon1")
    
        x.SetFirstName("Jimmy")
    

  def test_test_get_scenery_method(self):
        Bomb = Scenery(25, 25, 100, 100, "bomb.png", True, 1000)
    
        expected = "X position: 25\nY position: 25\nWidth: 100\nHeight: 100\nImage filename: bomb.png\nCauses damage: True\nDamage points: 1000"
    
        
    
        self.assertEquals(Bomb.GetScenery().lower().replace(" ", ""), expected.lower().replace(" ", ""))
    
    
        Bomb = Scenery(25, 25, 100, 100, "bomb.png", True, 1000)
    
        expected = "X position: 25\nY position: 25\nWidth: 100\nHeight: 100\nImage filename: bomb.png\nCauses damage: True\nDamage points: 1000"
    
        
    
        self.assertEquals(Bomb.GetScenery().lower().replace(" ", ""), expected.lower().replace(" ", ""))
    

  def test_test__check_game_element_class(self):
        Brick = GameElement(0, 0, 10, 10, "brick.png")
    
    
        Brick = GameElement(0, 0, 10, 10, "brick.png")

  def test_test_set_player_id_invalids(self):
    
        x = Player("123456")
    
        self.assertEquals(x.GetPlayerID(), "123456")
    
        inputs = ["123", "thisoneistooolong", "", "valid123"]
    
        with patch('sys.stdin', StringIO("\n".join(inputs))):
    
          x.SetPlayerID()
    
        self.assertEquals(x.GetPlayerID(), "valid123")
    
    
        pass
    
        
    
        
    
        x = Player("123456")
    
        self.assertEquals(x.GetPlayerID(), "123456")
    
        inputs = ["123", "thisoneistooolong", "", "valid123"]
    
        with patch('sys.stdin', StringIO("\n".join(inputs))):
    
          x.SetPlayerID()
    
        self.assertEquals(x.GetPlayerID(), "valid123")

  def test_test_add_medium_credits(self):
        new = PrintAccount("Kurt", "Cobain", "kurcob3")
    
        new.AddCredits(12)
    
        add_credits_result = dict(new.__dict__.items()) ['_PrintAccount__Credits']
    
        self.assertEquals(add_credits_result, 375)
    

  def test_test_add_credits_no_new_class_properties_local_only(self):
        new = PrintAccount("Kurt", "Cobain", "kurcob3")
    
        new.AddCredits(1)
    
        add_credits_result = dict(new.__dict__.items()) ['_PrintAccount__Credits']
    
        self.assertEquals(add_credits_result, 75)
    
        new.AddCredits(2)
    
        add_credits_result = dict(new.__dict__.items()) ['_PrintAccount__Credits']
    
        self.assertEquals(add_credits_result, 125)
    
        new.AddCredits(11)
    
        add_credits_result = dict(new.__dict__.items()) ['_PrintAccount__Credits']
    
        self.assertEquals(add_credits_result, 425)
    
        priv_prop_length = len(list(new.__dict__.items()))
    
        self.assertEquals(priv_prop_length, 4)

  def test_test_get_name_after_change(self):
    
        new = PrintAccount("MC", "Baz", "mcbaz1")
    
        self.assertEquals(new.GetName(), "MC Baz")
    
        new.SetFirstName("Barry")
    
        self.assertEquals(new.GetName(), "Barry Baz")
    

  def test_test_animated_element(self):
        self.assertIsInstance(YourPlayer, AnimatedElement)
    
        expected = "X position: 0\nY position: 0\nWidth: 50\nHeight: 75\nImage filename: player.png\nAnimation fps: 60\nDirection: Left\nStrength: 2000\nHealth: 100"
    
        
    
        self.assertEquals(YourPlayer.GetAnimeDetails().lower().replace(" ", ""), expected.lower().replace(" ", ""))
    
    
        self.assertIsInstance(YourPlayer, AnimatedElement)
    
        expected = "X position: 0\nY position: 0\nWidth: 50\nHeight: 75\nImage filename: player.png\nAnimation fps: 60\nDirection: Left\nStrength: 2000\nHealth: 100"
    
        
    
        self.assertEquals(YourPlayer.GetAnimeDetails().lower().replace(" ", ""), expected.lower().replace(" ", ""))
    

  def test_test_multiple_accounts_w_collisions(self):
    
        names = """Robin Hellums,Terrence Taing,Gregg Demay,Yuki Bizier,Madalene Boll,Lloyd Theisen,Ramonita Dalby,Trent Bosley,Markus Hake,Sabina Mizell,Darleen Brisco,Saran Danforth,Shawnee Augustus,Eleanor Didomenico,Meghann Smyth,Luis Vincent,Ola Detrick,Lashawn Kirkham,Freida Pineiro,Valeri Oritz""".split(",")
    
        
    
        
    
        
    
        global StudentAccounts, NumberOfStudents
    
        
    
        StudentAccounts = [PrintAccount("Keen", "Printer", "keepri1")]
    
        
    
        for n in names:
    
          fore, name = n.split(" ")
    
          id = (fore[:3] + name[:3] + '1').lower()
    
          StudentAccounts.append( PrintAccount(fore, name, id))
    
          
    
        StudentAccounts.insert(9, PrintAccount("Keen", "Printer", "keepri2"))
    
          
    
        StudentAccounts.append(PrintAccount("Keen", "Printer", "keepri3"))
    
        
    
        StudentAccounts += ([None] * (1000-len(StudentAccounts)))
    
        i = len(names) + 3
    
        NumberOfStudents = i-1
    
        StudentAccounts = CreateID("Keen", "Printer")
    
        
    
        self.assertEquals(StudentAccounts[i].GetName(), "Keen Printer")
    
        print_id_of_next_account = dict(StudentAccounts[i].__dict__.items()) ['_PrintAccount__PrintID']
    
        self.assertEquals(print_id_of_next_account, "keepri4")

  def test_test_one_student_account(self):
        global StudentAccounts, NumberOfStudents
    
        
    
        one_account = PrintAccount("Only", "Account", "onlacc1")
    
        StudentAccounts = [one_account] + ([None] * 999)
    
        NumberOfStudents = 1
    
        StudentAccounts = CreateID("Next", "Account")
    
        
    
        self.assertEquals(StudentAccounts[0].GetName(), "Only Account")
    
        self.assertEquals(StudentAccounts[1].GetName(), "Next Account")
    
        print_id_of_next_account = dict(StudentAccounts[1].__dict__.items()) ['_PrintAccount__PrintID']
    
        self.assertEquals(print_id_of_next_account, "nexacc1")
    

  def test_test_empty_student_accounts(self):
        global StudentAccounts, NumberOfStudents
    
        
    
        StudentAccounts = ([None] * 1000)
    
        NumberOfStudents = 0
    
        StudentAccounts = CreateID("First", "Account")
    
        self.assertEquals(StudentAccounts[0].GetName(), "First Account")
    
        print_id_of_first_account = dict(StudentAccounts[0].__dict__.items()) ['_PrintAccount__PrintID']
    
        self.assertEquals(print_id_of_first_account, "firacc1")
    

  def test_test_create_player_procedure(self):
    
        inputs = ["Frog123", "77"]
    
    
        
    
        with patch('sys.stdin', StringIO("\n".join(inputs))):
    
          with patch('builtins.print', side_effect=self.redirect_output):
    
            JoannePlayer = CreatePlayer()
    
            self.assertEquals(JoannePlayer.GetPlayerID(), "Frog123")
        
            
        
            self.assertEquals(JoannePlayer.GetScore(), 77)
        
            
        
            self.assertEquals(JoannePlayer.GetCategory(), "Beginner")
        
            
        
            self.assertIn("Beginner", self.outputs[-5:])

  def test_test__test_compare_snap(self):
        MyCard = Card(3, "triangle")
    
        YourCard = Card(3, "triangle")
    
        
    
        self.assertEquals(Compare(MyCard, YourCard), -1)
    
    
        MyCard = Card(3, "triangle")
    
        YourCard = Card(3, "triangle")
    
        
    
        self.assertEquals(Compare(MyCard, YourCard), -1)
    

  def test_test_print_account_params(self):
    
        x = PrintAccount("Bob", "Smith", "bobsmi1")
    

  def test_test_print_account_param_inits(self):
        p = PrintAccount("Earth", "Patravee", "earpat2")
    
        first_name_set_to = dict(p.__dict__.items()) ['_PrintAccount__FirstName']
    
        last_name_set_to = dict(p.__dict__.items()) ['_PrintAccount__LastName']
    
        printid_set_to = dict(p.__dict__.items()) ['_PrintAccount__PrintID']
    
        self.assertEquals(first_name_set_to, "Earth")
    
        self.assertEquals(last_name_set_to, "Patravee")
    
        self.assertEquals(printid_set_to, "earpat2")
    

  def test_test_print_account_credits_init(self):
        new = PrintAccount("Boris", "Johnson", "borjoh9")
    
        credits_set_to = dict(new.__dict__.items()) ['_PrintAccount__Credits']
    
        self.assertEquals(credits_set_to, 50)
    

  def test_test_set_first_name_result(self):
    
        x = PrintAccount("Jim", "Jones", "jimjon1")
    
        first_name_init_to = dict(x.__dict__.items()) ['_PrintAccount__FirstName']
    
        self.assertEquals(first_name_init_to, "Jim")
    
        x.SetFirstName("Jimmy")
    
        first_name_set_to = dict(x.__dict__.items()) ['_PrintAccount__FirstName']
    
        self.assertEquals(first_name_set_to, "Jimmy")
    
    

  def test_test_get_name_result(self):
    
        new = PrintAccount("MC", "Baz", "mcbaz1")
    
        self.assertEquals(new.GetName(), "MC Baz")
    
    

  def test_test_get_name_other_params_still_same(self):
    
        p = PrintAccount("Joy", "Davidson", "joydav1")
    
        self.assertEquals(p.GetName(), "Joy Davidson")
    
        p.SetFirstName("Joyce")
    
        self.assertEquals(p.GetName(), "Joyce Davidson")
    
        credits_set_to = dict(p.__dict__.items()) ['_PrintAccount__Credits']
    
        self.assertEquals(credits_set_to, 50)
    
        first_name_set_to = dict(p.__dict__.items()) ['_PrintAccount__FirstName']
    
        last_name_set_to = dict(p.__dict__.items()) ['_PrintAccount__LastName']
    
        printid_set_to = dict(p.__dict__.items()) ['_PrintAccount__PrintID']
    
        self.assertEquals(first_name_set_to, "Joyce")
    
        self.assertEquals(last_name_set_to, "Davidson")
    
        self.assertEquals(printid_set_to, "joydav1")
    

  def test_test_add_credits_params(self):
        new = PrintAccount("Kurt", "Cobain", "kurcob3")
    
        new.AddCredits(10)
    

  def test_test_add_credits_result(self):
    
        new = PrintAccount("Kurt", "Cobain", "kurcob3")
    
        add_credits_return_val = new.AddCredits(4)
    
        self.assertEquals(add_credits_return_val, None)
    

  def test_test_multiple_accounts(self):
        names = """Robin Hellums,Terrence Taing,Gregg Demay,Yuki Bizier,Madalene Boll,Lloyd Theisen,Ramonita Dalby,Trent Bosley,Markus Hake,Sabina Mizell,Darleen Brisco,Saran Danforth,Shawnee Augustus,Eleanor Didomenico,Meghann Smyth,Luis Vincent,Ola Detrick,Lashawn Kirkham,Freida Pineiro,Valeri Oritz""".split(",")
    
        
    
        global StudentAccounts, NumberOfStudents
    
        
    
        StudentAccounts = []
    
        
    
        for n in names:
    
          fore, name = n.split(" ")
    
          id = (fore[:3] + name[:3] + '1').lower()
    
          StudentAccounts.append( PrintAccount(fore, name, id))
    
        
    
        StudentAccounts += ([None] * (1000-len(StudentAccounts)))
    
        i = len(names)
    
        NumberOfStudents = i
    
        StudentAccounts = CreateID("Davie", "Printfirst")
    
        
    
        self.assertEquals(StudentAccounts[i].GetName(), "Davie Printfirst")
    
        print_id_of_next_account = dict(StudentAccounts[i].__dict__.items()) ['_PrintAccount__PrintID']
    
        self.assertEquals(print_id_of_next_account, "davpri1")
    

  def test_test_one_student_account_collision(self):
    
        global StudentAccounts, NumberOfStudents
    
        
    
        one_account = PrintAccount("Only", "Account", "onlacc1")
    
        StudentAccounts = [one_account] + ([None] * 999)
    
        NumberOfStudents = 1
    
        
    
        StudentAccounts = CreateID("Only", "Account")
    
        
    
        self.assertEquals(StudentAccounts[0].GetName(), "Only Account")
    
        self.assertEquals(StudentAccounts[1].GetName(), "Only Account")
    
        print_id_of_next_account = dict(StudentAccounts[1].__dict__.items()) ['_PrintAccount__PrintID']
    
        self.assertEquals(print_id_of_next_account, "onlacc2")
    

  def test_test_global_array_in_pseudocode(self):
    
        self.assertIn(StudentAccountsInPseudo, ["DECLARE StudentAccounts: ARRAY[1:1000] OF PrintAccount", "DECLARE StudentAccounts: ARRAY[0:999] OF PrintAccount"])
    
    

  def test_test_get_name_call(self):
    
        new = PrintAccount("MC", "Baz", "mcbaz1")
    
        new.GetName()

  def test_test_add_big_credits(self):
    
        new = PrintAccount("Kurt", "Cobain", "kurcob3")
    
        new.AddCredits(21)
    
        add_credits_result = dict(new.__dict__.items()) ['_PrintAccount__Credits']
    
        self.assertEquals(add_credits_result, 625)
    

  def test_test_create_player(self):
    
        x = Player("zug231")

  def test_test_get_score(self):
    
    
        x = Player("123456")
    
        self.assertEquals(x.GetScore(), 0)

  def test_test_get_category(self):
    
        x = Player("abc123")
    
        self.assertEquals(x.GetCategory(), "Not Qualified")

  def test_test_get_player_id(self):
    
    
        x = Player("12345")
    
        self.assertEquals(x.GetPlayerID(), "12345")
    

  def test_test__set_score(self):
    
        x = Player("123")
    
        self.assertEquals(x.GetScore(), 0)
    
        x.SetScore(6)
    
        self.assertEquals(x.GetScore(), 6)
    
        x.SetScore(x.GetScore() + len(x.GetPlayerID()))
    
        self.assertEquals(x.GetScore(), 9)
    

  def test_test_set_score_validation(self):
        x = Player("123")
    
        self.assertEquals(x.SetScore(7), True)
    
        self.assertEquals(x.SetScore(-5435), False)
    
        self.assertEquals(x.SetScore(0), True)
    
        self.assertEquals(x.SetScore(-1), False)
    
        self.assertEquals(x.SetScore(150), True)
    
        self.assertEquals(x.SetScore(151), False)
    
        self.assertEquals(x.GetScore(), 150)

  def test_test_set_player_id_valid(self):
    
        
    
        x = Player("zsjfioj")
    
        self.assertEquals(x.GetPlayerID(), "zsjfioj")
    
        with patch("sys.stdin", StringIO("valid123")):
    
          x.SetPlayerID()
    
        self.assertEquals(x.GetPlayerID(), "valid123")
    
    
        pass
    

  def test_test_set_category_intermediate(self):
        x = Player("finalplayer")
    
        x.SetScore(120)
    
        x.SetCategory()
    
        self.assertEquals(x.GetCategory(), "Intermediate")
    
    
        x = Player("finalplayer")
    
        x.SetScore(120)
    
        x.SetCategory()
    
        self.assertEquals(x.GetCategory(), "Intermediate")
    

  def test_test_set_category_advanced(self):
        x = Player("finalplayer")
    
        x.SetScore(121)
    
        x.SetCategory()
    
        self.assertEquals(x.GetCategory(), "Advanced")
    
    
        x = Player("finalplayer")
    
        x.SetScore(121)
    
        x.SetCategory()
    
        self.assertEquals(x.GetCategory(), "Advanced")
    

  def test_test_set_category_beginner(self):
    
        x = Player("finalplayer")
    
        x.SetScore(50)
    
        x.SetCategory()
    
        self.assertEquals(x.GetCategory(), "Beginner")
    
        x.SetScore(81)
    
        x.SetCategory()
    
        self.assertEquals(x.GetCategory(), "Intermediate")
    
    
        x = Player("finalplayer")
    
        x.SetScore(50)
    
        x.SetCategory()
    
        self.assertEquals(x.GetCategory(), "Beginner")
    
        x.SetScore(81)
    
        x.SetCategory()
    

  def test_test_book_record(self):
        ToKillAMockingBird = Book()
    
        ToKillAMockingBird.Title = "To Kill A Mocking Bird"
    
        ToKillAMockingBird.Author = "Harper Lee"
    
        ToKillAMockingBird.ISBN = "9780446310789"
    
        ToKillAMockingBird.Fiction = True
    
        ToKillAMockingBird.LastRead = "July 11, 1961"
    
        attributes = ToKillAMockingBird.__dict__.keys()
    
        for attr in attributes:
    
          if attr[:2] == "__":
    
            raise Exception("This is a a record. No attributes should be set as private.".format(attr))
    
    
        ToKillAMockingBird = Book()
    
        ToKillAMockingBird.Title = "To Kill A Mocking Bird"
    
        ToKillAMockingBird.Author = "Harper Lee"
    
        ToKillAMockingBird.ISBN = "9780446310789"
    
        ToKillAMockingBird.Fiction = True
    
        ToKillAMockingBird.LastRead = "July 11, 1961"
    
        attributes = ToKillAMockingBird.__dict__.keys()
    
        for attr in attributes:
    
          if attr[:2] == "__":
    
            raise Exception("This is a a record. No attributes should be set as private.".format(attr))

  def test_test__create_card(self):
    
        x = Card(5, "square")
    
    
        x = Card(5, "square")

  def test_test__create_cards_shape_validation(self):
    
        try:
    
          x = Card(-1, "square")
    
          error_thrown = False
    
        except InvalidNumberError:
    
          error_thrown = True
    
          
    
        self.assertEquals(error_thrown, True)
    
          
    
    
        try:
    
          x = Card(-1, "square")
    
          error_thrown = False
    
        except InvalidNumberError:
    
          error_thrown = True
    
          
    
        self.assertEquals(error_thrown, True)

  def test_test__check_game_element_get_details(self):
        Brick = GameElement(0, 0, 10, 10, "brick.png")
    
        expected = "X position: 0\nY position: 0\nWidth: 10\nHeight: 10\nImage filename: brick.png"
    
        
    
        self.assertEquals(Brick.GetDetails().lower().replace(" ", ""), expected.lower().replace(" ", ""))

  def test_test__check_game_element_private_properties(self):
        Brick = GameElement(0, 0, 10, 10, "brick.png")
    
        try:
    
          Brick.PostionX
    
          fail = False
    
        except:
    
          fail = True
    
          
    
          
    
        self.assertEquals(fail, True)
    
    
        Brick = GameElement(0, 0, 10, 10, "brick.png")
    
        try:
    
          Brick.PostionX
    
          fail = False
    
        except:
          fail = True
    
          
    
          
    
        self.assertEquals(fail, True)

  def test_test_set_score_not_qualified(self):
    
        x = Player("finalplayer")
    
        x.SetScore(49)
    
        x.SetCategory()
    
        self.assertEquals(x.GetCategory(), "Not Qualified")
    
        self.assertEquals(x.SetScore(-1), False)
    
    
        x = Player("finalplayer")
    
        x.SetScore(49)
    
        x.SetCategory()
    
        self.assertEquals(x.GetCategory(), "Not Qualified")
    
        self.assertEquals(x.SetScore(-1), False)

  def test_test__create_cards_number_validation(self):
        try:
    
          x = Card(1, "pineapple")
    
          error_thrown = False
    
        except InvalidShapeError:
    
          error_thrown = True
    
          
    
        self.assertEquals(error_thrown, True)
    
    
        try:
    
          x = Card(1, "pineapple")
    
          error_thrown = False
    
        except InvalidShapeError:
    
          error_thrown = True
    
          
    
        self.assertEquals(error_thrown, True)
    

  def test_test_test_ones(self):
    
        self.assertIsInstance(OneS, Card)
    
        try:
    
          OneS.Shape
    
          public_properties = True
    
        except:
    
          public_properties = False
    
          
    
        self.assertEquals(public_properties, False)
    
        
    
        self.assertEquals(OneS.GetShape(), "square")
    
        self.assertEquals(OneS.GetNumber(), 1)
    
    
        self.assertIsInstance(OneS, Card)
    
        try:
    
          OneS.Shape
    
          public_properties = True
    
        except:
    
          public_properties = False
    
          
    
        self.assertEquals(public_properties, False)
    
        
    
        self.assertEquals(OneS.GetShape(), "square")
    
        self.assertEquals(OneS.GetNumber(), 1)

  def test_test_test_compare_greater(self):
    
        MyCard = Card(3, "triangle")
    
        YourCard = Card(4, "triangle")
    
        self.assertEquals(Compare(MyCard, YourCard), 4)
    
        MyCard2 = Card(7, "square")
    
        YourCard2 = Card(5, "triangle")
    
        self.assertEquals(Compare(MyCard2, YourCard2), 7)
    
    
        MyCard = Card(3, "triangle")
    
        YourCard = Card(4, "triangle")
    
        self.assertEquals(Compare(MyCard, YourCard), 4)
    
        MyCard2 = Card(7, "square")
    
        YourCard2 = Card(5, "triangle")
    
        self.assertEquals(Compare(MyCard2, YourCard2), 7)
    

  def test_test_test_compare_same(self):
    
        MyCard = Card(3, "triangle")
    
        YourCard = Card(3, "square")
    
        
    
        self.assertEquals(Compare(MyCard, YourCard), 3)
    
    
        MyCard = Card(3, "triangle")
    
        YourCard = Card(3, "square")
    
        
    
        self.assertEquals(Compare(MyCard, YourCard), 3)

  def test_test_scenery_class(self):
        DeadlyBrick = Scenery(0, 0, 10, 10, "red-brick.png", True, 50)
    
    
        DeadlyBrick = Scenery(0, 0, 10, 10, "red-brick.png", True, 50)

  def test_test_give_damage_method(self):
        DeadlyBrick = Scenery(0, 0, 10, 10, "red-brick.png", True, 50)
    
        self.assertEquals(DeadlyBrick.GiveDamage(), 50)
    
        HarmlessBrick = Scenery(0, 0, 10, 10, "black-brick.png", False, 33)
    
        self.assertEquals(HarmlessBrick.GiveDamage(), 0)
    
    
        DeadlyBrick = Scenery(0, 0, 10, 10, "red-brick.png", True, 50)
    
        self.assertEquals(DeadlyBrick.GiveDamage(), 50)
    
        HarmlessBrick = Scenery(0, 0, 10, 10, "black-brick.png", False, 33)
    
        self.assertEquals(HarmlessBrick.GiveDamage(), 0)

  def test_test_add_small_credits(self):
        new = PrintAccount("Kurt", "Cobain", "kurcob3")
    
        new.AddCredits(4)
    
        add_credits_result = dict(new.__dict__.items()) ['_PrintAccount__Credits']
    
        self.assertEquals(add_credits_result, 150)

  def test_test_giftbox(self):
        self.assertIsInstance(GiftBox, Scenery)
    
        self.assertEquals(GiftBox.GiveDamage(), 50)
    
    
        self.assertIsInstance(GiftBox, Scenery)
    
        self.assertEquals(GiftBox.GiveDamage(), 50)
    

if __name__ == '__main__':
  unittest.main()