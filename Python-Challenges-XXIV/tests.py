import unittest
from main import *

# Add imports here!
from io import StringIO

class UnitTests(unittest.TestCase):

  # Add initialization code here!
  NONPRIVATE = []

  def test_showplaytime_method(self):
    
        # Failure message: 
    
        # Your ShowPlayTime method should return the CD's play time.
    
        x = CD("Nevermind", "13/04/1994", True, "Nirvana", "72:13")
    
        self.assertEqual(x.ShowPlayTime(), "72:13")
    
    
        x = CD("Nevermind", "13/04/1994", True, "Nirvana", "72:13")
    
        self.assertEqual(x.ShowPlayTime(), "72:13")

  def test_member_introduction_method(self):
        x = Member("Jim", "Davidson", "12/03/1978", "M")
    
        self.assertEqual(x.Introduction(), "Hello, I'm Jim Davidson.")
    
    
        x = Member("Jim", "Davidson", "12/03/1978", "M")
    
        self.assertEqual(x.Introduction(), "Hello, I'm Jim Davidson.")
    

  def test_statechange_rtest2(self):
      # Enter code here
        x = SafetyDepositBox()
    
        x.SetState("Open-NoCode")
    
        x.SetNewCode("1234")
    
        from unittest.mock import patch
    
        with patch('sys.stdin', StringIO("R")):
    
          s = {i:j for i, j in x.__dict__.items()}
    
          self.assertEqual(s["_SafetyDepositBox__Code"], "1234")
    
          
    
    
        x = SafetyDepositBox()
    
        x.SetState("Open-NoCode")
    
        x.SetNewCode("1234")
    
        from unittest.mock import patch
    
        with patch('sys.stdin', StringIO("R")):
    
          s = {i:j for i, j in x.__dict__.items()}
    
          self.assertEqual(s["_SafetyDepositBox__Code"], "1234")
    

  def test_showisbn_method(self):
    
        x = Book("Life of Pi", "21/02/1989", False, "Yann Martel", "0-676-97376-0")
    
        self.assertEqual(x.ShowISBN(), "0-676-97376-0")
    
    
        x = Book("Life of Pi", "21/02/1989", False, "Yann Martel", "0-676-97376-0")
    
        self.assertEqual(x.ShowISBN(), "0-676-97376-0")

  def test_statechange_correctcode(self):
      # Enter code here
        x = SafetyDepositBox()
    
        x.SetState("Locked")
    
        x.SetNewCode("1234")
    
        
    
        from unittest.mock import patch
    
        with patch('sys.stdin', StringIO('1234')):
    
          self.assertEqual(x.StateChange(), "Open-CodeSet")
    
          
    
    
        x = SafetyDepositBox()
    
        x.SetState("Locked")
    
        x.SetNewCode("1234")
    
        
    
        from unittest.mock import patch
    
        with patch('sys.stdin', StringIO('1234')):
    
          self.assertEqual(x.StateChange(), "Open-CodeSet")
    

  def test_statechange_incorrectcodeformat(self):
    
        x = SafetyDepositBox()
    
        
    
        x.SetState("Locked")
    
        from unittest.mock import patch
    
        with patch('sys.stdin', StringIO('12345')):
    
          self.assertEqual(x.StateChange(), "Error - code format incorrect")
    
          
    
    
        x = SafetyDepositBox()
    
        
    
        x.SetState("Locked")
    
        from unittest.mock import patch
    
        with patch('sys.stdin', StringIO('12345')):
    
          self.assertEqual(x.StateChange(), "Error - code format incorrect")
    

  def test_statechange_correctcode2(self):
      # Enter code here
      
        x = SafetyDepositBox()
    
        
    
        x.SetNewCode("1234")
    
        x.SetState("Closed")
    
        from unittest.mock import patch
    
        with patch('sys.stdin', StringIO('1234')):
    
        
    
          s = {i:j for i, j in x.__dict__.items()}
    
          self.assertEqual(x.StateChange(), "Locked")
    
          
    
    
        x = SafetyDepositBox()
    
        
    
        x.SetNewCode("1234")
    
        x.SetState("Closed")
    
        from unittest.mock import patch
    
        with patch('sys.stdin', StringIO('1234')):
    
        
    
          s = {i:j for i, j in x.__dict__.items()}
    
          self.assertEqual(x.StateChange(), "Locked")
    

  def test_showartist_method(self):
      # Enter code here
        x = CD("Nevermind", "13/04/1994", True, "Nirvana", "72:13")
    
        self.assertEqual(x.ShowArtist(), "Nirvana")
    
    
        x = CD("Nevermind", "13/04/1994", True, "Nirvana", "72:13")
    
        self.assertEqual(x.ShowArtist(), "Nirvana")
    

  def test_statechange_wrongcode(self):
      # Enter code here
        x = SafetyDepositBox()
    
        
    
        x.SetNewCode("7777")
    
        x.SetState("Open-CodeSet")
    
        from unittest.mock import patch
    
        with patch('sys.stdin', StringIO('7776')):
    
          self.assertEqual(x.StateChange(), "Error - does not match set code.")
    
          
    
    
        x = SafetyDepositBox()
    
        
    
        x.SetNewCode("7777")
    
        x.SetState("Open-CodeSet")
    
        from unittest.mock import patch
    
        with patch('sys.stdin', StringIO('7776')):
    
          self.assertEqual(x.StateChange(), "Error - does not match set code.")

  def test_statechange_setnewcode(self):
      # Enter code here
        x = SafetyDepositBox()
    
        
    
        x.SetNewCode("")
    
        x.SetState("Open-NoCode")
    
        from unittest.mock import patch
    
        with patch('sys.stdin', StringIO('7654')):
    
          self.assertEqual(x.StateChange() ,'Code set to: 7654')
    
        
    
          
    
    
        x = SafetyDepositBox()
    
        
    
        x.SetNewCode("")
    
        x.SetState("Open-NoCode")
    
        from unittest.mock import patch
    
        with patch('sys.stdin', StringIO('7654')):
    
          self.assertEqual(x.StateChange() ,'Code set to: 7654')
    
        
    

  def test_showauthor_method(self):
        x = Book("Life of Pi", "21/02/1989", False, "Yann Martel", "0-676-97376-0")
    
        self.assertEqual(x.ShowAuthor(), "Yann Martel")
    
    
        x = Book("Life of Pi", "21/02/1989", False, "Yann Martel", "0-676-97376-0")
    
        self.assertEqual(x.ShowAuthor(), "Yann Martel")

  def test_statechange_rtest(self):
      # Enter code here
        x = SafetyDepositBox()
    
        
    
        x.SetState("Open-CodeSet")
    
        from unittest.mock import patch
    
        with patch('sys.stdin', StringIO("R")):
    
          x.StateChange()
    
          s = {i:j for i, j in x.__dict__.items()}
    
          self.assertEqual(s["_SafetyDepositBox__Code"], "")
    
          self.assertEqual(s["_SafetyDepositBox__State"], "Open-NoCode")
    
          
    
    
        x = SafetyDepositBox()
    
        
    
        x.SetState("Open-CodeSet")
    
        from unittest.mock import patch
    
        with patch('sys.stdin', StringIO("R")):
    
          x.StateChange()
    
          s = {i:j for i, j in x.__dict__.items()}
    
          self.assertEqual(s["_SafetyDepositBox__Code"], "")
    
          self.assertEqual(s["_SafetyDepositBox__State"], "Open-NoCode")
    

  def test_valid_function(self):
        valid = ["0000", "2299", "9876"]
    
        invalid = ["01235", "999", "abc", "875a", "912.2", " 9872"]
    
        
    
        for v in valid:
    
          self.assertEqual(Valid(v), True)
    
        
    
        for v in invalid:
    
          self.assertEqual(Valid(v), False)
    
    
        valid = ["0000", "2299", "9876"]
    
        invalid = ["01235", "999", "abc", "875a", "912.2", " 9872"]
    
        
    
        for v in valid:
    
          self.assertEqual(Valid(v), True)
    
        
    
        for v in invalid:
    
          self.assertEqual(Valid(v), False)

  def test_setstate_method(self):
      # Enter code here
    
        x = SafetyDepositBox()
    
        x.SetState("Open-CodeSet")
    
        s = {i:j for i, j in x.__dict__.items()}
    
        self.assertEqual(s["_SafetyDepositBox__State"], "Open-CodeSet")
    
        
    
        x.SetState("Open-NoCode")
    
        s = {i:j for i, j in x.__dict__.items()}
    
        self.assertEqual(s["_SafetyDepositBox__State"], "Open-NoCode")
    
    
        x = SafetyDepositBox()
    
        x.SetState("Open-CodeSet")
    
        s = {i:j for i, j in x.__dict__.items()}
    
        self.assertEqual(s["_SafetyDepositBox__State"], "Open-CodeSet")
    
        
    
        x.SetState("Open-NoCode")
    
        s = {i:j for i, j in x.__dict__.items()}
    
        self.assertEqual(s["_SafetyDepositBox__State"], "Open-NoCode")
    

  def test_reset_method(self):
    
        x = SafetyDepositBox()
    
        x.SetNewCode("0011")
    
        x.Reset()
    
        s = {i:j for i, j in x.__dict__.items()}
    
        self.assertEqual(s["_SafetyDepositBox__Code"], "")
    
    
        x = SafetyDepositBox()
    
        x.SetNewCode("0011")
    
        x.Reset()
    
        s = {i:j for i, j in x.__dict__.items()}
    
        self.assertEqual(s["_SafetyDepositBox__Code"], "")

  def test_setnewcode_method(self):
        x = SafetyDepositBox()
    
        x.SetNewCode("9999")
    
        s = {i:j for i, j in x.__dict__.items()}
    
        
    
        self.assertEqual(s["_SafetyDepositBox__Code"], "9999")
    
    
        x = SafetyDepositBox()
    
        x.SetNewCode("9999")
    
        s = {i:j for i, j in x.__dict__.items()}
    
        
    
        self.assertEqual(s["_SafetyDepositBox__Code"], "9999")
    

  def test_safetydepositbox_private_attributes(self):
        x = SafetyDepositBox()
    
        attributes = x.__dict__.keys()
    
        for attr in attributes:
    
          attr = attr.replace("_SafetyDepositBox", "")
    
          if attr[:2] != "__" and attr not in self.NONPRIVATE:
    
            raise Exception("SafetyDepositBox  attribute {} is not set as private.".format(attr))
    
              
    
        
    
          
    
    
        x = SafetyDepositBox()
    
        attributes = x.__dict__.keys()
    
        for attr in attributes:
    
          attr = attr.replace("_SafetyDepositBox", "")
    
          if attr[:2] != "__" and attr not in self.NONPRIVATE:
    
            raise Exception("SafetyDepositBox  attribute {} is not set as private.".format(attr))
    
              
    

  def test_safetydepositbox_constructor(self):
        # Failure message: 
    
        # I should be able to initialise an instance of your SafetyDepositBox class. This class constructor takes no arguments - the code should be initialised to an empty string and the safe should be set to the default state.
    
        try:
    
          x = SafetyDepositBox()
    
        except Exception:
    
          raise Exception("Failed to initialise an instance of your SafetyDepositBox class.")
    
          
    
        try:
    
          inits = x.__dict__.items()
    
          for i, j in inits:
    
            if i == "_SafetyDepositBox__State":
    
              self.assertEqual(j, "Open-NoCode")
    
            if i == "_SafetyDepositBox__Code":
    
              self.assertEqual(j, "")
    
        except Exception:
    
          raise Exception("SafetyDepositBox attribute values were not initialised correctly.")
    
    
        try:
    
          x = SafetyDepositBox()
    
        except Exception:
    
          raise Exception("Failed to initialise an instance of your SafetyDepositBox class.")
    
          
    
        try:
    
          inits = x.__dict__.items()
    
          for i, j in inits:
    
            if i == "_SafetyDepositBox__State":
    
              self.assertEqual(j, "Open-NoCode")
    
            if i == "_SafetyDepositBox__Code":
    
              self.assertEqual(j, "")
    
        except Exception:
    
          raise Exception("SafetyDepositBox attribute values were not initialised correctly.")
    

  def test_cd_private_attributes(self):
    
        x = CD("Nevermind", "13/04/1994", True, "Nirvana", "72:13")
    
        attributes = x.__dict__.keys()
    
        for attr in attributes:
    
          attr = attr.replace("_CD", "").replace("_StockItem","")
    
          if attr[:2] != "__" and attr not in self.NONPRIVATE:
    
            raise Exception("CD  attribute {} is not set as private.".format(attr))
    
              
    
        
    
          
    
    
        x = CD("Nevermind", "13/04/1994", True, "Nirvana", "72:13")
    
        attributes = x.__dict__.keys()
    
        for attr in attributes:
    
          attr = attr.replace("_CD", "").replace("_StockItem","")
    
          if attr[:2] != "__" and attr not in self.NONPRIVATE:
    
            raise Exception("CD  attribute {} is not set as private.".format(attr))
    

  def test_cd_constructor(self):
        try:
    
          x = CD("Nevermind", "13/04/1994", True, "Nirvana", "72:13")
    
        except Exception:
    
          raise Exception("Failed to initialise an instance of your CD class.")
    
          
    
        try:
    
          self.assertIn("StockItem", str([CD.__bases__][0]))
    
        except:
    
          raise Exception("CD class is not a sub class of StockItem super class.")
    
    
        try:
    
          x = CD("Nevermind", "13/04/1994", True, "Nirvana", "72:13")
    
        except Exception:
    
          raise Exception("Failed to initialise an instance of your CD class.")
    
          
    
        try:
    
          self.assertIn("StockItem", str([CD.__bases__][0]))
    
        except:
    
          raise Exception("CD class is not a sub class of StockItem super class.")

  def test_book_private_attributes(self):
        x = Book("Life of Pi", "21/02/1989", False, "Yann Martel", "0-676-97376-0")
    
        attributes = x.__dict__.keys()
    
        for attr in attributes:
    
          attr = attr.replace("_Book", "").replace("_StockItem","")
    
          if attr[:2] != "__" and attr not in self.NONPRIVATE:
    
            raise Exception("Book attribute {} is not set as private.".format(attr))
    
              
    
        
    
          
    
    
        x = Book("Life of Pi", "21/02/1989", False, "Yann Martel", "0-676-97376-0")
    
        attributes = x.__dict__.keys()
    
        for attr in attributes:
    
          attr = attr.replace("_Book", "").replace("_StockItem","")
    
          if attr[:2] != "__" and attr not in self.NONPRIVATE:
    
            raise Exception("Book attribute {} is not set as private.".format(attr))
    

  def test_book_constructor(self):
        try:
    
          x = Book("Life of Pi", "21/02/1989", False, "Yann Martel", "0-676-97376-0")
    
        except Exception:
    
          raise Exception("Failed to initialise an instance of your Book class.")
    
          
    
        
    
        try:
    
          self.assertIn("StockItem", str([Book.__bases__][0]))
    
        except:
    
          raise Exception("Book class is not a sub class of StockItem super class.")
    
    
        try:
    
          x = Book("Life of Pi", "21/02/1989", False, "Yann Martel", "0-676-97376-0")
    
        except Exception:
    
          raise Exception("Failed to initialise an instance of your Book class.")
    
          
    
        
    
        try:
    
          self.assertIn("StockItem", str([Book.__bases__][0]))
    
        except:
    
          raise Exception("Book class is not a sub class of StockItem super class.")
    

  def test_stockitem_private_attributes(self):
        x = StockItem("Star Wars", "03/03/2003", True)
    
        attributes = x.__dict__.keys()
    
        for attr in attributes:
    
          attr = attr.replace("_StockItem", "")
    
          if attr[:2] != "__" and attr not in self.NONPRIVATE:
    
            raise Exception("StockItem attribute {} is not set as private.".format(attr))
    
              
    
        
    
          
    
    
        x = StockItem("Star Wars", "03/03/2003", True)
    
        attributes = x.__dict__.keys()
    
        for attr in attributes:
    
          attr = attr.replace("_StockItem", "")
    
          if attr[:2] != "__" and attr not in self.NONPRIVATE:
    
            raise Exception("StockItem attribute {} is not set as private.".format(attr))

  def test_showonloan_method(self):
    
        x = StockItem("Alice In Wonderland", "30/09/1980", False)
    
        self.assertEqual(x.ShowOnLoan(), False)
    
    
        x = StockItem("Alice In Wonderland", "30/09/1980", False)
    
        self.assertEqual(x.ShowOnLoan(), False)
    

  def test_showdateacquired_method(self):
    
        x = StockItem("Pink Panther", "30/03/1976", True)
    
        self.assertEqual(x.ShowDateAcquired(), "30/03/1976")
    
    
        x = StockItem("Pink Panther", "30/03/1976", True)
    
        self.assertEqual(x.ShowDateAcquired(), "30/03/1976")

  def test_showtitle_method(self):
    
        x = StockItem("Godzilla", "21/01/1993", True)
    
        self.assertEqual(x.ShowTitle(), "Godzilla")
    
    
        x = StockItem("Godzilla", "21/01/1993", True)
    
        self.assertEqual(x.ShowTitle(), "Godzilla")

  def test_stockitem_constructor(self):
        try:
    
          x = StockItem("Life of Pi", "21/02/1989", False)
    
        except Exception:
    
          raise Exception("Failed to initialise an instance of your StockItem class.")
    
    
        try:
    
          x = StockItem("Life of Pi", "21/02/1989", False)
    
        except Exception:
    
          raise Exception("Failed to initialise an instance of your StockItem class.")
    

  def test_member_displayfullname_method(self):
        x = Member("Jim", "Davidson", "12/03/1978", "M")
    
        self.assertEqual(x.DisplayFullnameAndDateOfBirth(), "Jim Davidson 12/03/1978")
    
    
        x = Member("Jim", "Davidson", "12/03/1978", "M")
    
        self.assertEqual(x.DisplayFullnameAndDateOfBirth(), "Jim Davidson 12/03/1978")
    

  def test_bmxjudge_test(self):
        self.assertEqual(BMXJudge.DisplayFullnameAndDateOfBirth(), "Omar Ellaboudy 17/03/1993")
    
        self.assertEqual(BMXJudge.Introduction(), "Hello, I'm Omar Ellaboudy.")
    
    
        self.assertEqual(BMXJudge.DisplayFullnameAndDateOfBirth(), "Omar Ellaboudy 17/03/1993")
    
        self.assertEqual(BMXJudge.Introduction(), "Hello, I'm Omar Ellaboudy.")

  def test_official_private_attributes(self):
        x = Official("Din", "Winnasubapon", "03/03/2003", "M", "Ball Boy", True)
    
        attributes = x.__dict__.keys()
    
        for attr in attributes:
    
          attr = attr.replace("_Official", "").replace("_Member","")
    
          if attr[:2] != "__" and attr not in self.NONPRIVATE:
    
            raise Exception("Official attribute {} is not set as private.".format(attr))
    
              
    
        
    
          
    
    
        x = Official("Din", "Winnasubapon", "03/03/2003", "M", "Ball Boy", True)
    
        attributes = x.__dict__.keys()
    
        for attr in attributes:
    
          attr = attr.replace("_Official", "").replace("_Member","")
    
          if attr[:2] != "__" and attr not in self.NONPRIVATE:
    
            raise Exception("Official attribute {} is not set as private.".format(attr))
    

  def test_official_constructor(self):
        try:
    
          x = Official("Arwun", "Sananarayan", "21/02/1989", "F", "Stats Analyst", False)
    
        except Exception:
    
          raise Exception("Failed to initialise an instance of your Official class.")
    
        
    
        
    
        try:
    
          self.assertIn("Member", str([Official.__bases__][0]))
    
        except:
    
          raise Exception("Official class is not a sub class of Member super class.")
    
    
        try:
    
          x = Official("Arwun", "Sananarayan", "21/02/1989", "F", "Stats Analyst", False)
    
        except Exception:
    
          raise Exception("Failed to initialise an instance of your Official class.")
    
        
    
        
    
        try:
    
          self.assertIn("Member", str([Official.__bases__][0]))
    
        except:
    
          raise Exception("Official class is not a sub class of Member super class.")

  def test_competitor_introduction_method(self):
    
        x = Competitor("Jim", "Davidson", "12/03/1978", "M", "Snooker")
    
        self.assertEqual(x.Introduction(), "Hello, I'm Jim Davidson and my sport is Snooker.")
    
    
        x = Competitor("Jim", "Davidson", "12/03/1978", "M", "Snooker")
    
        self.assertEqual(x.Introduction(), "Hello, I'm Jim Davidson and my sport is Snooker.")
    
    

  def test_competitor_private_attributes(self):
        x = Competitor("Sy", "Yann", "01/01/1956", "M", "Hockey")
    
        attributes = x.__dict__.keys()
    
        for attr in attributes:
    
          attr = attr.replace("_Competitor","").replace("_Member","")
    
          if attr[:2] != "__" and attr not in self.NONPRIVATE:
    
            raise Exception("Competitor attribute {} is not set as private.".format(attr))
    
              
    
        
    
          
    
    
        x = Competitor("Sy", "Yann", "01/01/1956", "M", "Hockey")
    
        attributes = x.__dict__.keys()
    
        for attr in attributes:
    
          attr = attr.replace("_Competitor","").replace("_Member","")
    
          if attr[:2] != "__" and attr not in self.NONPRIVATE:
    
            raise Exception("Competitor attribute {} is not set as private.".format(attr))
    
              
    

  def test_competitor_constructor(self):
        try:
    
          x = Competitor("Bob", "Jones", "12/12/2009", "M", "Badminton")
    
        except Exception:
    
          raise Exception("Failed to initialise an instance of your Competitor class.")
    
          
    
        try:
    
          self.assertIn("Member", str([Competitor.__bases__][0]))
    
        except:
    
          raise Exception("Competitor class is not a sub class of Member super class.")
    
    
        try:
    
          x = Competitor("Bob", "Jones", "12/12/2009", "M", "Badminton")
    
        except Exception:
    
          raise Exception("Failed to initialise an instance of your Competitor class.")
    
          
    
        try:
    
          self.assertIn("Member", str([Competitor.__bases__][0]))
    
        except:
    
          raise Exception("Competitor class is not a sub class of Member super class.")

  def test_member_private_attributes(self):
        x = Member("Sally", "Yui", "01/03/2001", "F")
    
        attributes = x.__dict__.keys()
    
        for attr in attributes:
    
          attr = attr.replace("_Member", "")
    
          if attr[:2] != "__" and attr not in self.NONPRIVATE:
    
            raise Exception("Member attribute {} is not set as private.".format(attr))
    
              
    
        
    
          
    
    
        x = Member("Sally", "Yui", "01/03/2001", "F")
    
        attributes = x.__dict__.keys()
    
        for attr in attributes:
    
          attr = attr.replace("_Member", "")
    
          if attr[:2] != "__" and attr not in self.NONPRIVATE:
    
            raise Exception("Member attribute {} is not set as private.".format(attr))
    

  def test_member_constructor_declaration(self):
        try:
    
          x = Member("Bob", "Jones", "12/12/2009", "M")
    
        except Exception:
    
          raise Exception("Failed to initialise an instance of your Member class.")
    
          
    
    
        try:
    
          x = Member("Bob", "Jones", "12/12/2009", "M")
    
        except Exception:
    
          raise Exception("Failed to initialise an instance of your Member class.")

  def test_newbook_instance(self):
    
    
        self.assertEqual(NewBook.ShowISBN(), "099111")
    
        self.assertEqual(NewBook.ShowOnLoan(), False)
    
        try:
    
          NewBook.ShowArtist()
    
          raise Exception("NewBook should be an instance of a Book object.")
    
        except Exception as e:
    
          pass
    

  def test_statechange_nocode(self):
      # Enter code here
        x = SafetyDepositBox()
    
        
    
        x.SetNewCode("1234")
    
        x.SetState("Open-CodeSet")
    
        from unittest.mock import patch
    
        with patch('sys.stdin', StringIO("")):
    
          s = {i:j for i, j in x.__dict__.items()}
    
          self.assertEqual(x.StateChange(), "Closed")
    
          
    
    
        x = SafetyDepositBox()
    
        
    
        x.SetNewCode("1234")
    
        x.SetState("Open-CodeSet")
    
        from unittest.mock import patch
    
        with patch('sys.stdin', StringIO("-")):
    
          s = {i:j for i, j in x.__dict__.items()}
    
          self.assertEqual(x.StateChange(), "Closed")

if __name__ == '__main__':
  unittest.main()