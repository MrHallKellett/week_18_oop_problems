_C=True
_B='01234567898'
_A=False
import unittest
from main import*
class UnitTests(unittest.TestCase):
	def test_create_device(self):x=Device(7);self.assertEqual(x.get_power_state(),_A);x=Device(7);self.assertEqual(x.get_power_state(),_A)
	def test_turn_on(self):x=Device(7);x.turn_on();self.assertEqual(x.get_power_state(),_C);x=Device(7);x.turn_on();self.assertEqual(x.get_power_state(),_C)
	def test_turn_off(self):x=Device(7);x.turn_on();x.turn_off();self.assertEqual(x.get_power_state(),_A);x=Device(7);x.turn_on();x.turn_off();self.assertEqual(x.get_power_state(),_A)
	def test_battery(self):x=Device(50);x.turn_on();self.assertEqual(x.get_battery(),50);x=Device(50);x.turn_on();self.assertEqual(x.get_battery(),50)
	def test_create_phone(self):y=Phone(50,_B);self.assertEqual(y.get_power_state(),_A);y.turn_on();self.assertEqual(y.get_power_state(),_C);self.assertEqual(y.get_battery(),50);y=Phone(50,_B);self.assertEqual(y.get_power_state(),_A);y.turn_on();self.assertEqual(y.get_power_state(),_C);self.assertEqual(y.get_battery(),50)
	def test_create_computer(self):
		z=Computer(100);y=Phone(100,_B);self.assertEqual(z.get_battery(),y.get_battery())
		try:z.set_phone_number(_B);return _A
		except Exception as e:pass
		z=Computer(100);y=Phone(100,_B);self.assertEqual(z.get_battery(),y.get_battery())
		try:z.set_phone_number(_B);return _A
		except Exception as e:pass
	def test_phone_number_error(self):
		B='Invalid phone number!';A='999'
		try:y=Phone(2,A)
		except InvalidPhoneNumber:print(B)
		try:y=Phone(2,A)
		except InvalidPhoneNumber:print(B)
if __name__=='__main__':unittest.main()