_e='12/12/2009'
_d='Jones'
_c='Bob'
_b='Member'
_a='03/03/2003'
_Z='StockItem'
_Y='Closed'
_X='_Member'
_W='_StockItem'
_V='Locked'
_U='12/03/1978'
_T='Davidson'
_S='Jim'
_R='_SafetyDepositBox__State'
_Q='13/04/1994'
_P='Nevermind'
_O='0-676-97376-0'
_N='Yann Martel'
_M='Life of Pi'
_L='_SafetyDepositBox__Code'
_K='72:13'
_J='Nirvana'
_I='Open-CodeSet'
_H='21/02/1989'
_G='Open-NoCode'
_F='__'
_E='1234'
_D='M'
_C='sys.stdin'
_B=True
_A=False
import unittest
from main import*
from io import StringIO
class UnitTests(unittest.TestCase):
	NONPRIVATE=[]
	def test_showplaytime_method(self):x=CD(_P,_Q,_B,_J,_K);self.assertEqual(x.ShowPlayTime(),_K);x=CD(_P,_Q,_B,_J,_K);self.assertEqual(x.ShowPlayTime(),_K)
	def test_member_introduction_method(self):A="Hello, I'm Jim Davidson.";x=Member(_S,_T,_U,_D);self.assertEqual(x.Introduction(),A);x=Member(_S,_T,_U,_D);self.assertEqual(x.Introduction(),A)
	def test_statechange_rtest2(self):
		x=SafetyDepositBox();x.SetState(_G);x.SetNewCode(_E);from unittest.mock import patch
		with patch(_C,StringIO('R')):s={i:j for(i,j)in x.__dict__.items()};self.assertEqual(s[_L],_E)
		x=SafetyDepositBox();x.SetState(_G);x.SetNewCode(_E);from unittest.mock import patch
		with patch(_C,StringIO('R')):s={i:j for(i,j)in x.__dict__.items()};self.assertEqual(s[_L],_E)
	def test_showisbn_method(self):x=Book(_M,_H,_A,_N,_O);self.assertEqual(x.ShowISBN(),_O);x=Book(_M,_H,_A,_N,_O);self.assertEqual(x.ShowISBN(),_O)
	def test_statechange_correctcode(self):
		x=SafetyDepositBox();x.SetState(_V);x.SetNewCode(_E);from unittest.mock import patch
		with patch(_C,StringIO(_E)):self.assertEqual(x.StateChange(),_I)
		x=SafetyDepositBox();x.SetState(_V);x.SetNewCode(_E);from unittest.mock import patch
		with patch(_C,StringIO(_E)):self.assertEqual(x.StateChange(),_I)
	def test_statechange_incorrectcodeformat(self):
		B='Error - code format incorrect';A='12345';x=SafetyDepositBox();x.SetState(_V);from unittest.mock import patch
		with patch(_C,StringIO(A)):self.assertEqual(x.StateChange(),B)
		x=SafetyDepositBox();x.SetState(_V);from unittest.mock import patch
		with patch(_C,StringIO(A)):self.assertEqual(x.StateChange(),B)
	def test_statechange_correctcode2(self):
		x=SafetyDepositBox();x.SetNewCode(_E);x.SetState(_Y);from unittest.mock import patch
		with patch(_C,StringIO(_E)):s={i:j for(i,j)in x.__dict__.items()};self.assertEqual(x.StateChange(),_V)
		x=SafetyDepositBox();x.SetNewCode(_E);x.SetState(_Y);from unittest.mock import patch
		with patch(_C,StringIO(_E)):s={i:j for(i,j)in x.__dict__.items()};self.assertEqual(x.StateChange(),_V)
	def test_showartist_method(self):x=CD(_P,_Q,_B,_J,_K);self.assertEqual(x.ShowArtist(),_J);x=CD(_P,_Q,_B,_J,_K);self.assertEqual(x.ShowArtist(),_J)
	def test_statechange_wrongcode(self):
		C='Error - does not match set code.';B='7776';A='7777';x=SafetyDepositBox();x.SetNewCode(A);x.SetState(_I);from unittest.mock import patch
		with patch(_C,StringIO(B)):self.assertEqual(x.StateChange(),C)
		x=SafetyDepositBox();x.SetNewCode(A);x.SetState(_I);from unittest.mock import patch
		with patch(_C,StringIO(B)):self.assertEqual(x.StateChange(),C)
	def test_statechange_setnewcode(self):
		B='Code set to: 7654';A='7654';x=SafetyDepositBox();x.SetNewCode('');x.SetState(_G);from unittest.mock import patch
		with patch(_C,StringIO(A)):self.assertEqual(x.StateChange(),B)
		x=SafetyDepositBox();x.SetNewCode('');x.SetState(_G);from unittest.mock import patch
		with patch(_C,StringIO(A)):self.assertEqual(x.StateChange(),B)
	def test_showauthor_method(self):x=Book(_M,_H,_A,_N,_O);self.assertEqual(x.ShowAuthor(),_N);x=Book(_M,_H,_A,_N,_O);self.assertEqual(x.ShowAuthor(),_N)
	def test_statechange_rtest(self):
		x=SafetyDepositBox();x.SetState(_I);from unittest.mock import patch
		with patch(_C,StringIO('R')):x.StateChange();s={i:j for(i,j)in x.__dict__.items()};self.assertEqual(s[_L],'');self.assertEqual(s[_R],_G)
		x=SafetyDepositBox();x.SetState(_I);from unittest.mock import patch
		with patch(_C,StringIO('R')):x.StateChange();s={i:j for(i,j)in x.__dict__.items()};self.assertEqual(s[_L],'');self.assertEqual(s[_R],_G)
	def test_valid_function(self):
		I=' 9872';H='912.2';G='875a';F='abc';E='999';D='01235';C='9876';B='2299';A='0000';valid=[A,B,C];invalid=[D,E,F,G,H,I]
		for v in valid:self.assertEqual(Valid(v),_B)
		for v in invalid:self.assertEqual(Valid(v),_A)
		valid=[A,B,C];invalid=[D,E,F,G,H,I]
		for v in valid:self.assertEqual(Valid(v),_B)
		for v in invalid:self.assertEqual(Valid(v),_A)
	def test_setstate_method(self):x=SafetyDepositBox();x.SetState(_I);s={i:j for(i,j)in x.__dict__.items()};self.assertEqual(s[_R],_I);x.SetState(_G);s={i:j for(i,j)in x.__dict__.items()};self.assertEqual(s[_R],_G);x=SafetyDepositBox();x.SetState(_I);s={i:j for(i,j)in x.__dict__.items()};self.assertEqual(s[_R],_I);x.SetState(_G);s={i:j for(i,j)in x.__dict__.items()};self.assertEqual(s[_R],_G)
	def test_reset_method(self):A='0011';x=SafetyDepositBox();x.SetNewCode(A);x.Reset();s={i:j for(i,j)in x.__dict__.items()};self.assertEqual(s[_L],'');x=SafetyDepositBox();x.SetNewCode(A);x.Reset();s={i:j for(i,j)in x.__dict__.items()};self.assertEqual(s[_L],'')
	def test_setnewcode_method(self):A='9999';x=SafetyDepositBox();x.SetNewCode(A);s={i:j for(i,j)in x.__dict__.items()};self.assertEqual(s[_L],A);x=SafetyDepositBox();x.SetNewCode(A);s={i:j for(i,j)in x.__dict__.items()};self.assertEqual(s[_L],A)
	def test_safetydepositbox_private_attributes(self):
		B='SafetyDepositBox  attribute {} is not set as private.';A='_SafetyDepositBox';x=SafetyDepositBox();attributes=x.__dict__.keys()
		for attr in attributes:
			attr=attr.replace(A,'')
			if attr[:2]!=_F and attr not in self.NONPRIVATE:raise Exception(B.format(attr))
		x=SafetyDepositBox();attributes=x.__dict__.keys()
		for attr in attributes:
			attr=attr.replace(A,'')
			if attr[:2]!=_F and attr not in self.NONPRIVATE:raise Exception(B.format(attr))
	def test_safetydepositbox_constructor(self):
		B='SafetyDepositBox attribute values were not initialised correctly.';A='Failed to initialise an instance of your SafetyDepositBox class.'
		try:x=SafetyDepositBox()
		except Exception:raise Exception(A)
		try:
			inits=x.__dict__.items()
			for(i,j)in inits:
				if i==_R:self.assertEqual(j,_G)
				if i==_L:self.assertEqual(j,'')
		except Exception:raise Exception(B)
		try:x=SafetyDepositBox()
		except Exception:raise Exception(A)
		try:
			inits=x.__dict__.items()
			for(i,j)in inits:
				if i==_R:self.assertEqual(j,_G)
				if i==_L:self.assertEqual(j,'')
		except Exception:raise Exception(B)
	def test_cd_private_attributes(self):
		B='CD  attribute {} is not set as private.';A='_CD';x=CD(_P,_Q,_B,_J,_K);attributes=x.__dict__.keys()
		for attr in attributes:
			attr=attr.replace(A,'').replace(_W,'')
			if attr[:2]!=_F and attr not in self.NONPRIVATE:raise Exception(B.format(attr))
		x=CD(_P,_Q,_B,_J,_K);attributes=x.__dict__.keys()
		for attr in attributes:
			attr=attr.replace(A,'').replace(_W,'')
			if attr[:2]!=_F and attr not in self.NONPRIVATE:raise Exception(B.format(attr))
	def test_cd_constructor(self):
		B='CD class is not a sub class of StockItem super class.';A='Failed to initialise an instance of your CD class.'
		try:x=CD(_P,_Q,_B,_J,_K)
		except Exception:raise Exception(A)
		try:self.assertIn(_Z,str([CD.__bases__][0]))
		except:raise Exception(B)
		try:x=CD(_P,_Q,_B,_J,_K)
		except Exception:raise Exception(A)
		try:self.assertIn(_Z,str([CD.__bases__][0]))
		except:raise Exception(B)
	def test_book_private_attributes(self):
		B='Book attribute {} is not set as private.';A='_Book';x=Book(_M,_H,_A,_N,_O);attributes=x.__dict__.keys()
		for attr in attributes:
			attr=attr.replace(A,'').replace(_W,'')
			if attr[:2]!=_F and attr not in self.NONPRIVATE:raise Exception(B.format(attr))
		x=Book(_M,_H,_A,_N,_O);attributes=x.__dict__.keys()
		for attr in attributes:
			attr=attr.replace(A,'').replace(_W,'')
			if attr[:2]!=_F and attr not in self.NONPRIVATE:raise Exception(B.format(attr))
	def test_book_constructor(self):
		B='Book class is not a sub class of StockItem super class.';A='Failed to initialise an instance of your Book class.'
		try:x=Book(_M,_H,_A,_N,_O)
		except Exception:raise Exception(A)
		try:self.assertIn(_Z,str([Book.__bases__][0]))
		except:raise Exception(B)
		try:x=Book(_M,_H,_A,_N,_O)
		except Exception:raise Exception(A)
		try:self.assertIn(_Z,str([Book.__bases__][0]))
		except:raise Exception(B)
	def test_stockitem_private_attributes(self):
		B='StockItem attribute {} is not set as private.';A='Star Wars';x=StockItem(A,_a,_B);attributes=x.__dict__.keys()
		for attr in attributes:
			attr=attr.replace(_W,'')
			if attr[:2]!=_F and attr not in self.NONPRIVATE:raise Exception(B.format(attr))
		x=StockItem(A,_a,_B);attributes=x.__dict__.keys()
		for attr in attributes:
			attr=attr.replace(_W,'')
			if attr[:2]!=_F and attr not in self.NONPRIVATE:raise Exception(B.format(attr))
	def test_showonloan_method(self):B='30/09/1980';A='Alice In Wonderland';x=StockItem(A,B,_A);self.assertEqual(x.ShowOnLoan(),_A);x=StockItem(A,B,_A);self.assertEqual(x.ShowOnLoan(),_A)
	def test_showdateacquired_method(self):B='Pink Panther';A='30/03/1976';x=StockItem(B,A,_B);self.assertEqual(x.ShowDateAcquired(),A);x=StockItem(B,A,_B);self.assertEqual(x.ShowDateAcquired(),A)
	def test_showtitle_method(self):B='21/01/1993';A='Godzilla';x=StockItem(A,B,_B);self.assertEqual(x.ShowTitle(),A);x=StockItem(A,B,_B);self.assertEqual(x.ShowTitle(),A)
	def test_stockitem_constructor(self):
		A='Failed to initialise an instance of your StockItem class.'
		try:x=StockItem(_M,_H,_A)
		except Exception:raise Exception(A)
		try:x=StockItem(_M,_H,_A)
		except Exception:raise Exception(A)
	def test_member_displayfullname_method(self):A='Jim Davidson 12/03/1978';x=Member(_S,_T,_U,_D);self.assertEqual(x.DisplayFullnameAndDateOfBirth(),A);x=Member(_S,_T,_U,_D);self.assertEqual(x.DisplayFullnameAndDateOfBirth(),A)
	def test_bmxjudge_test(self):B="Hello, I'm Omar Ellaboudy.";A='Omar Ellaboudy 17/03/1993';self.assertEqual(BMXJudge.DisplayFullnameAndDateOfBirth(),A);self.assertEqual(BMXJudge.Introduction(),B);self.assertEqual(BMXJudge.DisplayFullnameAndDateOfBirth(),A);self.assertEqual(BMXJudge.Introduction(),B)
	def test_official_private_attributes(self):
		E='Official attribute {} is not set as private.';D='_Official';C='Ball Boy';B='Winnasubapon';A='Din';x=Official(A,B,_a,_D,C,_B);attributes=x.__dict__.keys()
		for attr in attributes:
			attr=attr.replace(D,'').replace(_X,'')
			if attr[:2]!=_F and attr not in self.NONPRIVATE:raise Exception(E.format(attr))
		x=Official(A,B,_a,_D,C,_B);attributes=x.__dict__.keys()
		for attr in attributes:
			attr=attr.replace(D,'').replace(_X,'')
			if attr[:2]!=_F and attr not in self.NONPRIVATE:raise Exception(E.format(attr))
	def test_official_constructor(self):
		E='Official class is not a sub class of Member super class.';D='Failed to initialise an instance of your Official class.';C='Stats Analyst';B='Sananarayan';A='Arwun'
		try:x=Official(A,B,_H,'F',C,_A)
		except Exception:raise Exception(D)
		try:self.assertIn(_b,str([Official.__bases__][0]))
		except:raise Exception(E)
		try:x=Official(A,B,_H,'F',C,_A)
		except Exception:raise Exception(D)
		try:self.assertIn(_b,str([Official.__bases__][0]))
		except:raise Exception(E)
	def test_competitor_introduction_method(self):B="Hello, I'm Jim Davidson and my sport is Snooker.";A='Snooker';x=Competitor(_S,_T,_U,_D,A);self.assertEqual(x.Introduction(),B);x=Competitor(_S,_T,_U,_D,A);self.assertEqual(x.Introduction(),B)
	def test_competitor_private_attributes(self):
		E='Competitor attribute {} is not set as private.';D='_Competitor';C='Hockey';B='01/01/1956';A='Yann';x=Competitor('Sy',A,B,_D,C);attributes=x.__dict__.keys()
		for attr in attributes:
			attr=attr.replace(D,'').replace(_X,'')
			if attr[:2]!=_F and attr not in self.NONPRIVATE:raise Exception(E.format(attr))
		x=Competitor('Sy',A,B,_D,C);attributes=x.__dict__.keys()
		for attr in attributes:
			attr=attr.replace(D,'').replace(_X,'')
			if attr[:2]!=_F and attr not in self.NONPRIVATE:raise Exception(E.format(attr))
	def test_competitor_constructor(self):
		C='Competitor class is not a sub class of Member super class.';B='Failed to initialise an instance of your Competitor class.';A='Badminton'
		try:x=Competitor(_c,_d,_e,_D,A)
		except Exception:raise Exception(B)
		try:self.assertIn(_b,str([Competitor.__bases__][0]))
		except:raise Exception(C)
		try:x=Competitor(_c,_d,_e,_D,A)
		except Exception:raise Exception(B)
		try:self.assertIn(_b,str([Competitor.__bases__][0]))
		except:raise Exception(C)
	def test_member_private_attributes(self):
		D='Member attribute {} is not set as private.';C='01/03/2001';B='Yui';A='Sally';x=Member(A,B,C,'F');attributes=x.__dict__.keys()
		for attr in attributes:
			attr=attr.replace(_X,'')
			if attr[:2]!=_F and attr not in self.NONPRIVATE:raise Exception(D.format(attr))
		x=Member(A,B,C,'F');attributes=x.__dict__.keys()
		for attr in attributes:
			attr=attr.replace(_X,'')
			if attr[:2]!=_F and attr not in self.NONPRIVATE:raise Exception(D.format(attr))
	def test_member_constructor_declaration(self):
		A='Failed to initialise an instance of your Member class.'
		try:x=Member(_c,_d,_e,_D)
		except Exception:raise Exception(A)
		try:x=Member(_c,_d,_e,_D)
		except Exception:raise Exception(A)
	def test_newbook_instance(self):
		self.assertEqual(NewBook.ShowISBN(),'099111');self.assertEqual(NewBook.ShowOnLoan(),_A)
		try:NewBook.ShowArtist();raise Exception('NewBook should be an instance of a Book object.')
		except Exception as e:pass
	def test_statechange_nocode(self):
		x=SafetyDepositBox();x.SetNewCode(_E);x.SetState(_I);from unittest.mock import patch
		with patch(_C,StringIO('')):s={i:j for(i,j)in x.__dict__.items()};self.assertEqual(x.StateChange(),_Y)
		x=SafetyDepositBox();x.SetNewCode(_E);x.SetState(_I);from unittest.mock import patch
		with patch(_C,StringIO('-')):s={i:j for(i,j)in x.__dict__.items()};self.assertEqual(x.StateChange(),_Y)
if __name__=='__main__':unittest.main()