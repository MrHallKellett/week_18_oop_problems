_i='_PrintAccount__LastName'
_h='onlacc1'
_g='Robin Hellums,Terrence Taing,Gregg Demay,Yuki Bizier,Madalene Boll,Lloyd Theisen,Ramonita Dalby,Trent Bosley,Markus Hake,Sabina Mizell,Darleen Brisco,Saran Danforth,Shawnee Augustus,Eleanor Didomenico,Meghann Smyth,Luis Vincent,Ola Detrick,Lashawn Kirkham,Freida Pineiro,Valeri Oritz'
_f='MC Baz'
_e='jimjon1'
_d='Intermediate'
_c='Not Qualified'
_b='Only Account'
_a='Only'
_Z='mcbaz1'
_Y='Baz'
_X='Jimmy'
_W='Jim'
_V='red-brick.png'
_U='_PrintAccount__FirstName'
_T='Beginner'
_S='sys.stdin'
_R='123'
_Q='\n'
_P='Account'
_O='123456'
_N='brick.png'
_M=None
_L='kurcob3'
_K='Cobain'
_J='Kurt'
_I='valid123'
_H='_PrintAccount__PrintID'
_G='finalplayer'
_F='_PrintAccount__Credits'
_E='square'
_D='triangle'
_C=' '
_B=False
_A=True
import unittest
from main import*
from io import StringIO
from unittest.mock import patch
class UnitTests(unittest.TestCase):
	def redirect_output(self,*args,end=_Q):
		if args:
			for a in args:self.outputs.append(a);self.outputs.append(end)
		else:self.outputs.append(end)
	def setUp(self):self.outputs=[]
	def test_test_set_first_name_param(self):x=PrintAccount(_W,'Jones',_e);x.SetFirstName(_X)
	def test_test_get_scenery_method(self):B='X position: 25\nY position: 25\nWidth: 100\nHeight: 100\nImage filename: bomb.png\nCauses damage: True\nDamage points: 1000';A='bomb.png';Bomb=Scenery(25,25,100,100,A,_A,1000);expected=B;self.assertEquals(Bomb.GetScenery().lower().replace(_C,''),expected.lower().replace(_C,''));Bomb=Scenery(25,25,100,100,A,_A,1000);expected=B;self.assertEquals(Bomb.GetScenery().lower().replace(_C,''),expected.lower().replace(_C,''))
	def test_test__check_game_element_class(self):Brick=GameElement(0,0,10,10,_N);Brick=GameElement(0,0,10,10,_N)
	def test_test_set_player_id_invalids(self):
		A='thisoneistooolong';x=Player(_O);self.assertEquals(x.GetPlayerID(),_O);inputs=[_R,A,'',_I]
		with patch(_S,StringIO(_Q.join(inputs))):x.SetPlayerID()
		self.assertEquals(x.GetPlayerID(),_I);x=Player(_O);self.assertEquals(x.GetPlayerID(),_O);inputs=[_R,A,'',_I]
		with patch(_S,StringIO(_Q.join(inputs))):x.SetPlayerID()
		self.assertEquals(x.GetPlayerID(),_I)
	def test_test_add_medium_credits(self):new=PrintAccount(_J,_K,_L);new.AddCredits(12);add_credits_result=dict(new.__dict__.items())[_F];self.assertEquals(add_credits_result,375)
	def test_test_add_credits_no_new_class_properties_local_only(self):new=PrintAccount(_J,_K,_L);new.AddCredits(1);add_credits_result=dict(new.__dict__.items())[_F];self.assertEquals(add_credits_result,75);new.AddCredits(2);add_credits_result=dict(new.__dict__.items())[_F];self.assertEquals(add_credits_result,125);new.AddCredits(11);add_credits_result=dict(new.__dict__.items())[_F];self.assertEquals(add_credits_result,425);priv_prop_length=len(list(new.__dict__.items()));self.assertEquals(priv_prop_length,4)
	def test_test_get_name_after_change(self):new=PrintAccount('MC',_Y,_Z);self.assertEquals(new.GetName(),_f);new.SetFirstName('Barry');self.assertEquals(new.GetName(),'Barry Baz')
	def test_test_animated_element(self):A='X position: 0\nY position: 0\nWidth: 50\nHeight: 75\nImage filename: player.png\nAnimation fps: 60\nDirection: Left\nStrength: 2000\nHealth: 100';self.assertIsInstance(YourPlayer,AnimatedElement);expected=A;self.assertEquals(YourPlayer.GetAnimeDetails().lower().replace(_C,''),expected.lower().replace(_C,''));self.assertIsInstance(YourPlayer,AnimatedElement);expected=A;self.assertEquals(YourPlayer.GetAnimeDetails().lower().replace(_C,''),expected.lower().replace(_C,''))
	def test_test_multiple_accounts_w_collisions(self):
		B='Printer';A='Keen';names=_g.split(',');global StudentAccounts,NumberOfStudents;StudentAccounts=[PrintAccount(A,B,'keepri1')]
		for n in names:fore,name=n.split(_C);id=(fore[:3]+name[:3]+'1').lower();StudentAccounts.append(PrintAccount(fore,name,id))
		StudentAccounts.insert(9,PrintAccount(A,B,'keepri2'));StudentAccounts.append(PrintAccount(A,B,'keepri3'));StudentAccounts+=[_M]*(1000-len(StudentAccounts));i=len(names)+3;NumberOfStudents=i-1;StudentAccounts=CreateID(A,B);self.assertEquals(StudentAccounts[i].GetName(),'Keen Printer');print_id_of_next_account=dict(StudentAccounts[i].__dict__.items())[_H];self.assertEquals(print_id_of_next_account,'keepri4')
	def test_test_one_student_account(self):global StudentAccounts,NumberOfStudents;one_account=PrintAccount(_a,_P,_h);StudentAccounts=[one_account]+[_M]*999;NumberOfStudents=1;StudentAccounts=CreateID('Next',_P);self.assertEquals(StudentAccounts[0].GetName(),_b);self.assertEquals(StudentAccounts[1].GetName(),'Next Account');print_id_of_next_account=dict(StudentAccounts[1].__dict__.items())[_H];self.assertEquals(print_id_of_next_account,'nexacc1')
	def test_test_empty_student_accounts(self):global StudentAccounts,NumberOfStudents;StudentAccounts=[_M]*1000;NumberOfStudents=0;StudentAccounts=CreateID('First',_P);self.assertEquals(StudentAccounts[0].GetName(),'First Account');print_id_of_first_account=dict(StudentAccounts[0].__dict__.items())[_H];self.assertEquals(print_id_of_first_account,'firacc1')
	def test_test_create_player_procedure(self):
		A='Frog123';inputs=[A,'77']
		with patch(_S,StringIO(_Q.join(inputs))):
			with patch('builtins.print',side_effect=self.redirect_output):JoannePlayer=CreatePlayer();self.assertEquals(JoannePlayer.GetPlayerID(),A);self.assertEquals(JoannePlayer.GetScore(),77);self.assertEquals(JoannePlayer.GetCategory(),_T);self.assertIn(_T,self.outputs[-5:])
	def test_test__test_compare_snap(self):MyCard=Card(3,_D);YourCard=Card(3,_D);self.assertEquals(Compare(MyCard,YourCard),-1);MyCard=Card(3,_D);YourCard=Card(3,_D);self.assertEquals(Compare(MyCard,YourCard),-1)
	def test_test_print_account_params(self):x=PrintAccount('Bob','Smith','bobsmi1')
	def test_test_print_account_param_inits(self):C='earpat2';B='Patravee';A='Earth';p=PrintAccount(A,B,C);first_name_set_to=dict(p.__dict__.items())[_U];last_name_set_to=dict(p.__dict__.items())[_i];printid_set_to=dict(p.__dict__.items())[_H];self.assertEquals(first_name_set_to,A);self.assertEquals(last_name_set_to,B);self.assertEquals(printid_set_to,C)
	def test_test_print_account_credits_init(self):new=PrintAccount('Boris','Johnson','borjoh9');credits_set_to=dict(new.__dict__.items())[_F];self.assertEquals(credits_set_to,50)
	def test_test_set_first_name_result(self):x=PrintAccount(_W,'Jones',_e);first_name_init_to=dict(x.__dict__.items())[_U];self.assertEquals(first_name_init_to,_W);x.SetFirstName(_X);first_name_set_to=dict(x.__dict__.items())[_U];self.assertEquals(first_name_set_to,_X)
	def test_test_get_name_result(self):new=PrintAccount('MC',_Y,_Z);self.assertEquals(new.GetName(),_f)
	def test_test_get_name_other_params_still_same(self):C='Joyce';B='joydav1';A='Davidson';p=PrintAccount('Joy',A,B);self.assertEquals(p.GetName(),'Joy Davidson');p.SetFirstName(C);self.assertEquals(p.GetName(),'Joyce Davidson');credits_set_to=dict(p.__dict__.items())[_F];self.assertEquals(credits_set_to,50);first_name_set_to=dict(p.__dict__.items())[_U];last_name_set_to=dict(p.__dict__.items())[_i];printid_set_to=dict(p.__dict__.items())[_H];self.assertEquals(first_name_set_to,C);self.assertEquals(last_name_set_to,A);self.assertEquals(printid_set_to,B)
	def test_test_add_credits_params(self):new=PrintAccount(_J,_K,_L);new.AddCredits(10)
	def test_test_add_credits_result(self):new=PrintAccount(_J,_K,_L);add_credits_return_val=new.AddCredits(4);self.assertEquals(add_credits_return_val,_M)
	def test_test_multiple_accounts(self):
		names=_g.split(',');global StudentAccounts,NumberOfStudents;StudentAccounts=[]
		for n in names:fore,name=n.split(_C);id=(fore[:3]+name[:3]+'1').lower();StudentAccounts.append(PrintAccount(fore,name,id))
		StudentAccounts+=[_M]*(1000-len(StudentAccounts));i=len(names);NumberOfStudents=i;StudentAccounts=CreateID('Davie','Printfirst');self.assertEquals(StudentAccounts[i].GetName(),'Davie Printfirst');print_id_of_next_account=dict(StudentAccounts[i].__dict__.items())[_H];self.assertEquals(print_id_of_next_account,'davpri1')
	def test_test_one_student_account_collision(self):global StudentAccounts,NumberOfStudents;one_account=PrintAccount(_a,_P,_h);StudentAccounts=[one_account]+[_M]*999;NumberOfStudents=1;StudentAccounts=CreateID(_a,_P);self.assertEquals(StudentAccounts[0].GetName(),_b);self.assertEquals(StudentAccounts[1].GetName(),_b);print_id_of_next_account=dict(StudentAccounts[1].__dict__.items())[_H];self.assertEquals(print_id_of_next_account,'onlacc2')
	def test_test_global_array_in_pseudocode(self):self.assertIn(StudentAccountsInPseudo,['DECLARE StudentAccounts: ARRAY[1:1000] OF PrintAccount','DECLARE StudentAccounts: ARRAY[0:999] OF PrintAccount'])
	def test_test_get_name_call(self):new=PrintAccount('MC',_Y,_Z);new.GetName()
	def test_test_add_big_credits(self):new=PrintAccount(_J,_K,_L);new.AddCredits(21);add_credits_result=dict(new.__dict__.items())[_F];self.assertEquals(add_credits_result,625)
	def test_test_create_player(self):x=Player('zug231')
	def test_test_get_score(self):x=Player(_O);self.assertEquals(x.GetScore(),0)
	def test_test_get_category(self):x=Player('abc123');self.assertEquals(x.GetCategory(),_c)
	def test_test_get_player_id(self):A='12345';x=Player(A);self.assertEquals(x.GetPlayerID(),A)
	def test_test__set_score(self):x=Player(_R);self.assertEquals(x.GetScore(),0);x.SetScore(6);self.assertEquals(x.GetScore(),6);x.SetScore(x.GetScore()+len(x.GetPlayerID()));self.assertEquals(x.GetScore(),9)
	def test_test_set_score_validation(self):x=Player(_R);self.assertEquals(x.SetScore(7),_A);self.assertEquals(x.SetScore(-5435),_B);self.assertEquals(x.SetScore(0),_A);self.assertEquals(x.SetScore(-1),_B);self.assertEquals(x.SetScore(150),_A);self.assertEquals(x.SetScore(151),_B);self.assertEquals(x.GetScore(),150)
	def test_test_set_player_id_valid(self):
		A='zsjfioj';x=Player(A);self.assertEquals(x.GetPlayerID(),A)
		with patch(_S,StringIO(_I)):x.SetPlayerID()
		self.assertEquals(x.GetPlayerID(),_I)
	def test_test_set_category_intermediate(self):x=Player(_G);x.SetScore(120);x.SetCategory();self.assertEquals(x.GetCategory(),_d);x=Player(_G);x.SetScore(120);x.SetCategory();self.assertEquals(x.GetCategory(),_d)
	def test_test_set_category_advanced(self):A='Advanced';x=Player(_G);x.SetScore(121);x.SetCategory();self.assertEquals(x.GetCategory(),A);x=Player(_G);x.SetScore(121);x.SetCategory();self.assertEquals(x.GetCategory(),A)
	def test_test_set_category_beginner(self):x=Player(_G);x.SetScore(50);x.SetCategory();self.assertEquals(x.GetCategory(),_T);x.SetScore(81);x.SetCategory();self.assertEquals(x.GetCategory(),_d);x=Player(_G);x.SetScore(50);x.SetCategory();self.assertEquals(x.GetCategory(),_T);x.SetScore(81);x.SetCategory()
	def test_test_book_record(self):
		E='This is a a record. No attributes should be set as private.';D='July 11, 1961';C='9780446310789';B='Harper Lee';A='To Kill A Mocking Bird';ToKillAMockingBird=Book();ToKillAMockingBird.Title=A;ToKillAMockingBird.Author=B;ToKillAMockingBird.ISBN=C;ToKillAMockingBird.Fiction=_A;ToKillAMockingBird.LastRead=D;attributes=ToKillAMockingBird.__dict__.keys()
		for attr in attributes:
			if attr[:2]=='__':raise Exception(E.format(attr))
		ToKillAMockingBird=Book();ToKillAMockingBird.Title=A;ToKillAMockingBird.Author=B;ToKillAMockingBird.ISBN=C;ToKillAMockingBird.Fiction=_A;ToKillAMockingBird.LastRead=D;attributes=ToKillAMockingBird.__dict__.keys()
		for attr in attributes:
			if attr[:2]=='__':raise Exception(E.format(attr))
	def test_test__create_card(self):x=Card(5,_E);x=Card(5,_E)
	def test_test__create_cards_shape_validation(self):
		try:x=Card(-1,_E);error_thrown=_B
		except InvalidNumberError:error_thrown=_A
		self.assertEquals(error_thrown,_A)
		try:x=Card(-1,_E);error_thrown=_B
		except InvalidNumberError:error_thrown=_A
		self.assertEquals(error_thrown,_A)
	def test_test__check_game_element_get_details(self):Brick=GameElement(0,0,10,10,_N);expected='X position: 0\nY position: 0\nWidth: 10\nHeight: 10\nImage filename: brick.png';self.assertEquals(Brick.GetDetails().lower().replace(_C,''),expected.lower().replace(_C,''))
	def test_test__check_game_element_private_properties(self):
		Brick=GameElement(0,0,10,10,_N)
		try:Brick.PostionX;fail=_B
		except:fail=_A
		self.assertEquals(fail,_A);Brick=GameElement(0,0,10,10,_N)
		try:Brick.PostionX;fail=_B
		except:fail=_A
		self.assertEquals(fail,_A)
	def test_test_set_score_not_qualified(self):x=Player(_G);x.SetScore(49);x.SetCategory();self.assertEquals(x.GetCategory(),_c);self.assertEquals(x.SetScore(-1),_B);x=Player(_G);x.SetScore(49);x.SetCategory();self.assertEquals(x.GetCategory(),_c);self.assertEquals(x.SetScore(-1),_B)
	def test_test__create_cards_number_validation(self):
		A='pineapple'
		try:x=Card(1,A);error_thrown=_B
		except InvalidShapeError:error_thrown=_A
		self.assertEquals(error_thrown,_A)
		try:x=Card(1,A);error_thrown=_B
		except InvalidShapeError:error_thrown=_A
		self.assertEquals(error_thrown,_A)
	def test_test_test_ones(self):
		self.assertIsInstance(OneS,Card)
		try:OneS.Shape;public_properties=_A
		except:public_properties=_B
		self.assertEquals(public_properties,_B);self.assertEquals(OneS.GetShape(),_E);self.assertEquals(OneS.GetNumber(),1);self.assertIsInstance(OneS,Card)
		try:OneS.Shape;public_properties=_A
		except:public_properties=_B
		self.assertEquals(public_properties,_B);self.assertEquals(OneS.GetShape(),_E);self.assertEquals(OneS.GetNumber(),1)
	def test_test_test_compare_greater(self):MyCard=Card(3,_D);YourCard=Card(4,_D);self.assertEquals(Compare(MyCard,YourCard),4);MyCard2=Card(7,_E);YourCard2=Card(5,_D);self.assertEquals(Compare(MyCard2,YourCard2),7);MyCard=Card(3,_D);YourCard=Card(4,_D);self.assertEquals(Compare(MyCard,YourCard),4);MyCard2=Card(7,_E);YourCard2=Card(5,_D);self.assertEquals(Compare(MyCard2,YourCard2),7)
	def test_test_test_compare_same(self):MyCard=Card(3,_D);YourCard=Card(3,_E);self.assertEquals(Compare(MyCard,YourCard),3);MyCard=Card(3,_D);YourCard=Card(3,_E);self.assertEquals(Compare(MyCard,YourCard),3)
	def test_test_scenery_class(self):DeadlyBrick=Scenery(0,0,10,10,_V,_A,50);DeadlyBrick=Scenery(0,0,10,10,_V,_A,50)
	def test_test_give_damage_method(self):A='black-brick.png';DeadlyBrick=Scenery(0,0,10,10,_V,_A,50);self.assertEquals(DeadlyBrick.GiveDamage(),50);HarmlessBrick=Scenery(0,0,10,10,A,_B,33);self.assertEquals(HarmlessBrick.GiveDamage(),0);DeadlyBrick=Scenery(0,0,10,10,_V,_A,50);self.assertEquals(DeadlyBrick.GiveDamage(),50);HarmlessBrick=Scenery(0,0,10,10,A,_B,33);self.assertEquals(HarmlessBrick.GiveDamage(),0)
	def test_test_add_small_credits(self):new=PrintAccount(_J,_K,_L);new.AddCredits(4);add_credits_result=dict(new.__dict__.items())[_F];self.assertEquals(add_credits_result,150)
	def test_test_giftbox(self):self.assertIsInstance(GiftBox,Scenery);self.assertEquals(GiftBox.GiveDamage(),50);self.assertIsInstance(GiftBox,Scenery);self.assertEquals(GiftBox.GiveDamage(),50)
if __name__=='__main__':unittest.main()